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
					if (char == 'a' || char == 'c' || char == "g" || 
						char == 't' || char == 'u') {
						output += char;
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
						char == '-') {
						output += char;
					}
				}
			}
			msg.payload = { "sequence":output }
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing RAW data",rawProcessingNode);
}
