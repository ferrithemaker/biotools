module.exports = function(RED) {
    function ComplementNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var inputchar;
            var outputchar;
            var output = "";
			for (var i = 0; i < msg.payload.length; i++) {
				inputchar = msg.payload[i].toLowerCase();
				outputchar = inputchar;
				if (inputchar == 't') {
					outputchar = 'a'; 
				}
				if (inputchar == 'u') {
					outputchar = 'a'; 
				}
				if (inputchar == 'a' && config.seqtype == "ADN") {
					outputchar = 't';
				}
				if (inputchar == 'a' && config.seqtype == "ARN") {
					outputchar = 'u';
				}
				if (inputchar == 'c') {
					outputchar = 'g';
				}
				if (inputchar == 'g') {
					outputchar = 't';
				}
				output += outputchar;
			}
			msg.payload = output; 		
            node.send(msg);
        });
    }
    RED.nodes.registerType("complement",ComplementNode);
}
