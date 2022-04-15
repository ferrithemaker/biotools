module.exports = function(RED) {
    function hammingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var hammingValue = 0;
        let flowContext = this.context().flow;
        node.on('input', function(msg) {
			var seq1_id = flowContext.get("seq1_id") || null;
			var seq2_id = flowContext.get("seq2_id") || null;
			var idvalue = msg.payload.id;
			if (flowContext.get("seq1_id") != null && flowContext.get("seq2_id") == null &&
				idvalue != flowContext.get("seq1_id") ) {
				flowContext.set("seq2_id",idvalue);
				flowContext.set("seq2",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id") == null) {
				flowContext.set("seq1_id",idvalue);
				flowContext.set("seq1",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id") != null && flowContext.get("seq2_id") != null &&
				flowContext.get("seq1_id") != flowContext.get("seq2_id")) {
				var seq1 = 	flowContext.get("seq1");
				var seq2 = 	flowContext.get("seq2");
				flowContext.set("seq1_id",null);
				flowContext.set("seq2_id",null);
				flowContext.set("seq1",null);
				flowContext.set("seq2",null);
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
