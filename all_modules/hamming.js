module.exports = function(RED) {
    function hammingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        let flowContext = this.context().flow;
        node.on('input', function(msg) {
			var hammingValue = 0;
			var seq1_id = flowContext.get("seq1_id_h") || null;
			var seq2_id = flowContext.get("seq2_id_h") || null;
			var idvalue = msg.payload.id;
			if (flowContext.get("seq1_id_h") != null && flowContext.get("seq2_id_h") == null &&
				idvalue != flowContext.get("seq1_id_h") ) {
				flowContext.set("seq2_id_h",idvalue);
				flowContext.set("seq2_h",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id_h") == null) {
				flowContext.set("seq1_id_h",idvalue);
				flowContext.set("seq1_h",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id_h") != null && flowContext.get("seq2_id_h") != null &&
				flowContext.get("seq1_id_h") != flowContext.get("seq2_id_h")) {
				var seq1 = 	flowContext.get("seq1_h").toLowerCase();
				var seq2 = 	flowContext.get("seq2_h").toLowerCase();
				flowContext.set("seq1_id_h",null);
				flowContext.set("seq2_id_h",null);
				flowContext.set("seq1_h",null);
				flowContext.set("seq2_h",null);
				if (seq1.length !== seq2.length) {
					hammingValue = 0;
				} else {
					for (let i = 0; i < seq1.length; i += 1) {
						if (seq1[i] !== seq2[i]) {
							hammingValue += 1;
						}
					}
				}
				msg.payload = hammingValue;
				node.send(msg);
			}      
        });
    }
    RED.nodes.registerType("hamming distance",hammingNode);
}
