module.exports = function(RED) {
    function TranscriptionNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var inputchar = "";
            var output = "";
			for (var i = 0; i < msg.payload.length; i++) {
				inputchar = msg.payload[i].toLowerCase();
				if (inputchar == 't') {
					inputchar = 'u';
				}
				output += inputchar;
			}
			msg.payload = output;
            node.send(msg);
        });
    }
    RED.nodes.registerType("transcription",TranscriptionNode);
}
