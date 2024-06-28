from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

app=QApplication([])

window=QWidget()

window.setWindowIcon(QIcon('15727928.png'))
window.setStyleSheet('background-color: #000000;')
window.resize(500,500)
window.move(100,150)
window.setWindowTitle('Перша програма')




window.show()

app.exec_()

