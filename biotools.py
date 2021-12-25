def preprocessing(cadena):  # Elimina cualquier caracter que no sea nucleotido o aminoacido
    cadenaLimpia = ''.join([letra for letra in cadena.lower() if letra in ['d', 'e', 'a', 'r', 'n', 'c', 'f', 'g', 'q',
                                                                           'h', 'i', 'l', 'k', 'm', 'p', 's', 'y', 't',
                                                                           'w', 'v', 'u', '-']])
    return cadenaLimpia


def readstring(file):  # Lee una potencial cadena de nucleotidos de un archivo de texto plano y lo limpia
    f = open(file, "r")
    cadena = f.read().strip()
    f.close()
    return preprocessing(cadena)


def readstringRAW(file):  # Lee una potencial cadena de nucleotidos de un archivo de texto plano
    f = open(file, "r")
    cadena = f.read().strip()
    f.close()
    return cadena


def getsegment(inicio, final, cadena):  # Retorna un segmento de la cadena original
    return cadena[inicio - 1:final]


def detecttype(cadena): # Nos indica si la cadena es de ARN, ADN, proteina o desconocido
    type_of_data = "unknown"
    NOTadn = [letra for letra in cadena.lower() if letra not in ['a', 'c', 'g', 't']]
    NOTarn = [letra for letra in cadena.lower() if letra not in ['a', 'c', 'g', 'u']]
    NOTaa = [letra for letra in cadena.lower() if letra not in ['d', 'e', 'a', 'r', 'n', 'c', 'f', 'g', 'q', 'h',
                                                                'i', 'l', 'k', 'm', 'p', 's', 'y', 't', 'w', 'v',
                                                                '-']]
    if len(NOTadn) == 0:
        type_of_data = "adn"
    if len(NOTarn) == 0:
        type_of_data = "arn"
    if len(NOTaa) == 0 and len(NOTadn) > 0:
        # Normalmente los AA normalmente van en mayusculas, en cadenas cortas se puede
        # confundir con adn si esta en minusculas.
        type_of_data = "protein"
    return type_of_data


def nucleotidscount(cadena):  # Nos devuelve la cantidad de cada tipo de nucleotido de una cadena
    a, c, g, t, u = 0, 0, 0, 0, 0
    for n in cadena:
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


def complement(cadena):  # Nos devuelve la cadena complementaria, tanto para ARN como para ADN
    cc = ""
    type_of_data = detecttype(cadena)
    if type_of_data == "adn" or type_of_data == "arn":
        for n in cadena.lower():
            if n == "a":
                if type_of_data == "adn":
                    cc += "t"
                else:
                    cc += "u"
            if n == "c":
                cc += "g"
            if n == "g":
                cc += "c"
            if n == "t":
                cc += "a"
            if n == "u":
                cc += "a"
            if n == " ":
                cc += " "
    return cc


def reverse(cadena):  # Nos retorna la cadena inversa
    return cadena[::-1]


def length(cadena):  # Nos retorna el numero de bases (longitud)
    return len(cadena)


def transcription(cadena):  # Nos retorna la cadena transcrita
    return cadena.lower().replace('t', 'u')


def translation(cadena):  # Nos retorna los aminoacidos de una cadena (traducción)
    proteina = ""
    if len(cadena) % 3 == 0:  # solo se realiza la traducción si los codones estan enteros
        cadena = transcription(cadena)  # realizamos la transcripción
        while len(cadena) >= 3:
            codon = cadena[0] + cadena[1] + cadena[2]
            cadena = cadena[3:]
            codon = codon.lower()
            if codon == "gac" or codon == "gau":
                proteina += "D"
            if codon == "gaa" or codon == "gag":
                proteina += "E"
            if codon == "gca" or codon == "gcc" or codon == "gcg" or codon == "gcu":
                proteina += "A"
            if codon == "aga" or codon == "agg" or codon == "cga" or codon == "cgc" or codon == "cgg" or codon == "cgu":
                proteina += "R"
            if codon == "aac" or codon == "aau":
                proteina += "N"
            if codon == "ugc" or codon == "ugu":
                proteina += "C"
            if codon == "uuc" or codon == "uuu":
                proteina += "F"
            if codon == "gca" or codon == "ggc" or codon == "ggg" or codon == "ggu":
                proteina += "G"
            if codon == "caa" or codon == "cag":
                proteina += "Q"
            if codon == "cac" or codon == "cau":
                proteina += "H"
            if codon == "aua" or codon == "auc" or codon == "auu":
                proteina += "I"
            if codon == "uua" or codon == "uug" or codon == "cua" or codon == "cuc" or codon == "cug" or codon == "cuu":
                proteina += "L"
            if codon == "aaa" or codon == "aag":
                proteina += "K"
            if codon == "aug":
                proteina += "M"
            if codon == "cca" or codon == "ccc" or codon == "ccg" or codon == "ccu":
                proteina += "P"
            if codon == "agc" or codon == "agu" or codon == "uca" or codon == "ucc" or codon == "ucg" or codon == "ucu":
                proteina += "S"
            if codon == "uac" or codon == "uau":
                proteina += "Y"
            if codon == "aca" or codon == "acc" or codon == "acg" or codon == "acu":
                proteina += "T"
            if codon == "ugg":
                proteina += "W"
            if codon == "gua" or codon == "guc" or codon == "gug" or codon == "guu":
                proteina += "V"
            if codon == "uaa" or codon == "uag" or codon == "uga":
                proteina += "-"  # stop
    return proteina
