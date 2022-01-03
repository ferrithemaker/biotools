import biotools as bt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QAction
import sys
from ui_biotools import Ui_MainWindow
from ui_biotools_about import Ui_Frame


class BioToolsAbout(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.setWindowTitle("About")


class BioToolsMainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Python Biotools UI")

        # initial setup
        self.ui.a_count.setText('0')
        self.ui.c_count.setText('0')
        self.ui.g_count.setText('0')
        self.ui.t_count.setText('0')
        self.ui.u_count.setText('0')
        self.ui.count_length.setText('0')
        self.ui.autodetection_label.setText('UNKNOWN')

        # create sequence object
        self.sequence = bt.Sequence()

        # add actions to buttons
        self.ui.preprocessingButton.clicked.connect(self.preprocessingAction)
        self.ui.autodetectionButton.clicked.connect(self.autodetectionAction)
        self.ui.reverseButton.clicked.connect(self.reverseAction)
        self.ui.complementButton.clicked.connect(self.complementAction)
        self.ui.revCompButton.clicked.connect(self.revCompAction)
        self.ui.transcriptionButton.clicked.connect(self.transcriptionAction)
        self.ui.translationButton.clicked.connect(self.translationAction)
        self.ui.countButton.clicked.connect(self.countAction)
        self.ui.copy2inputButton.clicked.connect(self.copy2inputAction)

        # add menu actions

        # exit action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exitApp)
        self.ui.menu.addAction(exit_action)

        # about action
        about_action = QAction("About", self)
        about_action.triggered.connect(self.openAbout)
        self.ui.menu.addAction(about_action)

    def exitApp(self):
        QApplication.quit()

    def openAbout(self):
        self.aboutWidget = BioToolsAbout(self)
        self.aboutWidget.show()

    def copy2inputAction(self):
        if self.ui.output_sequence.toPlainText() != "":
            self.ui.input_sequence.setText(self.ui.output_sequence.toPlainText())
            self.ui.output_sequence.setText("")

    def preprocessingAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        self.sequence.preprocessing()
        self.ui.output_sequence.setText(self.sequence.seq)

    def autodetectionAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        detectedType = self.sequence.detecttype()
        self.ui.autodetection_label.setText(detectedType)

    def reverseAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        self.sequence.reverse()
        self.ui.output_sequence.setText(self.sequence.seq)

    def complementAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        self.sequence.complement()
        self.ui.output_sequence.setText(self.sequence.seq)

    def revCompAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        self.sequence.complement()
        self.sequence.reverse()
        self.ui.output_sequence.setText(self.sequence.seq)

    def transcriptionAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        self.sequence.transcription()
        self.ui.output_sequence.setText(self.sequence.seq)

    def translationAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        self.sequence.translation()
        if self.sequence.seq == "":
            self.ui.output_sequence.setText("The input sequence must "
                                            "be a sequence of ADN / ARN "
                                            "without partial codons")
        else:
            self.ui.output_sequence.setText(self.sequence.seq)

    def countAction(self):
        self.sequence.seq = self.ui.input_sequence.toPlainText()
        length = self.sequence.length()
        nc = self.sequence.nucleotidscount()
        self.ui.count_length.setText(str(length))
        self.ui.a_count.setText(str(nc["a"]))
        self.ui.c_count.setText(str(nc["c"]))
        self.ui.g_count.setText(str(nc["g"]))
        self.ui.t_count.setText(str(nc["t"]))
        self.ui.u_count.setText(str(nc["u"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BioToolsMainWindow()
    window.show()

    sys.exit(app.exec())
