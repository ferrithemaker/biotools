module.exports = function(RED) {
	function wunsch(inA, inB, gap, score) {

    // set default headings
    var headA = 'InputA',
    headB = 'InputB',
    newline = /[\n\r]+/,
    MARKED;

    // if the input sequence A contains newline chars, use the first
    // line as the heading for the sequence
    if (inA.match(newline)) {
        inA = inA.split(newline);
        headA = inA.shift();
        inA = inA.join('');
    }

    // if the input sequence B contains newline chars, use the first
    // line as the heading for the sequence
    if (inB.match(newline)) {
        inB = inB.split(newline);
        headB = inB.shift();
        inB = inB.join('');
    }

    // @type {number}
    var width = inA.length + 1,
    // @type {number}
    height = inB.length + 1,
    // @type {number[][]} map holds the cost map
    map = [[0]],
    // @type {string} outA holds the aligned input A
    outA = '',
    // @type {string} outB holds the aligned output B
    outB = '',
    // @type {string} alignment holds the alignment info
    alignment = '',
    // @type {number} x,y,z are counting variables
    x,y,z;

    // make the sequences index 1
    inA = ' ' + inA;
    inB = ' ' + inB;

    // create left column
    for (x = 1; x < height; x++)
        map[x] = [x * gap];

    // create top row
    for (y = 1; y < width; y++)
        map[0][y] = y * gap;

    // fill the cost map
    for (x = 1; x < height; x++)
        for (y = 1; y < width; y++)
            map[x][y] = Math.max(
                map[x - 1][y - 1] + score(inA[x], inB[y]),
                map[x - 1][y] + gap,
                map[x][y - 1] + gap
            );

    x = height-1;
    y = width-1;


    // calculate alignment
    while (x > 0 || y > 0) {
        z = map[x][y]
        if (MARKED)
            MARKED[x][y] = '\033[1;31m' + MARKED[x][y] + '\033[m';

        if (x > 0 && y > 0 && z === map[x-1][y-1] + score(inA[x], inB[y])) {
            outA = inA[y] + outA;
            outB = inB[x] + outB;
            alignment = (inA[x] === inB[x] ? ':' : '.') + alignment;
            x--; y--;
        } else if (x > 0 && z === map[x-1][y] + gap) {
            outB = inB[x] + outB;
            outA = '-'  + outA;
            alignment = ' '  + alignment;
            x--;
        } else if (y > 0 && z === map[x][y-1] + gap) {
            outB = '-'  + outB;
            outA = inA[y] + outA;
            alignment = ' '  + alignment;
            y--;
        }
    }

    if (MARKED)
        console.log(MARKED.map(function(row){return row.join(' ');}).join('\n'));

    // calculate score
    for (x = 0; x < alignment.length; x++)
        z += alignment[x] === ' ' ? gap : score(outA[x], outB[x]);

    return [
        [headA, outA],
        [headB, outB],
        ['aln', alignment],
        ['score', z]
    ];
}
    function alignmentNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        let flowContext = this.context().flow;
        node.on('input', function(msg) {
			var alignment1 = flowContext.get("seq1_id_al") || null;
			var alignment2 = flowContext.get("seq2_id_al") || null;
			var idvalue = msg.payload.id;
			if (flowContext.get("seq1_id_al") != null && flowContext.get("seq2_id_al") == null &&
				idvalue != flowContext.get("seq1_id_al") ) {
				flowContext.set("seq2_id_al",idvalue);
				flowContext.set("seq2_al",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id_al") == null) {
				flowContext.set("seq1_id_al",idvalue);
				flowContext.set("seq1_al",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id_al") != null && flowContext.get("seq2_id_al") != null &&
				flowContext.get("seq1_id_al") != flowContext.get("seq2_id_al")) {
				var seq1 = 	flowContext.get("seq1_al").toLowerCase();
				var seq2 = 	flowContext.get("seq2_al").toLowerCase();
				flowContext.set("seq1_id_al",null);
				flowContext.set("seq2_id_al",null);
				flowContext.set("seq1_al",null);
				flowContext.set("seq2_al",null);
				var gap = parseInt(config.gap);
				var match = parseInt(config.match);
				var miss = parseInt(config.miss);
				var scorefn = function (seq1, seq2) {return seq1 === seq2 ? match : miss;};
				var r = wunsch(seq1, seq2, gap, scorefn);
				msg.payload = { "output":r };
				node.send(msg);
			}
            
        });
    }
    RED.nodes.registerType("alignment",alignmentNode);
}
