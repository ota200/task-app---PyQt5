import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class Main(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("wjhg")

		self.setLayout(qtw.QVBoxLayout())
		
		label = qtw.QLabel("hi")
		label.setFont(qtg.QFont('pixel',50))
		self.layout().addWidget(label)

		entry = qtw.QLineEdit("hi test")
		entry.setObjectName("hi")
		self.layout().addWidget(entry)


		self.show()

app = qtw.QApplication([])
mw = Main()

app.exec_()