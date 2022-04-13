module.exports = function(RED) {
    function alignmentNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        let flowContext = this.context().flow;
        node.on('input', function(msg) {
			var alignment1 = flowContext.get("alignment1") || null;
			var alignment2 = flowContext.get("alignment2") || null;
			var idvalue = msg.payload.id;
			if (flowContext.get("alignment1") != null && flowContext.get("alignment2") == null &&
				idvalue != flowContext.get("alignment1") ) {
				flowContext.set("alignment2",idvalue);
			}
			if (flowContext.get("alignment1") == null) {
				flowContext.set("alignment1",idvalue);
			}
			if (flowContext.get("alignment1") != null && flowContext.get("alignment2") != null &&
				flowContext.get("alignment1") != flowContext.get("alignment2")) {
				msg.payload = "Els dos valors estan setejats";
				flowContext.set("alignment1",null);
				flowContext.set("alignment2",null);
				node.send(msg);
			}
            
        });
    }
    RED.nodes.registerType("alignment",alignmentNode);
}
