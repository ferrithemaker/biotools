module.exports = function(RED) {
    function fastaProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var output = "";
			var char = "";
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing FASTA file",fastaProcessingNode);
}
