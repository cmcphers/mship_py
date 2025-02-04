from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget)
from classes import (MSClassBlock, MSClass)
from equipment import MSEquipmentBlock
from stats import (MSStatBlock, MSSaveBlock, MSStat)
from skills import (MSSkill, MSSkillBlock)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Lay everything out.
        w = QWidget()
        self._v_main = QVBoxLayout()
        g_top = QGridLayout()
        lbl_charName = QLabel("Character Name:")
        lbl_playerName = QLabel("Player Name:")
        lbl_pronouns = QLabel("Pronouns:")
        edit_charName = QLineEdit()
        edit_playerName = QLineEdit()
        edit_pronouns = QLineEdit()
        self._btn_generate = QPushButton("Generate")
        self._btn_generate.clicked.connect(self._onGenerateClicked)
        g_top.addWidget(lbl_charName, 0, 0)
        g_top.addWidget(lbl_playerName, 0, 1)
        g_top.addWidget(lbl_pronouns, 0, 2)
        g_top.addWidget(edit_charName, 1, 0)
        g_top.addWidget(edit_playerName, 1, 1)
        g_top.addWidget(edit_pronouns, 1, 2)
        g_top.addWidget(self._btn_generate, 1, 3)

        self._h_statSave = QHBoxLayout()
        self._statBlock = MSStatBlock()
        self._saveBlock = MSSaveBlock()
        self._h_statSave.addWidget(self._statBlock)
        self._h_statSave.addWidget(self._saveBlock)

        self._classBlock = MSClassBlock()
        self._classBlock.classChanged.connect(self._onClassChanged)

        self._skillBlock = MSSkillBlock()

        self._equipmentBlock = MSEquipmentBlock()

        self._v_main.addLayout(g_top)
        self._v_main.addLayout(self._h_statSave)
        self._v_main.addWidget(self._classBlock)
        self._v_main.addWidget(self._skillBlock)
        self._v_main.addWidget(self._equipmentBlock)
        w.setLayout(self._v_main)
        self.setCentralWidget(w)
        self.setWindowTitle("Mothership Character Generator")

    @pyqtSlot()
    def _onGenerateClicked(self):
        pass

    @pyqtSlot()
    def _onClassChanged(self, cl: MSClass, st: MSStat):
        self._equipmentBlock.updateClass(cl)
        self._statBlock.updateClass(cl, st)
        self._saveBlock.updateClass(cl)
        self._skillBlock.updateClass(cl)

    @pyqtSlot()
    def _onModStatChanged(self, cl: MSClass, st: MSStat):
        self._statBlock.updateClass(cl, st)
