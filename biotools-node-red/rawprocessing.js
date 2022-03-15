module.exports = function(RED) {
    function rawProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var output = "";
			var char = "";
			for (var i = 0; i < msg.payload.length; i++) {
				char = msg.payload[i].toLowerCase();
				if (config.seqtype.toLowerCase() == "nucleotides") {
					if (config.degenerate == "no") {
						if (char == 'a' || char == 'c' || char == "g" || 
							char == 't' || char == 'u') {
								output += char;
						}
					} else {
						if (char == 'a' || char == 'c' || char == "g" || 
							char == 't' || char == 'u' || char == "k" ||
							char == 's' || char == 'y' || char == "m" ||
							char == 'w' || char == 'r' || char == "b" ||
							char == 'd' || char == 'h' || char == "v" ||
							char == '-' ) {
								output += char;
						}
					}
					
				}
				if (config.seqtype.toLowerCase() == "proteins") {
					if (char == 'a' || char == "d" || char == 'e' ||
						char == 'r' || char == "n" || char == 'c' ||
						char == 'f' || char == "g" || char == 'q' ||
						char == 'h' || char == "i" || char == 'l' ||
						char == 'k' || char == "m" || char == 'p' ||
						char == 's' || char == "y" || char == 't' ||
						char == 'w' || char == "v" || char == 'u' ||
						char == '*' || char == '-') {
							output += char;
					}
				}
			}
			if (config.seqtype.toLowerCase() == "nucleotides") {
				msg.payload = { "sequence": output.toUpperCase() ,"protein": "" ,"information": {"db": "", "id": "", "infodata": "", "extrainfo": ""}}
			}
			if (config.seqtype.toLowerCase() == "proteins") {
				msg.payload = { "sequence": "", "protein": output.toUpperCase() ,"information": {"db": "", "id": "", "infodata": "", "extrainfo": ""}}
			}
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing RAW data",rawProcessingNode);
}
