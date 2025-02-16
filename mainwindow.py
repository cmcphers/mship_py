from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget)
from classes import (MSClassBlock, MSClass, NUM_CLASSES, HEALTH_BASE)
from equipment import MSEquipmentBlock
from stats import (MSStatBlock, MSSaveBlock, MSStat, STAT_BASE, SAVE_BASE, NUM_STATS)
from skills import (MSSkill, MSSkillBlock)
from random import randint

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
        # Check each block to see if it should be randomized.
        if not self._statBlock.isChecked():
            # Generate random stats.
            self._statBlock.setStr(STAT_BASE + d10(2))
            self._statBlock.setSpeed(STAT_BASE + d10(2))
            self._statBlock.setInt(STAT_BASE + d10(2))
            self._statBlock.setCombat(STAT_BASE + d10(2))
        if not self._saveBlock.isChecked():
            # Generate random saves.
            self._saveBlock.setSanity(SAVE_BASE + d10(2))
            self._saveBlock.setFear(SAVE_BASE + d10(2))
            self._saveBlock.setBody(SAVE_BASE + d10(2))
        if not self._classBlock.isChecked():
            # Generate random class
            self._classBlock.setClass(MSClass(randint(1,NUM_CLASSES-1)))
            # Set the modified stat
            self._classBlock.setModStat(MSStat(randint(0, NUM_STATS-1)))
            # Generate random health
            self._classBlock.setHealth(HEALTH_BASE + d10(1))
        if not self._skillBlock.isChecked():
            # Generate random skills.
            self._skillBlock.setChecked(True)
            if self._skillBlock.getSkill1Enabled():
                self._skillBlock.setSkill1(randint(1, self._skillBlock.getSkill1Range()-1))
            if self._skillBlock.getSkill2Enabled():
                self._skillBlock.setSkill2(randint(1, self._skillBlock.getSkill2Range()-1))
            if self._skillBlock.getSkill3Enabled():
                self._skillBlock.setSkill3(randint(1, self._skillBlock.getSkill3Range()-1))
            if self._skillBlock.getSkill4Enabled():
                self._skillBlock.setSkill4(randint(1, self._skillBlock.getSkill4Range()-1))
            if self._skillBlock.getSkill5Enabled():
                self._skillBlock.setSkill5(randint(1, self._skillBlock.getSkill5Range()-1))
            self._skillBlock.setChecked(False)
        if not self._equipmentBlock.isChecked():
            # Generate random equipment
            self._equipmentBlock.setLoadout(randint(1, self._equipmentBlock.getNumLoadouts()-1))
            self._equipmentBlock.setTrinket(randint(1, self._equipmentBlock.getNumTrinkets()-1))
            self._equipmentBlock.setPatch(randint(1, self._equipmentBlock.getNumPatches()-1))
            # Generate money
            self._equipmentBlock.setCredits(10*d10(2))

    @pyqtSlot(MSClass, MSStat)
    def _onClassChanged(self, cl: MSClass, st: MSStat):
        self._equipmentBlock.updateClass(cl)
        self._statBlock.updateClass(cl, st)
        self._saveBlock.updateClass(cl)
        self._skillBlock.updateClass(cl)

    @pyqtSlot()
    def _onModStatChanged(self, cl: MSClass, st: MSStat):
        self._statBlock.updateClass(cl, st)

def d10(n: int):
    a = 0
    if n > 0:
        for i in range(n):
            a += randint(1,10)
    return a