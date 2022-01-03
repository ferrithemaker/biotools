class Sequence:
    def __init__(self, seq=None):
        if seq is None:
            self.seq = ""
        else:
            self.seq = seq

    # Lee una potencial seq de nucleotidos de un archivo
    # de texto plano y lo limpia
    def readstring(self, file):
        f = open(file, "r")
        self.seq = f.read().strip()
        self.preprocessing()
        f.close()

    # Lee una potencial seq de nucleotidos de un archivo de texto plano
    def readstringRAW(self, file):
        f = open(file, "r")
        self.seq = f.read().strip()
        f.close()

    # Elimina cualquier caracter que no sea nucleotido o aminoacido
    def preprocessing(self):
        self.seq = ''.join([letra for letra in self.seq.lower()
                            if letra in ['d', 'e', 'a', 'r', 'n',
                                         'c', 'f', 'g', 'q', 'h',
                                         'i', 'l', 'k', 'm', 'p',
                                         's', 'y', 't', 'w', 'v',
                                         'u', '-']])

    # Nos devuelve un segmento de la seq original
    def getsegment(self, inicio, final):
        return self.seq[inicio - 1:final]

    # Nos indica si la seq es de ARN, ADN, proteina o desconocido
    def detecttype(self):
        type_of_data = "UNKNOWN"
        NOTadn = [letra for letra in self.seq.lower()
                  if letra not in ['a', 'c', 'g', 't']]
        NOTarn = [letra for letra in self.seq.lower()
                  if letra not in ['a', 'c', 'g', 'u']]
        NOTaa = [letra for letra in self.seq.lower()
                 if letra not in ['d', 'e', 'a', 'r', 'n', 'c', 'f', 'g',
                                  'q', 'h', 'i', 'l', 'k', 'm', 'p', 's',
                                  'y', 't', 'w', 'v', '-']]

        if len(NOTadn) == 0 and len(NOTarn) > 0 and len(NOTaa) > 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "ADN"
        if len(NOTarn) == 0 and len(NOTadn) > 0 and len(NOTaa) > 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "ARN"
        if len(NOTaa) == 0 and len(NOTadn) > 0 and len(NOTarn) > 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "PROTEIN"
        if len(NOTadn) == 0 and len(NOTarn) == 0 and len(NOTaa) > 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "ADN / ARN"
        if len(NOTadn) == 0 and len(NOTarn) == 0 and len(NOTaa) == 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "ADN / ARN / PROT."
        if len(NOTadn) == 0 and len(NOTarn) > 0 and len(NOTaa) == 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "ADN / PROTEIN"
        if len(NOTadn) > 0 and len(NOTarn) == 0 and len(NOTaa) == 0 \
                and not self.seq.isspace() and len(self.seq) > 0:
            type_of_data = "ARN / PROTEIN"
        return type_of_data

    # Nos devuelve la cantidad de cada tipo de nucleotido de una seq
    def nucleotidscount(self):
        a, c, g, t, u = 0, 0, 0, 0, 0
        for n in self.seq:
            if n.lower() == 'a':
                a += 1
            if n.lower() == 'c':
                c += 1
            if n.lower() == 't':
                t += 1
            if n.lower() == 'g':
                g += 1
            if n.lower() == 'u':
                u += 1
        return {"a": a, "c": c, "g": g, "t": t, "u": u}

    # Nos devuelve la seq complementaria, tanto para ARN como para ADN
    def complement(self):
        cc = ""
        type_of_data = self.detecttype()
        if "ADN" in type_of_data or "ARN" in type_of_data:
            for n in self.seq.lower():
                if n == "a":
                    if "ADN" in type_of_data:
                        cc += "t"
                    else:
                        cc += "u"
                if n == "c":
                    cc += "g"
                if n == "g":
                    cc += "c"
                if n == "t" or n == "u":
                    cc += "a"
                if n == " ":
                    cc += " "
        self.seq = cc

    # Nos devuelve la seq inversa
    def reverse(self):
        self.seq = self.seq[::-1]

    # Nos devuelve el numero de bases (longitud)
    def length(self):
        return len(self.seq)

    # Nos devuelve la seq transcrita
    def transcription(self):
        self.seq = self.seq.lower().replace('t', 'u')

    # Nos devuelve los aminoacidos de una seq (traducción)
    def translation(self):
        proteina = ""
        print(len(self.seq))
        print(self.seq)
        # solo se realiza la traducción si los codones estan enteros
        if len(self.seq) % 3 == 0:
            # realizamos la transcripción
            self.transcription()
            while len(self.seq) >= 3:
                codon = self.seq[0] + self.seq[1] + self.seq[2]
                self.seq = self.seq[3:]
                codon = codon.lower()
                if codon == "gac" or codon == "gau":
                    proteina += "D"
                if codon == "gaa" or codon == "gag":
                    proteina += "E"
                if codon == "gca" or codon == "gcc" \
                        or codon == "gcg" or codon == "gcu":
                    proteina += "A"
                if codon == "aga" or codon == "agg" or codon == "cga" \
                        or codon == "cgc" or codon == "cgg" or codon == "cgu":
                    proteina += "R"
                if codon == "aac" or codon == "aau":
                    proteina += "N"
                if codon == "ugc" or codon == "ugu":
                    proteina += "C"
                if codon == "uuc" or codon == "uuu":
                    proteina += "F"
                if codon == "gca" or codon == "ggc" \
                        or codon == "ggg" or codon == "ggu":
                    proteina += "G"
                if codon == "caa" or codon == "cag":
                    proteina += "Q"
                if codon == "cac" or codon == "cau":
                    proteina += "H"
                if codon == "aua" or codon == "auc" or codon == "auu":
                    proteina += "I"
                if codon == "uua" or codon == "uug" or codon == "cua" \
                        or codon == "cuc" or codon == "cug" or codon == "cuu":
                    proteina += "L"
                if codon == "aaa" or codon == "aag":
                    proteina += "K"
                if codon == "aug":
                    proteina += "M"
                if codon == "cca" or codon == "ccc" or codon == "ccg" \
                        or codon == "ccu":
                    proteina += "P"
                if codon == "agc" or codon == "agu" or codon == "uca" \
                        or codon == "ucc" or codon == "ucg" or codon == "ucu":
                    proteina += "S"
                if codon == "uac" or codon == "uau":
                    proteina += "Y"
                if codon == "aca" or codon == "acc" \
                        or codon == "acg" or codon == "acu":
                    proteina += "T"
                if codon == "ugg":
                    proteina += "W"
                if codon == "gua" or codon == "guc" \
                        or codon == "gug" or codon == "guu":
                    proteina += "V"
                if codon == "uaa" or codon == "uag" or codon == "uga":
                    proteina += "-"  # stop
        self.seq = proteina
