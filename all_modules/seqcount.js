module.exports = function(RED) {
    function seqcountNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var a = 0;
        var c = 0;
        var g = 0;
        var t = 0;
        var u = 0;
        var all = 0;
        node.on('input', function(msg) {
			for (var i = 0; i < msg.payload.sequence.length; i++) {
				char = msg.payload.sequence[i].toLowerCase();
				if (char == "a") {
					a = a + 1;
					all = all + 1;
				}
				if (char == "c") {
					c = c + 1;
					all = all + 1;
				}
				if (char == "g") {
					g = g + 1;
					all = all + 1;
				}
				if (char == "t") {
					t = t + 1;
					all = all + 1;
				}
				if (char == "u") {
					u = u + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "r") {
					a = a + 1;
					g = g + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "y") {
					c = c + 1;
					t = t + 1;
					u = u + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "k") {
					t = t + 1;
					g = g + 1;
					u = u + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "m") {
					a = a + 1;
					c = c + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "s") {
					c = c + 1;
					g = g + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "w") {
					t = t + 1;
					a = a + 1;
					u = u + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "b") {
					c = c + 1;
					g = g + 1;
					u = u + 1;
					t = t + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "d") {
					t = t + 1;
					g = g + 1;
					u = u + 1;
					a = a + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "h") {
					t = t + 1;
					a = a + 1;
					c = c + 1;
					u = u + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "v") {
					a = a + 1;
					c = c + 1;
					g = g + 1;
					all = all + 1;
				}
				if (config.degenerate == "yes" && char == "n") {
					t = t + 1;
					g = g + 1;
					u = u + 1;
					a = a + 1;
					c = c + 1;
					all = all + 1;
				}
			}
			if (config.datatype == "a") {
				msg.payload = a;
			}
			if (config.datatype == "c") {
				msg.payload = c;
			}
			if (config.datatype == "g") {
				msg.payload = g;
			}
			if (config.datatype == "t") {
				msg.payload = t;
			}
			if (config.datatype == "u") {
				msg.payload = u;
			}
			if (config.datatype == "all") {
				msg.payload = all;
			}
			node.send(msg);		
		});
	}
    RED.nodes.registerType("sequence count",seqcountNode);
}
