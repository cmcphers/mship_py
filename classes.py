from enum import IntEnum
from PyQt5.QtCore import (pyqtSignal, pyqtSlot)
from PyQt5.QtWidgets import (QComboBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QSpinBox, QVBoxLayout)
import stats

NUM_CLASSES = 5
HEALTH_MIN = 0
HEALTH_MAX = 20
WOUNDS_MIN = 0
WOUNDS_MAX  = 3

class MSClass(IntEnum):
    NO_CLASS = 0
    MARINE = 1
    ANDROID = 2
    SCIENTIST = 3
    TEAMSTER = 4

Names = ["-- Select Class --", "Marine", "Android", "Scientist", "Teamster"]
Trauma = ["N/A",
                "Whenever you panic, every close friendly player must make a fear save.",
                "Fear saves made by close friendly players are at disadvantage.",
                "Whenever you fail a sanity save, all close friendly players gain 1 stress",
                "Once per session, you may take advantage on a panic check"]

Wounds = [0, 3, 3, 2, 2]

class MSClassBlock(QGroupBox):
    classChanged = pyqtSignal(int)
    modStatChanged = pyqtSignal(int)

    def __init__(self, parent):
        super(MSClassBlock, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)

        # Create all subwidgets
        v_main = QVBoxLayout()
        g_class = QGridLayout()
        lbl_class = QLabel("Class")
        lbl_modstat = QLabel("Modified Stat")
        lbl_health = QLabel("Max Health")
        lbl_wounds = QLabel("Max Wounds")
        self._cmb_class = QComboBox()
        for key in MSClass:
            self._cmb_class.addItem(Names[key], key)
        self._cmb_class.currentIndexChanged.connect(self._onclch)
        self._cmb_modstat = QComboBox()
        for key in stats.MSStat:
            self._cmb_modstat.addItem(stats.Names[key], key)
        self._cmb_modstat.currentIndexChanged.connect(self.modStatChanged)
        self._spin_health = QSpinBox()
        self._spin_health.setMinimum(HEALTH_MIN)
        self._spin_health.setMaximum(HEALTH_MAX)
        self._spin_wounds = QSpinBox()
        self._spin_wounds.setEnabled(False)
        self._spin_wounds.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        h_trauma = QHBoxLayout()
        lbl_trauma = QLabel("Trauma Response")
        self._cmb_trauma = QComboBox()
        for resp in Trauma:
            self._cmb_trauma.addItem(resp)

        # Lay everything out
        g_class.addWidget(lbl_class, 0, 0)
        g_class.addWidget(lbl_modstat, 0, 1)
        g_class.addWidget(lbl_health, 0, 2)
        g_class.addWidget(lbl_wounds, 0, 3)
        g_class.addWidget(self._cmb_class, 1, 0)
        g_class.addWidget(self._cmb_modstat, 1, 1)
        g_class.addWidget(self._spin_health, 1, 2)
        g_class.addWidget(self._spin_wounds, 1, 3)

        h_trauma.addWidget(lbl_trauma)
        h_trauma.addWidget(self._cmb_trauma)

        v_main.addLayout(g_class)
        v_main.addLayout(h_trauma)
        self.setLayout(v_main)

    @pyqtSlot(int)
    def _onclch(self, v: int):
        self._cmb_trauma.setCurrentIndex(v)
        self._spin_wounds.setValue(Wounds[v])
        self.classChanged.emit()

    def setClass(self, cl: MSClass):
        self._cmb_class.setCurrentIndex(cl)

    def getClass(self) -> MSClass:
        return self._cmb_class.currentData()

    def setModStat(self, st: stats.MSStat):
        self._cmb_modstat.setCurrentIndex(st)

    def getModStat(self) -> stats.MSStat:
        return self._cmb_modstat.currentData()

    def setHealth(self, v: int):
        if v < HEALTH_MIN or v > HEALTH_MAX:
            raise ValueError("Value out of range [{0}, {1}]".format(HEALTH_MIN, HEALTH_MAX))
        self._spin_health.setValue(v)

    def getHealth(self) -> int:
        return self._spin_health.value()

    def setWounds(self, v: int):
        if v < WOUNDS_MIN or v > WOUNDS_MAX:
            raise ValueError("Value out of range [{0}, {1}]".format(WOUNDS_MIN, WOUNDS_MAX))
        self._spin_wounds.setValue(v)

    def getWounds(self) -> int:
        return self._spin_wounds.value()
