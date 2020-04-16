from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import time

app = QtWidgets.QApplication([])
dlg = uic.loadUi("gauges.ui")

#get ODB2 data and populate gauges
dlg.lcdSpeed.display(55)
dlg.lcdRPM.display(2000)
dlg.lcdGear.display(3)
dlg.lcdCoolantTemp.display(222)
dlg.lcdAirTemp.display(110)
dlg.lcdVoltage.display(14.2)
dlg.gaugeLoad.setValue(30)
dlg.gaugeThrottle.setValue(10)

time.sleep(5) #sleep 5 seconds

#add message box
def show_msg(title="Test", message="test"):
	QMessageBox.information(None,title,message)

# need Get DTC method to fill listWidget

#dlg.buttonGetDTCs.clicked.connect(getDTCs)

dlg.show()
app.exec()