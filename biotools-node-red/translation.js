module.exports = function(RED) {
    function TranslationNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            var inputchar = "";
            var codon = "";
            var proteina = "";
            if (msg.payload.sequence.length % 3 == 0) {
				while (msg.payload.sequence.length >= 3) {
					codon = msg.payload.sequence[0] + msg.payload.sequence[1] + msg.payload.sequence[2];
					msg.payload.sequence = msg.payload.sequence.substring(3);
					codon = codon.toLowerCase();
					if (codon == "gac" || codon == "gau") { proteina += "D"; }
					if (codon == "gaa" || codon == "gag") { proteina += "E"; }
					if (codon == "gca" || codon == "gcc" || codon == "gcg" || codon == "gcu") { proteina += "A"; }
					if (codon == "aga" || codon == "agg" || codon == "cga" || codon == "cgc" || codon == "cgg" || codon == "cgu") { proteina += "R"; }
					if (codon == "aac" || codon == "aau") { proteina += "N"; }
					if (codon == "ugc" || codon == "ugu") { proteina += "C"; }
					if (codon == "uuc" || codon == "uuu") { proteina += "F"; }
					if (codon == "gca" || codon == "ggc" || codon == "ggg" || codon == "ggu") { proteina += "G"; }
					if (codon == "caa" || codon == "cag") { proteina += "Q"; }
					if (codon == "cac" || codon == "cau") { proteina += "H"; }
					if (codon == "aua" || codon == "auc" || codon == "auu") { proteina += "I"; }
					if (codon == "uua" || codon == "uug" || codon == "cua" || codon == "cuc" || codon == "cug" || codon == "cuu") { proteina += "L"; }
					if (codon == "aaa" || codon == "aag") { proteina += "K"; }
					if (codon == "aug") { proteina += "M"; }
					if (codon == "cca" || codon == "ccc" || codon == "ccg" || codon == "ccu") { proteina += "P"; }
					if (codon == "agc" || codon == "agu" || codon == "uca" || codon == "ucc" || codon == "ucg" || codon == "ucu") { proteina += "S"; }
					if (codon == "uac" || codon == "uau") { proteina += "Y"; }
					if (codon == "aca" || codon == "acc" || codon == "acg" || codon == "acu") { proteina += "T"; }
					if (codon == "ugg") { proteina += "W"; }
					if (codon == "gua" || codon == "guc" || codon == "gug" || codon == "guu") { proteina += "V"; }
					if (codon == "uaa" || codon == "uag" || codon == "uga") { proteina += "-"; }
				}
			}
			msg.payload.sequence = proteina;
            node.send(msg);
        });
    }
    RED.nodes.registerType("translation",TranslationNode);
}
