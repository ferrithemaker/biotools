module.exports = function(RED) {
    function jasparProcessingNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
			var info;
			var a_array;
			var c_array;
			var g_array;
			var t_array;
			var a_values = [];
			var c_values = [];
			var g_values = [];
			var t_values = [];
			var pfm = [];
			lines = msg.payload.split("\n");
			for (var i = 0; i < lines.length; i++) {
				if (lines[i][0] == '>') {
					info = lines[i].replace('>','').replace('\t',' ');
				}
				if (lines[i][0] == 'A') {
					a_array = lines[i].replace('[','').replace(']','').replace('A','').split(' ');
					for (var a_pos = 0; a_pos < a_array.length; a_pos++) {
						if (a_array[a_pos] != "") {
							a_values.push(a_array[a_pos]);
						}
					}
					pfm.push(a_values);
				}
				if (lines[i][0] == 'C') {
					c_array = lines[i].replace('[','').replace(']','').replace('C','').split(' ');
					for (var c_pos = 0; c_pos < c_array.length; c_pos++) {
						if (c_array[c_pos] != "") {
							c_values.push(c_array[c_pos]);
						}
					}
					pfm.push(c_values);
				}
				if (lines[i][0] == 'G') {
					g_array = lines[i].replace('[','').replace(']','').replace('G','').split(' ');
					for (var g_pos = 0; g_pos < g_array.length; g_pos++) {
						if (g_array[g_pos] != "") {
							g_values.push(g_array[g_pos]);
						}
					}
					pfm.push(g_values);
				}
				if (lines[i][0] == 'T') {
					t_array = lines[i].replace('[','').replace(']','').replace('T','').split(' ');
					for (var t_pos = 0; t_pos < t_array.length; t_pos++) {
						if (t_array[t_pos] != "") {
							t_values.push(t_array[t_pos]);
						}
					}
					pfm.push(t_values);
				}
				
			}
			msg.payload = { "information": info,"PFMArray": pfm}
            node.send(msg);
        });
    }
    RED.nodes.registerType("processing JASPAR file",jasparProcessingNode);
}
