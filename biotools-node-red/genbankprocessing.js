module.exports = function(RED) {
    function genbankProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var rawOutput;
        var cdsNumber = -1;
        var cds;
        var genBankInfo;
        var cdsArray = [];
        var output = "";
        node.on('input', function(msg) {
			// get INFO
			genBankInfo = msg.payload.substring(0,msg.payload.indexOf('FEATURE'));
			if (config.seqtype.toLowerCase() == "origin") {
				// ORIGIN reads
				rawOutput = msg.payload.substring(msg.payload.indexOf('ORIGIN') + 6);
				for (var i = 0; i < rawOutput.length; i++) {
					char = rawOutput[i].toLowerCase();
					if (char == 'a' || char == 'c' || char == "g" || 
						char == 't' || char == 'u') {
							output += char;
					}			
				}
			}
			if (config.seqtype.toLowerCase() == "cds") {
				// CDS translation
				while ((cdsNumber = msg.payload.indexOf("/translation=",cdsNumber+1)) >= 0) cdsArray.push(cdsNumber);
				cds = cdsArray[config.number-1] + 14;
				while (msg.payload[cds] != '"') {
					output = output + msg.payload[cds];
					cds++;
				}
			}
			if (config.seqtype.toLowerCase() == "origin") {
				msg.payload = { "sequence": output.toUpperCase() ,"protein": "" ,"information": genBankInfo}
			}
			if (config.seqtype.toLowerCase() == "cds") {
				msg.payload = { "sequence": "", "protein": output.toUpperCase() ,"information": genBankInfo}
			}
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing Genbank file",genbankProcessingNode);
}
