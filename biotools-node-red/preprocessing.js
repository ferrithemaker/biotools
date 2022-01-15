module.exports = function(RED) {
    function PreProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var output = "";
			var char = "";
			for (var i = 0; i < msg.payload.length; i++) {
				char = msg.payload[i].toLowerCase();
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
			msg.payload = output
            node.send(msg);
        });
    }
    RED.nodes.registerType("preprocessing",PreProcessingNode);
}
