module.exports = function(RED) {
    function fastaProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var seqNumber = 0;
        var output = "";
        var information = "";
        var seqFound = false;
        node.on('input', function(msg) {
			lines = msg.payload.split("\n");
			for (var i=0; i < lines.length; i++) {
				if (lines[i][0] == '>' || lines[i][0] == ';') {
					seqNumber ++;
					if (seqNumber == parseInt(config.number)) {
						information = lines[i].substring(1);
						seqFound = true;
					} else {
						seqFound = false;
					}
				} else {
					if (seqFound == true) {
						output = output + lines[i];
					}
				}
			}
			if (config.seqtype.toLowerCase() == "nucleotides") {
				msg.payload = { "sequence": output.toUpperCase() ,"protein": "" ,"information": information}
			}
			if (config.seqtype.toLowerCase() == "proteins") {
				msg.payload = { "sequence": "", "protein": output.toUpperCase() ,"information": information}
			}
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing FASTA file",fastaProcessingNode);
}
