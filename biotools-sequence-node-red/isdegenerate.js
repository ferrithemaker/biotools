module.exports = function(RED) {
    function isDegenerate(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var degenerate = false;
        node.on('input', function(msg) {
			for (var i = 0; i < msg.payload.sequence.length; i++) {
				inputchar = msg.payload.sequence[i].toLowerCase();
				if (inputchar == 'w' || inputchar == "s" ||
					inputchar == 'm' || inputchar == "k" ||
					inputchar == 'r' || inputchar == "y" ||
					inputchar == 'b' || inputchar == "d" ||
					inputchar == 'h' || inputchar == "v" ||
					inputchar == 'n') {
						degenerate = true;
				}
			}
			if (degenerate == true) {
				msg = [msg,null];
			} else {
				msg = [null,msg];
			}
            node.send(msg);
        });
    }
    RED.nodes.registerType("is degenerate",isDegenerate);
}
