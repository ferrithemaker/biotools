module.exports = function(RED) {
    function reverseNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            msg.payload.sequence = msg.payload.sequence.split("").reverse().join("");
            node.send(msg);
        });
    }
    RED.nodes.registerType("reverse",reverseNode);
}
