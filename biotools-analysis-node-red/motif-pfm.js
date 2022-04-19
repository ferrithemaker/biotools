module.exports = function(RED) {
	function compute_pwm_score(pwm, S,offset) {
		var score=0.0;
		var pwm_ncol = pwm[0].length;
        score = 0.00;
        for (var x = 0; x < pwm_ncol; x++) {
			var y = -1;
            switch(S.charAt(offset+x)) {
				case 'a':case 'A': y=0; break;
				case 'c':case 'C': y=1; break;
				case 't':case 'T': y=2; break;
				case 'g':case 'G': y=3; break;
			}
			if (y == -1) continue;
			score += pwm[y][x];
        }
	return score;
	}

	function match_PWM_XString(pwm,S,minscore) {
		var ncols= pwm[0].length;
		for (var n1 = 0; n1+ncols<=S.length;++n1) {
			var score = compute_pwm_score(pwm,S,n1);
				if (score >= minscore) {
					return score;
				}
		}
		return null;
	}


	/* search pwm in dna */
	function scanPwm(matrix,dna,score) {
		var score=match_PWM_XString(matrix,dna,score);
	}

	/* convert a matrix to string */
	function matrixToString(matrix) {
		var s="";
		var bases=["A","C","G","T"];
		var i=0,j;
		for(i=0;i< 4;++i) {
			var total=0;
			s+=bases[i];
			for(j=0;j< matrix[i].length;++j) {
				s+=" "+matrix[i][j];
				total+=matrix[i][j];
			}
			//s+=" ("+total+")";
			s+="\n";
		}
		return s;
	}
	
    function motifpfmNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        let flowContext = this.context().flow;
        node.on('input', function(msg) {
			var hammingValue = 0;
			var seq1_id = flowContext.get("data1_id_motif") || null;
			var seq2_id = flowContext.get("data2_id_motif") || null;
			var idvalue = msg.payload.id;
			if (flowContext.get("data1_id_motif") != null && flowContext.get("data2_id_motif") == null &&
				idvalue != flowContext.get("data1_id_motif") ) {
				flowContext.set("data2_id_motif",idvalue);
				if (msg.payload.sequence != null) {
					flowContext.set("data_sequence",msg.payload.sequence);
				}
				if (msg.payload.PFMArray != null) {
					flowContext.set("data_pfm",msg.payload.PFMArray);
				}
			}
			if (flowContext.get("data1_id_motif") == null) {
				flowContext.set("data1_id_motif",idvalue);
				if (msg.payload.sequence != null) {
					flowContext.set("data_sequence",msg.payload.sequence);
				}
				if (msg.payload.PFMArray != null) {
					flowContext.set("data_pfm",msg.payload.PFMArray);
				}
			}
			if (flowContext.get("data1_id_motif") != null && flowContext.get("data2_id_motif") != null &&
				flowContext.get("data1_id_motif") != flowContext.get("data2_id_motif")) {
				var data_pfm = flowContext.get("data_pfm");
				var data_sequence = flowContext.get("data_sequence").toLowerCase();
				flowContext.set("data1_id_motif",null);
				flowContext.set("data2_id_motif",null);
				flowContext.set("data_pfm",null);
				flowContext.set("data_sequence",null);
				var pfm = data_pfm;
				var ncols = pfm[0].length;
				var pwm = [
					new Array(ncols),
					new Array(ncols),
					new Array(ncols),
					new Array(ncols)
				];

				/* convert pfm to pwm */
				for(var x = 0;x < ncols; ++x) {
					var total = 0;
					for(var y = 0;y < 4; ++y) total += pfm[y][x];
					for(var y = 0;y <4 ; ++y) {
						var prob_base = 0.25;
						var freq = pfm[y][x];
						var w = Math.log2 ( ( freq + Math.sqrt(total) * prob_base ) / ( total + Math.sqrt(total) ) / prob_base );
						pwm[y][x] = w;
					}
				}
				var min_score = parseFloat(config.minscore);
				var output_score = match_PWM_XString(pwm,data_sequence.toUpperCase(),min_score);
				msg.payload = {"sequence":data_sequence,"PFMArray":data_pfm,"score":output_score};
				node.send(msg);
			}      
        });
    }
    RED.nodes.registerType("motif pfm score",motifpfmNode);
}
