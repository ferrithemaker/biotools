module.exports = function(RED) {
    function transcriptionNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var inputchar = "";
            var output = "";
			for (var i = 0; i < msg.payload.sequence.length; i++) {
				inputchar = msg.payload.sequence[i].toLowerCase();
				if (inputchar == 't') {
					inputchar = 'u';
				}
				output += inputchar;
			}
			msg.payload.sequence = output.toUpperCase();
            node.send(msg);
        });
    }
    RED.nodes.registerType("transcription",transcriptionNode);
}
