import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.tree = QTreeWidget()
        self.item1 = QTreeWidgetItem()			        # 1
        self.item2 = QTreeWidgetItem()
        self.item3 = QTreeWidgetItem()
        self.item1.setText(0, '第1章')
        self.item2.setText(0, '第1节')
        self.item3.setText(0, '第1段')
        self.item1.setCheckState(0, Qt.Unchecked)		# 2
        self.item2.setCheckState(0, Qt.Unchecked)
        self.item3.setCheckState(0, Qt.Unchecked)
        self.item1.addChild(self.item2)			        # 3
        self.item2.addChild(self.item3)

        self.tree.addTopLevelItem(self.item1)
        self.tree.setHeaderLabel('PyQt教程')
        self.tree.clicked.connect(self.click_slot)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.tree)
        self.setLayout(h_layout)

    def click_slot(self):					            # 4
        item = self.tree.currentItem()
        print(item.text(0))

        if item == self.item1:
            if self.item1.checkState(0) == Qt.Checked:
                self.item2.setCheckState(0, Qt.Checked)
                self.item3.setCheckState(0, Qt.Checked)
            else:
                self.item2.setCheckState(0, Qt.Unchecked)
                self.item3.setCheckState(0, Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())