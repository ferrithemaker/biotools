import biotools as bt
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from ui_biotools import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initial setup
        self.ui.a_count.setText('0')
        self.ui.c_count.setText('0')
        self.ui.g_count.setText('0')
        self.ui.t_count.setText('0')
        self.ui.u_count.setText('0')
        self.ui.count_length.setText('0')
        self.ui.autodetection_label.setText('unknown')

        # add actions to buttons
        self.ui.preprocessingButton.clicked.connect(self.preprocessingAction)
        self.ui.autodetectionButton.clicked.connect(self.autodetectionAction)
        self.ui.reverseButton.clicked.connect(self.reverseAction)
        self.ui.complementButton.clicked.connect(self.complementAction)
        self.ui.RCButton.clicked.connect(self.RCAction)
        self.ui.transcriptionButton.clicked.connect(self.transcriptionAction)
        self.ui.translationButton.clicked.connect(self.translationAction)
        self.ui.countButton.clicked.connect(self.countAction)

    def preprocessingAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        outputText = bt.preprocessing(inputText)
        self.ui.output_sequence.setText(outputText)

    def autodetectionAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        detectedType = bt.detecttype(inputText)
        self.ui.autodetection_label.setText(detectedType)

    def reverseAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        outputText = bt.reverse(inputText)
        self.ui.output_sequence.setText(outputText)

    def complementAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        outputText = bt.complement(inputText)
        self.ui.output_sequence.setText(outputText)

    def RCAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        outputText = bt.complement(bt.reverse(inputText))
        self.ui.output_sequence.setText(outputText)

    def transcriptionAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        outputText = bt.transcription(inputText)
        self.ui.output_sequence.setText(outputText)

    def translationAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        outputText = bt.translation(inputText)
        self.ui.output_sequence.setText(outputText)

    def countAction(self):
        inputText = self.ui.input_sequence.toPlainText()
        length = bt.length(inputText)
        nc = bt.nucleotidscount(inputText)
        self.ui.count_length.setText(str(length))
        self.ui.a_count.setText(str(nc["a"]))
        self.ui.c_count.setText(str(nc["c"]))
        self.ui.g_count.setText(str(nc["g"]))
        self.ui.t_count.setText(str(nc["t"]))
        self.ui.u_count.setText(str(nc["u"]))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())