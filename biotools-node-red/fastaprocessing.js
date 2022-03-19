module.exports = function(RED) {
    function fastaProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var seqNumber = 0;
        var output = "";
        var information = "";
        var info;
        var db = "";
        var id = "";
        var infodata1 = "";
        var infodata2 = "";
        var seqFound = false;
        node.on('input', function(msg) {
			lines = msg.payload.split("\n");
			for (var i = 0; i < lines.length; i++) {
				if (lines[i][0] == '>' || lines[i][0] == ';') {
					seqNumber ++;
					if (seqNumber == parseInt(config.number)) {
						// seq. info processing
						info = lines[i].substring(1).split('|');
						if (info.length >= 1) {
							db = info[0];
						}
						if (info.length >= 2) {
							id = info[1];
						}
						if (info.length >= 3) {
							infodata1 = info[2];
						}
						
						if (info.length >= 4) {
							for (var i2 = 3; i2 < info.length; i2++) {
								infodata2 = infodata2 + info[i2];
								if (i2 < info.length -1) {
									infodata2 = infodata2 + '|';
								}
							}
						}
						information = {"db": db, "id": id, "infodata": infodata1, "extrainfo": infodata2}
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
			if (config.seqtype.toLowerCase() == "protein") {
				msg.payload = { "sequence": "", "protein": output.toUpperCase() ,"information": information}
			}
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing FASTA file",fastaProcessingNode);
}
