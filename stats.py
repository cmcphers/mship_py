from enum import IntEnum
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QSpinBox)
from classes import MSClass

# Constants
NUM_STATS = 4
STAT_MIN = 0
STAT_MAX = 65
SAVE_MIN = 0
SAVE_MAX = 90


class MSStat(IntEnum):
    STRENGTH = 0
    SPEED = 1
    INTELLECT = 2
    COMBAT = 3

Str = [0, 0, 0, 0, 5]
Speed = [0, 0, 0, 0, 5]
Intel = [0, 0, 20, 10, 5]
Combat = [0, 10, 0, 0, 5]
Sanity = [0, 0, 0, 30, 10]
Fear = [0, 20, 60, 0, 10]
Body = [0, 10, 0, 0, 10]
Mod = [0, 0, -10, 5, 0]

Names = ["Strength", "Speed", "Intellect", "Combat"]

ID = [MSStat.STRENGTH, MSStat.SPEED, MSStat.INTELLECT, MSStat.COMBAT]


# Stat block to hold character stats.
class MSStatBlock(QGroupBox):
    strChanged = pyqtSignal(int)
    speedChanged = pyqtSignal(int)
    intChanged = pyqtSignal(int)
    combatChanged = pyqtSignal(int)

    def __init__(self, parent):
        super(MSStatBlock, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)

        # Create all widgets
        g_main = QGridLayout()
        lbl_base = QLabel("Base")
        lbl_adj = QLabel("Adj.")
        lbl_str = QLabel("Strength")
        lbl_speed = QLabel("Speed")
        lbl_int = QLabel("Intellect")
        lbl_combat = QLabel("Combat")
        self._spin_str = QSpinBox()
        self._spin_str.valueChanged.connect(self.strChanged)
        self._spin_str.setMinimum(STAT_MIN)
        self._spin_str.setMaximum(STAT_MAX)
        self._spin_speed = QSpinBox()
        self._spin_speed.valueChanged.connect(self.speedChanged)
        self._spin_speed.setMinimum(STAT_MIN)
        self._spin_speed.setMaximum(STAT_MAX)
        self._spin_int = QSpinBox()
        self._spin_int.valueChanged.connect(self.intChanged)
        self._spin_int.setMinimum(STAT_MIN)
        self._spin_int.setMaximum(STAT_MAX)
        self._spin_combat = QSpinBox()
        self._spin_combat.valueChanged.connect(self.combatChanged)
        self._spin_combat.setMinimum(STAT_MIN)
        self._spin_combat.setMaximum(STAT_MAX)
        self._spin_adjStr = QSpinBox()
        self._spin_adjSpeed = QSpinBox()
        self._spin_adjInt = QSpinBox()
        self._spin_adjCombat = QSpinBox()

        # Disable adjusted spinboxes and remove their arrows.
        self._spin_adjStr.setEnabled(False)
        self._spin_adjStr.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self._spin_adjSpeed.setEnabled(False)
        self._spin_adjSpeed.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self._spin_adjInt.setEnabled(False)
        self._spin_adjInt.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self._spin_adjCombat.setEnabled(False)
        self._spin_adjCombat.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        # Lay everything out.
        g_main.addWidget(lbl_str, 0, 1)
        g_main.addWidget(lbl_speed, 0, 2)
        g_main.addWidget(lbl_int, 0, 3)
        g_main.addWidget(lbl_combat, 0, 4)
        g_main.addWidget(lbl_base, 1, 0)
        g_main.addWidget(self._spin_str, 1, 1)
        g_main.addWidget(self._spin_speed, 1, 2)
        g_main.addWidget(self._spin_int, 1, 3)
        g_main.addWidget(self._spin_combat, 1, 4)
        g_main.addWidget(lbl_adj, 2, 0)
        g_main.addWidget(self._spin_adjStr, 2, 1)
        g_main.addWidget(self._spin_adjSpeed, 2, 2)
        g_main.addWidget(self._spin_adjInt, 2, 3)
        g_main.addWidget(self._spin_combat, 2, 4)
        self.setLayout(g_main)

    def setStr(self, v: int, base: bool = False):
        if v > STAT_MAX or v < STAT_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_str.setValue(v)
        else:
            self._spin_adjStr.setValue(v)

    def getStr(self, base: bool = False) -> int:
        if base:
            return self._spin_str.value()
        else:
            return self._spin_adjStr.value()

    def setSpeed(self, v: int, base: bool = False):
        if v > STAT_MAX or v < STAT_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_speed.setValue(v)
        else:
            self._spin_adjSpeed.setValue(v)

    def getSpeed(self, base: bool = False) -> int:
        if base:
            return self._spin_speed.value()
        else:
            return self._spin_adjSpeed.value()

    def setInt(self, v: int, base: bool = False):
        if v > STAT_MAX or v < STAT_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_int.setValue(v)
        else:
            self._spin_adjInt.setValue(v)

    def getInt(self, base: bool = False) -> int:
        if base:
            return self._spin_int.value()
        else:
            return self._spin_adjInt.value()

    def setCombat(self, v: int, base: bool = False):
        if v > STAT_MAX or v < STAT_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_combat.setValue(v)
        else:
            self._spin_adjCombat.setValue(v)

    def getCombat(self, base: bool = False) -> int:
        if base:
            return self._spin_combat.value()
        else:
            return self._spin_adjCombat.value()

    def updateClass(self, cl: MSClass, modstat: MSStat):
        new_str = self._spin_str.value() + Str[cl]
        new_speed = self._spin_speed.value() + Speed[cl]
        new_int = self._spin_int.value() + Intel[cl]
        new_combat = self._spin_combat.value() + Combat[cl]

        if modstat == MSStat.STRENGTH:
            new_str += Mod[cl]
        elif modstat == MSStat.SPEED:
            new_speed += Mod[cl]
        elif modstat == MSStat.INTELLECT:
            new_int += Mod[cl]
        else:
            new_combat += Mod[cl]

        self._spin_adjStr.setValue(new_str)
        self._spin_adjSpeed.setValue(new_speed)
        self._spin_adjInt.setValue(new_int)
        self._spin_adjCombat.setValue(new_combat)

