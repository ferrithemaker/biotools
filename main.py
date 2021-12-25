import biotools as bt
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from ui_biotools import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    
'''
cadena = bt.readstring("bases")

#print(cadena)
cadenaNeta = bt.preprocessing(cadena)
print(cadenaNeta)
print(bt.nucleotidscount(cadenaNeta))

exon1 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(5639,5710,cadenaNeta))))
exon2 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(2257,2530,cadenaNeta))))
exon3 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(1528,2182,cadenaNeta))))
exon4 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(1151,1466,cadenaNeta))))
exon5 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(816,947,cadenaNeta))))
exon6 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(131,745,cadenaNeta))))

exon1 = bt.reverse(bt.complement(bt.getsegment(5639,5710,cadenaNeta)))
exon2 = bt.reverse(bt.complement(bt.getsegment(2257,2530,cadenaNeta)))
exon3 = bt.reverse(bt.complement(bt.getsegment(1528,2182,cadenaNeta)))
exon4 = bt.reverse(bt.complement(bt.getsegment(1151,1466,cadenaNeta)))
exon5 = bt.reverse(bt.complement(bt.getsegment(816,947,cadenaNeta)))
exon6 = bt.reverse(bt.complement(bt.getsegment(131,745,cadenaNeta)))

ii12 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(5637,5638,cadenaNeta))))
fi12 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(2531,2532,cadenaNeta))))
ii23 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(2255,2256,cadenaNeta))))
fi23 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(2183,2184,cadenaNeta))))
ii34 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(1526,1527,cadenaNeta))))
fi34 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(1467,1468,cadenaNeta))))
ii45 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(1149,1150,cadenaNeta))))
fi45 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(948,949,cadenaNeta))))
ii56 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(814,815,cadenaNeta))))
fi56 = bt.transcription(bt.reverse(bt.complement(bt.getsegment(746,747,cadenaNeta))))

#print(ii12,"-",fi12)
#print(ii23,"-",fi23)
#print(ii34,"-",fi34)
#print(ii45,"-",fi45)
#print(ii56,"-",fi56)

#print(len(exon1)+len(exon2)+len(exon3)+len(exon4)+len(exon5)+len(exon6))

#print(exon1+exon2+exon3+exon4+exon5+exon6)

#print(len(exon1))

#print(bt.transcription(exon6))

#print(bt.traduccion(bt.transcription(exon1)))

cadena = "acatgaaacaatcgttatttgtttatttggaatatccgtgactaggcgtagtcaatttgtttgttaggtacatggtcggtatatttaa aatgcttttggttagttaagtcccatttcgacttatatacatatatatatataggaagttcaagtgccagctc"

cadena2 = "ttc gga aac cag gtt gct ggc cac ctc taa gca ctt ttc cac gtc cac gtt gtg tga cat"
cadenaNeta = bt.preprocessing(cadena2)
print(bt.detecttype(cadena2))
print(cadenaNeta)

print(bt.reverse(bt.complement(cadenaNeta)))

print((bt.transcription(bt.reverse(bt.complement(cadenaNeta)))))
print((bt.translation(bt.transcription(bt.reverse(bt.complement(cadenaNeta))))))
'''