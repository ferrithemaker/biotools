module.exports = function(RED) {
    function ttratioNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        let flowContext = this.context().flow;
        node.on('input', function(msg) {
			var transitions = 0;
			var transversions = 0;
			var rate = 0;
			var seq1_id = flowContext.get("seq1_id_tt") || null;
			var seq2_id = flowContext.get("seq2_id_tt") || null;
			var idvalue = msg.payload.id;
			if (flowContext.get("seq1_id_tt") != null && flowContext.get("seq2_id_tt") == null &&
				idvalue != flowContext.get("seq1_id_tt") ) {
				flowContext.set("seq2_id_tt",idvalue);
				flowContext.set("seq2_tt",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id_tt") == null) {
				flowContext.set("seq1_id_tt",idvalue);
				flowContext.set("seq1_tt",msg.payload.sequence);
			}
			if (flowContext.get("seq1_id_tt") != null && flowContext.get("seq2_id_tt") != null &&
				flowContext.get("seq1_id_tt") != flowContext.get("seq2_id_tt")) {
				var seq1 = 	flowContext.get("seq1_tt").toLowerCase();
				var seq2 = 	flowContext.get("seq2_tt").toLowerCase();
				flowContext.set("seq1_id_tt",null);
				flowContext.set("seq2_id_tt",null);
				flowContext.set("seq1_tt",null);
				flowContext.set("seq2_tt",null);
				if (seq1.length !== seq2.length) {
					transitions = 0;
					transversions = 0;
					rate = 0;
				} else {
					for (let i = 0; i < seq1.length; i += 1) {
						if (seq1[i] == 'a' && seq2[i] == 'g') {
							transitions += 1;
						}
						if (seq1[i] == 'g' && seq2[i] == 'a') {
							transitions += 1;
						}
						if (seq1[i] == 'c' && (seq2[i] == 't' || seq2[i] == 'u')) {
							transitions += 1;
						}
						if ((seq1[i] == 't' || seq1[i] == 'u') && seq2[i] == 'c') {
							transitions += 1;
						}
						if (seq1[i] == 'a' && seq2[i] == 'c') {
							transversions += 1;
						}
						if (seq1[i] == 'a' && seq2[i] == 'a') {
							transversions += 1;
						}
						if (seq1[i] == 'a' && (seq2[i] == 't' || seq2[i] == 'u')) {
							transversions += 1;
						}
						if ((seq1[i] == 't' || seq1[i] == 'u') && seq2[i] == 'a') {
							transversions += 1;
						}				
					}
					rate = parseFloat(transitions)/parseFloat(transversions);
					rate = rate.toFixed(2);
				}
				msg.payload = { "transitions":transitions, "transversions":transversions, "ratio":rate };
				node.send(msg); 
			}     
        });
    }
    RED.nodes.registerType("transition transversion ratio",ttratioNode);
}
