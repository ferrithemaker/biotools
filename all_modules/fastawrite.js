module.exports = function(RED) {
    function fastaWriteNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var output = "";
        var splitseq = "";
        node.on('input', function(msg) {
			output = ">" + msg.payload.information.db;
			if (msg.payload.information.id != "") {
				output = output + "|" + msg.payload.information.id;
				if (msg.payload.information.infodata != "") {
					output = output + "|" + msg.payload.information.infodata;
					if (msg.payload.information.extrainfo != "") {
						output = output + "|" + msg.payload.information.extrainfo;
					}
				}
			} 
			if (config.seqtype.toLowerCase() == "nucleotides") {
				for (let i = 0;i < msg.payload.sequence.length;i++) {
					splitseq = splitseq + msg.payload.sequence[i].toLowerCase();
					if ((i + 1) % 60 == 0) {
						splitseq = splitseq + "\n";
					}
				}
				output = output + "\n" + splitseq + "\n";
			}
			if (config.seqtype.toLowerCase() == "protein") {
				for (let i = 0;i < msg.payload.protein.length;i++) {
					splitseq = splitseq + msg.payload.protein[i].toLowerCase();
					if ((i + 1) % 60 == 0) {
						splitseq = splitseq + "\n";
					}
				}
				output = output + "\n" + splitseq + "\n";
			}
			msg.payload = output;
            node.send(msg);
        });
    }
    RED.nodes.registerType("FASTA file output",fastaWriteNode);
}