class MSSaveBlock(QGroupBox):
    sanityChanged = pyqtSignal(int)
    fearChanged = pyqtSignal(int)
    bodyChanged = pyqtSignal(int)

    def __init__(self, parent):
        super(MSSaveBlock, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)

        g_main = QGridLayout()
        # Create all widgets
        lbl_sanity = QLabel("Sanity")
        lbl_fear = QLabel("Fear")
        lbl_body = QLabel("Body")
        lbl_base = QLabel("Base")
        self._spin_sanity = QSpinBox()
        self._spin_sanity.setMinimum(SAVE_MIN)
        self._spin_sanity.setMaximum(SAVE_MAX)
        self._spin_sanity.valueChanged.connect(self.sanityChanged)
        self._spin_fear = QSpinBox()
        self._spin_fear.setMinimum(SAVE_MIN)
        self._spin_fear.setMaximum(SAVE_MAX)
        self._spin_fear.valueChanged.connect(self.fearChanged)
        self._spin_body = QSpinBox()
        self._spin_body.setMinimum(SAVE_MIN)
        self._spin_body.setMaximum(SAVE_MAX)
        self._spin_body.valueChanged.connect(self.bodyChanged)
        lbl_adj = QLabel("Adj")
        self._spin_adjSanity = QSpinBox()
        self._spin_adjSanity.setEnabled(False)
        self._spin_adjSanity.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self._spin_adjFear = QSpinBox()
        self._spin_adjFear.setEnabled(False)
        self._spin_adjFear.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self._spin_adjBody = QSpinBox()
        self._spin_adjBody.setEnabled(False)
        self._spin_adjBody.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        # Lay everything out
        g_main.addWidget(lbl_sanity, 0, 1)
        g_main.addWidget(lbl_fear, 0, 2)
        g_main.addWidget(lbl_body, 0, 3)
        g_main.addWidget(lbl_base, 1, 0)
        g_main.addWidget(self._spin_sanity, 1, 1)
        g_main.addWidget(self._spin_fear, 1, 2)
        g_main.addWidget(self._spin_body, 1, 3)
        g_main.addWidget(lbl_adj, 2, 0)
        g_main.addWidget(self._spin_adjSanity, 2, 1)
        g_main.addWidget(self._spin_adjFear, 2, 2)
        g_main.addWidget(self.sipn_adjBody, 2, 3)
        self.setLayout(g_main)

    def setSanity(self, v: int, base: bool = False):
        if v > SAVE_MAX or v < SAVE_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_sanity.setValue(v)
        else:
            self._spin_adjSanity.setValue(v)

    def getSanity(self, base: bool = False) -> int:
        if base:
            return self._spin_sanity.value()
        else:
            return self._spin_adjSanity.value()

    def setFear(self, v: int, base: bool = False):
        if v > SAVE_MAX or v < SAVE_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_fear.setValue(v)
        else:
            self._spin_adjFear.setValue(v)

    def getFear(self, base: bool = False) -> int:
        if base:
            return self._spin_fear.value()
        else:
            return self._spin_adjFear.value()

    def setBody(self, v: int, base: bool = False):
        if v > SAVE_MAX or v < SAVE_MIN:
            raise ValueError("Value out of range [{0}, {1}]".format(STAT_MIN, STAT_MAX))
        if base:
            self._spin_body.setValue(v)
        else:
            self._spin_adjBody.setValue(v)

    def getBody(self, base: bool = False) -> int:
        if base:
            return self._spin_body.value()
        else:
            return self._spin_adjBody.value()

    def updateClass(self, cl: MSClass):
        self._spin_adjSanity.setValue(self._spin_sanity.value() + Sanity[cl])
        self._spin_adjFear.setValue(self._spin_fear.value() + Fear[cl])
        self._spin_adjBody.setValue(self._spin_body.value() + Body[cl])

