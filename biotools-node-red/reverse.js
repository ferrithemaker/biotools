module.exports = function(RED) {
    function ReverseNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            msg.payload = msg.payload.str.split("").reverse().join("");
            node.send(msg);
        });
    }
    RED.nodes.registerType("reverse",ReverseNode);
}
