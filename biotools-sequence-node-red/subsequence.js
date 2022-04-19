module.exports = function(RED) {
    function subSequence(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
			msg.payload.sequence = msg.payload.sequence.substring(parseInt(config.from) - 1,parseInt(config.to));
            node.send(msg);
        });
    }
    RED.nodes.registerType("get subsequence",subSequence);
}
