module.exports = function(RED) {
    function seqtypeNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var wrong = false;
        var rna = false;
        var dna = false;
        node.on('input', function(msg) {
			for (var i = 0; i < msg.payload.sequence.length; i++) {
				char = msg.payload.sequence[i].toLowerCase();
				if (config.degenerate == "no") {
						if (char != 'a' && char != 'c' && char != 'g' && 
							char != 't' && char != 'u') {
								wrong = true;
						}
						if (char == 't' && wrong == false) {
							if (rna == false) {
								dna = true;
							} else {
								wrong = true;
							}							
						}
						if (char == 'u' && wrong == false) {
							if (dna == false) { 
								rna = true;
							} else {
								wrong = true;
							}
						}
				} else {
					if (char != 'a' && char != 'c' && char != 'g' && 
						char != 't' && char != 'u' && char != 'k' &&
						char != 's' && char != 'y' && char != 'm' &&
						char != 'w' && char != 'r' && char != 'b' &&
						char != 'd' && char != 'h' && char != 'v' &&
						char != '-' ) {
							wrong = true;
					}
					if (char == 't' && wrong == false) {
							if (rna == false) {
								dna = true;
							} else {
								wrong = true;
							}							
					}
					if (char == 'u' && wrong == false) {
							if (dna == false) { 
								rna = true;
							} else {
								wrong = true;
							}
					}
				}
			}
			if (rna == false && dna ==false) { msg.payload = "undefined"; }
			if (wrong == true) { msg.payload = "wrong sequence"; }
			if (rna == true && wrong == false) { msg.payload = "RNA"; }
			if (dna == true && wrong == false) { msg.payload = "DNA"; }
			node.send(msg);
		});
	}
    RED.nodes.registerType("sequence type",seqtypeNode);
}
