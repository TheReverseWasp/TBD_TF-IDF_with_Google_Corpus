
from helpers import *

app = QApplication(sys.argv)

class Interfaz(QDialog):
    #inicializados valores de botones e interfaz
    def __init__(self):
        self.carta_trampa = 0
        super(Interfaz, self).__init__()
        loadUi("Interfaz.ui", self)
        self.setWindowTitle("Buscador de palabras")
        self.btnProcessBool.clicked.connect(self.on_btnProcessBool_clicked)
        self.btnProcessDistance.clicked.connect(self.on_btnProcessDistance_clicked)
    @pyqtSlot()
    def on_btnProcessBool_clicked(self):
        self.carta_trampa += 1
        if self.carta_trampa % 2 == 1:
            return
        print("lol")
        self.tblResults.setRowCount(0)
        start = time.time()
        print(self.txtWord.toPlainText())
        full_rows = get_rows_bool(self.txtWord.toPlainText(), self.lblAlert, app)
        end = time.time()
        print("tiempo: " + str(end - start))
        #En caso de fallar se produce una alerta
        if full_rows == False:
            self.lblAlert.setText("Resultado: Error al procesar")
            return
        else:
            self.lblAlert.setText("Resultado: Completado en " + str(end - start))
        for i in range(len(full_rows)):
            self.tblResults.insertRow(i)
            self.tblResults.setItem(i,0, QTableWidgetItem(full_rows[i][0]))
            self.tblResults.setItem(i,1, QTableWidgetItem(str(full_rows[i][1])))
        app.processEvents()

    def on_btnProcessDistance_clicked(self):
        self.carta_trampa += 1
        if self.carta_trampa % 2 == 1:
            return
        self.tblResults.setRowCount(0)
        start = time.time()
        full_rows = get_rows_distance(self.txtWord.toPlainText(), self.lblAlert, app)
        end = time.time()
        print("tiempo: " + str(end - start))
        #En caso de fallar se produce una alerta
        if full_rows == False:
            self.lblAlert.setText("Resultado: Error al procesar")
            return
        else:
            self.lblAlert.setText("Resultado: Completado en " + str(end - start))
        for i in range(len(full_rows)):
            self.tblResults.insertRow(i)
            self.tblResults.setItem(i,0, QTableWidgetItem(full_rows[i][0]))
            self.tblResults.setItem(i,1, QTableWidgetItem(str(full_rows[i][1])))
        app.processEvents()

Widget = Interfaz()
Widget.show()
sys.exit(app.exec_())
