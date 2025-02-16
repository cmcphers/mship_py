from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QComboBox, QGroupBox, QGridLayout, QLabel, QSpinBox)
from classes import MSClass
import trinkets
import patches
import loadouts

class MSEquipmentBlock(QGroupBox):
    def __init__(self, parent=None):
        super(MSEquipmentBlock, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)

        # Create subwidgets
        g_main = QGridLayout()
        lbl_loadout = QLabel("Loadout")
        self._cmb_loadout = QComboBox()
        for i in range(len(loadouts.NoClass)):
            self._cmb_loadout.addItem(loadouts.NoClass[0], loadouts.NoClassAP[0])
        self._cmb_loadout.currentIndexChanged.connect(self.onLoadoutChanged)
        lbl_trinket = QLabel("Trinket")
        self._cmb_trinket = QComboBox()
        for t in trinkets.Trinkets:
            self._cmb_trinket.addItem(t)
        lbl_patch = QLabel("Patch")
        self._cmb_patch = QComboBox()
        for p in patches.Patches:
            self._cmb_patch.addItem(p)
        lbl_armor = QLabel("Armor")
        self._spin_armor = QSpinBox()
        self._spin_armor.setEnabled(False)
        self._spin_armor.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        lbl_credits = QLabel("Credits")
        self._spin_credits = QSpinBox()
        self._spin_credits.setMinimum(0)
        self._spin_credits.setMaximum(10000)

        # Lay everything out
        g_main.addWidget(lbl_loadout, 0, 0)
        g_main.addWidget(self._cmb_loadout, 0, 1, 1, 3)
        g_main.addWidget(lbl_trinket, 1, 0)
        g_main.addWidget(self._cmb_trinket, 1, 1, 1, 3)
        g_main.addWidget(lbl_patch, 2, 0)
        g_main.addWidget(self._cmb_patch, 2, 1, 1, 3)
        g_main.addWidget(lbl_armor, 3, 0)
        g_main.addWidget(self._spin_armor, 3, 1)
        g_main.addWidget(lbl_credits, 4, 0)
        g_main.addWidget(self._spin_credits, 4, 1)
        self.setLayout(g_main)

    @pyqtSlot(int)
    def onLoadoutChanged(self, v: int):
        ap = self._cmb_loadout.currentData()
        if ap is not None:
            self._spin_armor.setValue(ap)
        else:
            self._spin_armor.setValue(0)

    def updateClass(self, cl: MSClass):
        # Briefly reset.
        self._cmb_loadout.clear()
        if cl == MSClass.MARINE:
            for i in range(len(loadouts.Marine)):
                self._cmb_loadout.addItem(loadouts.Marine[i], loadouts.MarineAP[i])
        elif cl == MSClass.ANDROID:
            for i in range(len(loadouts.Android)):
                self._cmb_loadout.addItem(loadouts.Android[i], loadouts.AndroidAP[i])
        elif cl == MSClass.SCIENTIST:
            for i in range(len(loadouts.Scientist)):
                self._cmb_loadout.addItem(loadouts.Scientist[i], loadouts.ScientistAP[i])
        elif cl == MSClass.TEAMSTER:
            for i in range(len(loadouts.Teamster)):
                self._cmb_loadout.addItem(loadouts.Teamster[i], loadouts.TeamsterAP[i])
        else:
            for i in range(len(loadouts.NoClass)):
                self._cmb_loadout.addItem(loadouts.NoClass[i], loadouts.NoClassAP[i])

    def setLoadout(self, i: int):
        if i < 0 or i > self._cmb_loadout.count():
            raise IndexError("Index out of range for number of loadouts")
        self._cmb_loadout.setCurrentIndex(i)

    def getNumLoadouts(self) -> int:
        return self._cmb_loadout.count()

    def setTrinket(self, i: int):
        if i < 0 or i > self._cmb_trinket.count():
            raise IndexError("Index out of range for number of trinkets")
        self._cmb_trinket.setCurrentIndex(i)

    def getNumTrinkets(self) -> int:
        return self._cmb_trinket.count()

    def setPatch(self, i: int):
        if i < 0 or i > self._cmb_patch.count():
            raise IndexError("Index out of range for number of patches")
        self._cmb_patch.setCurrentIndex(i)

    def getNumPatches(self) -> int:
        return self._cmb_patch.count()

    def setCredits(self, v: int):
        if v < self._spin_credits.minimum() or v > self._spin_credits.maximum():
            raise ValueError("Number of credits is out of range [{0}, {1}]".format(self._spin_credits.minimum(),
                                                                                   self._spin_credits.maximum()))
        self._spin_credits.setValue(v)