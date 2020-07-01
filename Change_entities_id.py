import sys
import pymongo as pm
from bson.objectid import ObjectId
from PyQt5 import QtWidgets as pqt
from PyQt5 import QtGui as qg
client = pm.MongoClient("mongodb://jarvis:#p1dormammusbargain@localhost:27017")
print("Connected to mongodb")
db = client.jarvis_db
col = db.entities

class App(pqt.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Change Entities _id")
		self.setWindowIcon(qg.QIcon("favicon.ico"))
		self.setGeometry(100, 100, 400, 250)
		self.text1 = pqt.QLineEdit(self)
		self.text2 = pqt.QLineEdit(self)
		self.button = pqt.QPushButton("Change id", self)
		self.text1.move(75, 50)
		self.text1.resize(250, 40)
		self.text2.move(75, 100)
		self.text2.resize(250, 40)
		self.button.move(150, 180)
		self.button.clicked.connect(self.change_func)
		self.show()

	def change_func(self):
		nid = int(self.text2.text())
		oid = self.text1.text()
		data = col.find_one({"_id": ObjectId(oid)})
		data["_id"] = nid
		if col.insert_one(data):
			print("New document with id %i inserted" % nid)
		if col.delete_one({"_id": ObjectId(oid)}):
			print("Old document with id %s deleted" % oid)

if __name__ == "__main__":
	app = pqt.QApplication(sys.argv)
	app.setStyle("Fusion")
	ex = App()
	sys.exit(app.exec_())