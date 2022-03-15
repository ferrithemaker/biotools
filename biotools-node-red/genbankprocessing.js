module.exports = function(RED) {
    function genbankProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        var rawOutput;
        var output = "";
        node.on('input', function(msg) {
			if (config.seqtype.toLowerCase() == "complete") {
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
			if (config.seqtype.toLowerCase() == "complete") {
				msg.payload = { "sequence": output.toUpperCase() ,"protein": "" ,"information": {"db": "", "id": "", "infodata": "", "extrainfo": ""}}
			}
			if (config.seqtype.toLowerCase() == "cds") {
				// not implemented
				msg.payload = { "sequence": "", "protein": "" ,"information": {"db": "", "id": "", "infodata": "", "extrainfo": ""}}
			}
			msg.payload = output;
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing Genbank file",genbankProcessingNode);
}
