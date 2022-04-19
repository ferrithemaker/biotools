module.exports = function(RED) {
    function complementNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var inputchar;
            var outputchar;
            var output = "";
			for (var i = 0; i < msg.payload.sequence.length; i++) {
				inputchar = msg.payload.sequence[i].toLowerCase();
				outputchar = inputchar;
				if (inputchar == 't') {
					outputchar = 'a'; 
				}
				if (inputchar == 'u') {
					outputchar = 'a'; 
				}
				if (inputchar == 'a' && config.seqtype.toLowerCase() == "dna") {
					outputchar = 't';
				}
				if (inputchar == 'a' && config.seqtype.toLowerCase() == "rna") {
					outputchar = 'u';
				}
				if (inputchar == 'c') {
					outputchar = 'g';
				}
				if (inputchar == 'g') {
					outputchar = 'c';
				}
				if (inputchar == 'w') {
					outputchar = 'w';
				}
				if (inputchar == 's') {
					outputchar = 's';
				}
				if (inputchar == 'm') {
					outputchar = 'k';
				}
				if (inputchar == 'k') {
					outputchar = 'm';
				}
				if (inputchar == 'r') {
					outputchar = 'y';
				}
				if (inputchar == 'y') {
					outputchar = 'r';
				}
				if (inputchar == 'b') {
					outputchar = 'v';
				}
				if (inputchar == 'd') {
					outputchar = 'h';
				}
				if (inputchar == 'h') {
					outputchar = 'd';
				}
				if (inputchar == 'v') {
					outputchar = 'b';
				}
				if (inputchar == 'n') {
					outputchar = 'n';
				}
				output += outputchar;
			}
			msg.payload.sequence = output.toUpperCase(); 		
            node.send(msg);
        });
    }
    RED.nodes.registerType("complement",complementNode);
}
