from enum import IntEnum
from PyQt5.QtCore import (pyqtSignal, pyqtSlot)
from PyQt5.QtWidgets import (QComboBox, QGroupBox, QHBoxLayout, QVBoxLayout)
from classes import MSClass

MAX_SKILLS = 5

class MSSkill(IntEnum):
    NO_SKILL = 0
    LINGUISTICS = 1
    ZOOLOGY = 2
    BOTANY = 3
    GEOLOGY = 4
    INDUSTRIAL_EQUIPMENT = 5
    JURY_RIGGING = 6
    CHEMISTRY = 7
    COMPUTERS = 8
    ZERO_G = 9
    MATHEMATICS = 10
    ART = 11
    ARCHAEOLOGY = 12
    THEOLOGY = 13
    MILITARY_TRAINING = 14
    RIMWISE = 15
    ATHLETICS = 16
    PSYCHOLOGY = 17
    PATHOLOGY = 18
    FIELD_MEDICINE = 19
    ECOLOGY = 20
    ASTEROID_MINING = 21
    MECHANICAL_REPAIR = 22
    EXPLOSIVES = 23
    PHARMACOLOGY = 24
    HACKING = 25
    PILOTING = 26
    PHYSICS = 27
    MYSTICISM = 28
    WILDERNESS_SURVIVAL = 29
    FIREARMS = 30
    HAND_TO_HAND = 31
    SOPHONTOLOGY = 32
    EXOBIOLOGY = 33
    SURGERY = 34
    PLANETOLOGY = 35
    ROBOTICS = 36
    ENGINEERING = 37
    CYBERNETICS = 38
    ARTIFICIAL_INTELLIGENCE = 39
    HYPERSPACE = 40
    XENOESOTERICISM = 41
    COMMAND = 42

class MSSkillType(IntEnum):
    NA = 0
    TRAINED = 1
    EXPERT = 2
    MASTER = 3

SkillNames = ["--Select Skill--","Linguistics","Zoology","Botany","Geology","Industrial Eqpt.","Jury Rigging",
           "Chemistry","Computers","Zero-G","Mathematics","Art","Archaeology",
           "Theology","Mil. Training","Rimwise","Athletics","Psychology","Pathology",
           "Field Medicine","Ecology","Asteroid Mining","Mech. Repair","Explosives","Pharmacology",
           "Hacking","Piloting","Physics","Mysticism","Survival","Firearms",
           "Hand-to-Hand","Sophontology","Exobiology","Surgery","Planetology","Robotics",
           "Engineering","Cybernetics","Artifical Int.","Hyperspace","Xenoesotericism","Command"]

Prereqs = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
          [MSSkill.LINGUISTICS,MSSkill.ZOOLOGY,MSSkill.BOTANY], [MSSkill.ZOOLOGY, MSSkill.BOTANY], [MSSkill.ZOOLOGY,MSSkill.BOTANY], [MSSkill.BOTANY,MSSkill.GEOLOGY],
          [MSSkill.GEOLOGY,MSSkill.INDUSTRIAL_EQUIPMENT], [MSSkill.INDUSTRIAL_EQUIPMENT,MSSkill.JURY_RIGGING],
          [MSSkill.INDUSTRIAL_EQUIPMENT,MSSkill.CHEMISTRY,MSSkill.MILITARY_TRAINING], [MSSkill.CHEMISTRY],
          [MSSkill.COMPUTERS], [MSSkill.ZERO_G], [MSSkill.MATHEMATICS], [MSSkill.ART,MSSkill.ARCHAEOLOGY,MSSkill.THEOLOGY],
          [MSSkill.BOTANY,MSSkill.MILITARY_TRAINING], [MSSkill.MILITARY_TRAINING,MSSkill.RIMWISE],
          [MSSkill.MILITARY_TRAINING,MSSkill.RIMWISE,MSSkill.ATHLETICS], [MSSkill.PSYCHOLOGY], [MSSkill.PATHOLOGY],
          [MSSkill.PATHOLOGY,MSSkill.FIELD_MEDICINE], [MSSkill.ECOLOGY,MSSkill.ASTEROID_MINING],
          [MSSkill.MECHANICAL_REPAIR], [MSSkill.MECHANICAL_REPAIR], [MSSkill.MECHANICAL_REPAIR],
          [MSSkill.HACKING], [MSSkill.PILOTING,MSSkill.PHYSICS,MSSkill.MYSTICISM], [MSSkill.MYSTICISM],
          [MSSkill.PILOTING,MSSkill.FIREARMS]]

Postreqs = [[], [MSSkill.PSYCHOLOGY], [MSSkill.PSYCHOLOGY,MSSkill.PATHOLOGY,MSSkill.FIELD_MEDICINE],
           [MSSkill.PATHOLOGY,MSSkill.ECOLOGY,MSSkill.WILDERNESS_SURVIVAL], [MSSkill.ECOLOGY,MSSkill.ASTEROID_MINING],
           [MSSkill.ASTEROID_MINING,MSSkill.MECHANICAL_REPAIR], [MSSkill.MECHANICAL_REPAIR,MSSkill.EXPLOSIVES],
           [MSSkill.EXPLOSIVES,MSSkill.PHARMACOLOGY], [MSSkill.HACKING], [MSSkill.PILOTING], [MSSkill.PHYSICS],
           [MSSkill.MYSTICISM], [MSSkill.MYSTICISM], [MSSkill.MYSTICISM],
           [MSSkill.EXPLOSIVES,MSSkill.WILDERNESS_SURVIVAL,MSSkill.FIREARMS,MSSkill.HAND_TO_HAND],
           [MSSkill.FIREARMS,MSSkill.HAND_TO_HAND], [MSSkill.HAND_TO_HAND], [MSSkill.SOPHONTOLOGY],
           [MSSkill.EXOBIOLOGY,MSSkill.SURGERY], [MSSkill.SURGERY], [MSSkill.PLANETOLOGY], [MSSkill.PLANETOLOGY],
           [MSSkill.ROBOTICS,MSSkill.ENGINEERING,MSSkill.CYBERNETICS], [], [], [MSSkill.ARTIFICIAL_INTELLIGENCE],
           [MSSkill.HYPERSPACE,MSSkill.COMMAND], [MSSkill.HYPERSPACE], [MSSkill.HYPERSPACE,MSSkill.XENOESOTERICISM], [],
           [MSSkill.COMMAND], [], [], [], [], [], [], [], [], [], [], [], []]

Types = [MSSkillType.NA, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED,
          MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED, MSSkillType.TRAINED,
          MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT,
          MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.EXPERT, MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER,
          MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER, MSSkillType.MASTER]

Master = [False, True, True, True, True, True, True, False, True, True, True, True, True, True, True,
         True, False, True, True, True, True, True, True, False, False, True, True, True, True,
         False, True, False, True, True, True, True, True, True, True, True, True, True, True]

ID = [MSSkill.NO_SKILL, MSSkill.LINGUISTICS, MSSkill.ZOOLOGY, MSSkill.BOTANY, MSSkill.GEOLOGY, MSSkill.INDUSTRIAL_EQUIPMENT, MSSkill.JURY_RIGGING,
      MSSkill.CHEMISTRY, MSSkill.COMPUTERS, MSSkill.ZERO_G, MSSkill.MATHEMATICS, MSSkill.ART, MSSkill.ARCHAEOLOGY, MSSkill.THEOLOGY, MSSkill.MILITARY_TRAINING,
      MSSkill.RIMWISE, MSSkill.ATHLETICS, MSSkill.PSYCHOLOGY, MSSkill.PATHOLOGY, MSSkill.FIELD_MEDICINE, MSSkill.ECOLOGY, MSSkill.ASTEROID_MINING,
      MSSkill.MECHANICAL_REPAIR, MSSkill.EXPLOSIVES, MSSkill.PHARMACOLOGY, MSSkill.HACKING, MSSkill.PILOTING, MSSkill.PHYSICS, MSSkill.MYSTICISM,
      MSSkill.WILDERNESS_SURVIVAL, MSSkill.FIREARMS, MSSkill.HAND_TO_HAND, MSSkill.SOPHONTOLOGY, MSSkill.EXOBIOLOGY, MSSkill.SURGERY,
      MSSkill.PLANETOLOGY, MSSkill.ROBOTICS, MSSkill.ENGINEERING, MSSkill.CYBERNETICS, MSSkill.ARTIFICIAL_INTELLIGENCE, MSSkill.HYPERSPACE,
      MSSkill.XENOESOTERICISM, MSSkill.COMMAND]


class MSSkillBlock(QGroupBox):
    def __init__(self, parent=None):
        super(MSSkillBlock, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)
        self._charClass = MSClass.NO_CLASS
        self._lastSkill = [MSSkill.NO_SKILL]*MAX_SKILLS

        # Create subwidgets
        v_main = QVBoxLayout()
        h_top = QHBoxLayout()
        self._cmb_sk1 = QComboBox()
        self._cmb_sk1.addItem(SkillNames[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk1.currentTextChanged.connect(self._onSK1Changed)
        self._cmb_sk2 = QComboBox()
        self._cmb_sk2.addItem(SkillNames[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk2.currentTextChanged.connect(self._onSK2Changed)
        self._cmb_sk3 = QComboBox()
        self._cmb_sk3.addItem(SkillNames[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk3.currentTextChanged.connect(self._onSK3Changed)
        h_bot = QHBoxLayout()
        self._cmb_sk4 = QComboBox()
        self._cmb_sk4.addItem(SkillNames[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk4.currentTextChanged.connect(self._onSK4Changed)
        self._cmb_sk5 = QComboBox()
        self._cmb_sk5.addItem(SkillNames[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk5.currentTextChanged.connect(self._onSK5Changed)

        # Lay everything out
        h_top.addWidget(self._cmb_sk1)
        h_top.addWidget(self._cmb_sk2)
        h_top.addWidget(self._cmb_sk3)
        h_bot.addStretch()
        h_bot.addWidget(self._cmb_sk4)
        h_bot.addWidget(self._cmb_sk5)
        h_bot.addStretch()
        v_main.addLayout(h_top)
        v_main.addLayout(h_bot)
        self.setLayout(v_main)

    def setSkill1(self, sk: int | str):
        if type(sk) is int:
            if sk >= self._cmb_sk1.count():
                raise IndexError("Index out of range for Skill 1 drop-down")
            self._cmb_sk1.setCurrentIndex(sk)
        else:
            idx = self._cmb_sk1.findText(sk)
            if idx < 0:
                raise ValueError("Could not find skill {0} in Skill 1 drop-down".format(sk))
            self._cmb_sk1.setCurrentIndex(idx)

    def getSkill1(self) -> MSSkill:
        return self._cmb_sk1.currentData()

    def getSkill1Enabled(self) -> bool:
        return self._cmb_sk1.isEnabled()

    def setSkill2(self, sk: int | str):
        if type(sk) is int:
            if sk >= self._cmb_sk2.count():
                raise IndexError("Index out of range for Skill 2 drop-down")
            self._cmb_sk2.setCurrentIndex(sk)
        else:
            idx = self._cmb_sk2.findText(sk)
            if idx < 0:
                raise ValueError("Could not find skill {0} in Skill 2 drop-down".format(sk))
            self._cmb_sk2.setCurrentIndex(idx)

    def getSkill2(self) -> MSSkill:
        return self._cmb_sk2.currentData()

    def getSkill2Enabled(self) -> bool:
        return self._cmb_sk2.isEnabled()

    def setSkill3(self, sk: int | str):
        if type(sk) is int:
            if sk >= self._cmb_sk3.count():
                raise IndexError("Index out of range for Skill 3 drop-down")
            self._cmb_sk3.setCurrentIndex(sk)
        else:
            idx = self._cmb_sk3.findText(sk)
            if idx < 0:
                raise ValueError("Could not find skill {0} in Skill 3 drop-down".format(sk))
            self._cmb_sk3.setCurrentIndex(idx)

    def getSkill3(self) -> MSSkill:
        return self._cmb_sk3.currentData()

    def getSkill3Enabled(self) -> bool:
        return self._cmb_sk3.isEnabled()

    def setSkill4(self, sk: int | str):
        if type(sk) is int:
            if sk >= self._cmb_sk4.count():
                raise IndexError("Index out of range for Skill 4 drop-down")
            self._cmb_sk4.setCurrentIndex(sk)
        else:
            idx = self._cmb_sk4.findText(sk)
            if idx < 0:
                raise ValueError("Could not find skill {0} in Skill 4 drop-down".format(sk))
            self._cmb_sk4.setCurrentIndex(idx)

    def getSkill4(self) -> MSSkill:
        return self._cmb_sk4.currentData()

    def getSkill4Enabled(self) -> bool:
        return self._cmb_sk4.isEnabled()

    def setSkill5(self, sk: int | str):
        if type(sk) is int:
            if sk >= self._cmb_sk5.count():
                raise IndexError("Index out of range for Skill 5 drop-down")
            self._cmb_sk5.setCurrentIndex(sk)
        else:
            idx = self._cmb_sk5.findText(sk)
            if idx < 0:
                raise ValueError("Could not find skill {0} in Skill 5 drop-down".format(sk))
            self._cmb_sk5.setCurrentIndex(idx)

    def getSkill5(self) -> MSSkill:
        return self._cmb_sk5.currentData()

    def getSkill5Enabled(self) -> bool:
        return self._cmb_sk5.isEnabled()

    def updateClass(self, cl: MSClass):
        self._lastSkill = [MSSkill.NO_SKILL]*MAX_SKILLS
        self._cmb_sk1.setEnabled(False)
        self._cmb_sk2.setEnabled(False)
        self._cmb_sk3.setEnabled(False)
        self._cmb_sk4.setEnabled(False)
        self._cmb_sk5.setEnabled(False)
        self._cmb_sk1.blockSignals(True)
        self._cmb_sk2.blockSignals(True)
        self._cmb_sk3.blockSignals(True)
        self._cmb_sk4.blockSignals(True)
        self._cmb_sk5.blockSignals(True)

        if cl == MSClass.MARINE:
            # SK1 fixed as Military Training
            self._cmb_sk1.clear()
            self._cmb_sk1.addItem(SkillNames[MSSkill.MILITARY_TRAINING], MSSkill.MILITARY_TRAINING)
            # SK2 fixed as Athletics
            self._cmb_sk2.clear()
            self._cmb_sk2.addItem(SkillNames[MSSkill.ATHLETICS], MSSkill.ATHLETICS)
            # SK3 filled with all available trained and expert skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk3)
            AddAll(MSSkillType.TRAINED, self._cmb_sk3, [MSSkill.MILITARY_TRAINING, MSSkill.ATHLETICS])
            EnsurePostreqs([MSSkill.MILITARY_TRAINING, MSSkill.ATHLETICS], self._cmb_sk3)
            # SK4 filled with all available trained skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk4)
            AddAll(MSSkillType.TRAINED, self._cmb_sk4, [MSSkill.MILITARY_TRAINING, MSSkill.ATHLETICS])
            RemoveAll(MSSkillType.NA, self._cmb_sk5)
            self._cmb_sk3.setEnabled(True)
            self._cmb_sk4.setEnabled(True)
        elif cl == MSClass.ANDROID:
            # SK1 fixed as Linguistics
            self._cmb_sk1.clear()
            self._cmb_sk1.addItem(SkillNames[MSSkill.LINGUISTICS], MSSkill.LINGUISTICS)
            # SK2 fixed as Computers
            self._cmb_sk2.clear()
            self._cmb_sk2.addItem(SkillNames[MSSkill.COMPUTERS], MSSkill.COMPUTERS)
            # SK3 fixed as Mathematics
            self._cmb_sk3.clear()
            self._cmb_sk3.addItem(SkillNames[MSSkill.MATHEMATICS], MSSkill.MATHEMATICS)
            # SK4 filled with all available trained and expert skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk4)
            AddAll(MSSkillType.TRAINED, self._cmb_sk4, [MSSkill.LINGUISTICS, MSSkill.COMPUTERS,
                                                        MSSkill.MATHEMATICS])
            EnsurePostreqs([MSSkill.LINGUISTICS, MSSkill.COMPUTERS, MSSkill.MATHEMATICS], self._cmb_sk4)
            # SK5 filled with all available trained skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk5)
            AddAll(MSSkillType.TRAINED, self._cmb_sk5, [MSSkill.LINGUISTICS, MSSkill.COMPUTERS,
                                                        MSSkill.MATHEMATICS])
            # Enable SK4 and SK5
            self._cmb_sk4.setEnabled(True)
            self._cmb_sk5.setEnabled(True)
        elif cl == MSClass.SCIENTIST:
            # Fill SK1 with all master skills
            RemoveAll(MSSkillType.NA, self._cmb_sk1)
            AddAll(MSSkillType.MASTER, self._cmb_sk1)
            # Ensure SK2, SK3, and SK5 are empty.
            RemoveAll(MSSkillType.NA, self._cmb_sk2)
            RemoveAll(MSSkillType.NA, self._cmb_sk3)
            RemoveAll(MSSkillType.NA, self._cmb_sk5)
            # Fill SK4 with all trained skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk4)
            AddAll(MSSkillType.TRAINED, self._cmb_sk4)
            # Enable SK1 only.
            self._cmb_sk1.setEnabled(True)
        elif cl == MSClass.TEAMSTER:
            # SK1 fixed as Industrial Equipment
            self._cmb_sk1.clear()
            self._cmb_sk1.addItem(SkillNames[MSSkill.INDUSTRIAL_EQUIPMENT], MSSkill.INDUSTRIAL_EQUIPMENT)
            # SK2 fixed as Zero-G
            self._cmb_sk2.clear()
            self._cmb_sk2.addItem(SkillNames[MSSkill.ZERO_G], MSSkill.ZERO_G)
            # SK3 filled with all available trained skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk3)
            AddAll(MSSkillType.TRAINED, self._cmb_sk3, [MSSkill.INDUSTRIAL_EQUIPMENT, MSSkill.ZERO_G])
            # SK4 filled with all available expert skills.
            RemoveAll(MSSkillType.NA, self._cmb_sk4)
            EnsurePostreqs([MSSkill.INDUSTRIAL_EQUIPMENT, MSSkill.ZERO_G], self._cmb_sk4)
            # Enable SK3 and SK4
            self._cmb_sk3.setEnabled(True)
            self._cmb_sk4.setEnabled(True)
        else:
            RemoveAll(MSSkillType.NA, self._cmb_sk1)
            RemoveAll(MSSkillType.NA, self._cmb_sk2)
            RemoveAll(MSSkillType.NA, self._cmb_sk3)
            RemoveAll(MSSkillType.NA, self._cmb_sk4)
            RemoveAll(MSSkillType.NA, self._cmb_sk5)
        self._charClass = cl
        if not self.isChecked():
            self.setChecked(True)
            self.setChecked(False)
        # Re-enable signals.
        self._cmb_sk1.blockSignals(False)
        self._cmb_sk2.blockSignals(False)
        self._cmb_sk3.blockSignals(False)
        self._cmb_sk4.blockSignals(False)
        self._cmb_sk5.blockSignals(False)

    @pyqtSlot(str)
    def _onSK1Changed(self, sk: str):
        if self._cmb_sk1.count() == 0:
            self._lastSkill[0] = MSSkill.NO_SKILL
            return
        else:
            id = self._cmb_sk1.currentData()
        if self._charClass == MSClass.SCIENTIST:
            EnsurePrereqs(id, self._cmb_sk2, True)
        if id > 0:
            self._cmb_sk2.setEnabled(True)
            if not self.isChecked():
                self.setChecked(True)
                self.setChecked(False)

    @pyqtSlot(str)
    def _onSK2Changed(self, sk: str):
        if self._cmb_sk2.count() == 0:
            self._lastSkill[1] = MSSkill.NO_SKILL
            return
        else:
            id = self._cmb_sk2.currentData()
        if self._charClass == MSClass.SCIENTIST:
            id4 = self._cmb_sk4.currentData()  # Get trained skill we need to not double-count
            # Ensure SK3 has all prereqs for this skill.
            EnsurePrereqs(id, self._cmb_sk3, True)
            if id4 > 0:
                i = self._cmb_sk3.findData(id4)
                if i >= 0:
                    self._cmb_sk3.removeItem(i)
            if id > 0:
                self._cmb_sk3.setEnabled(True)
                if not self.isChecked():
                    self.setChecked(True)
                    self.setChecked(False)
            

    @pyqtSlot(str)
    def _onSK3Changed(self, sk: str):
        if self._cmb_sk3.count() == 0:
            self._lastSkill[2] = MSSkill.NO_SKILL
            return
        else:
            id = self._cmb_sk3.currentData()

        if self._charClass == MSClass.MARINE or self._charClass == MSClass.SCIENTIST:
            if Types[id] == MSSkillType.EXPERT:
                self._cmb_sk4.setCurrentIndex(0)
                self._cmb_sk4.setEnabled(False)
            else:
                # Remove new selection from sk4.
                self._cmb_sk4.removeItem(self._cmb_sk4.findData(id))
                # Add back previous if it wasn't an expert skill.
                if Types[self._lastSkill[2]] == MSSkillType.TRAINED:
                    InsertSkill(self._lastSkill[2], self._cmb_sk4)
                # Ensure that sk4 is enabled.
                self._cmb_sk4.setEnabled(True)
                if not self.isChecked():
                    self.setChecked(True)
                    self.setChecked(False)
        elif self._charClass == MSClass.TEAMSTER:
            id1 = self._cmb_sk1.currentData()
            id2 = self._cmb_sk2.currentData()
            # Ensure that sk4 only has postreqs for sk1, sk2, and sk3.
            EnsurePostreqs([id, id1, id2], self._cmb_sk4, True)
        self._lastSkill[2] = id

    @pyqtSlot(str)
    def _onSK4Changed(self, sk: str):
        if self._cmb_sk4.count() == 0:
            self._lastSkill[3] = MSSkill.NO_SKILL
            return
        else:
            id = self._cmb_sk4.currentData()

        if self._charClass == MSClass.MARINE:
            # Remove new selection from sk3
            if id > 0:
                self._cmb_sk3.removeItem(self._cmb_sk3.findData(id))
            # Add back previous selection if it was a trained skill.
            if Types[self._lastSkill[3]] == MSSkillType.TRAINED:
                InsertSkill(self._lastSkill[3], self._cmb_sk3)
        elif self._charClass == MSClass.SCIENTIST:
            # Remove new selection from sk3.
            if id > 0:
                idx = self._cmb_sk3.findData(id)
                if idx > 0:
                    self._cmb_sk3.removeItem(idx)
            # Add back previous if it was another prerequisite to sk2.
            id2 = self._cmb_sk2.currentData()
            if IsPrereq(self._last_skill[3], id2):
                InsertSkill(self._last_skill[3], self._cmb_sk3)
        elif self._charClass == MSClass.ANDROID:
            # Same as marine for sk3 changed, but with sk4 and sk5.
            if Types[id] == MSSkillType.EXPERT:
                self._cmb_sk5.setCurrentIndex(0)
                self._cmb_sk5.setEnabled(False)
            else:
                # Remove the new selection from sk5
                self._cmb_sk5.removeItem(self._cmb_sk5.findData(id))
                # Add back the previous skill if it was trained.
                if Types[self._lastSkill[3]] == MSSkillType.TRAINED:
                    InsertSkill(self._lastSkill[3], self._cmb_sk5)
                # Ensure sk5 is enabled.
                self._cmb_sk5.setEnabled(True)
                if not self.isChecked():
                    self.setEnabled(True)
                    self.setEnabled(False)
        self._lastSkill[3] = id

    @pyqtSlot(str)
    def _onSK5Changed(self, sk: str):
        # Do nothing if the drop-down is cleared
        if self._cmb_sk5.count() == 0:
            self._lastSkill[4] = MSSkill.NO_SKILL
            return
        else:
            id = self._cmb_sk5.currentData()

        if self._charClass == MSClass.ANDROID:
            # Remove selection from sk4
            self._cmb_sk4.removeItem(self._cmb_sk4.findData(id))
            # Add back previous skill
            if Types[self._lastSkill[4]] == MSSkillType.TRAINED:
                InsertSkill(self._lastSkill[4], self._cmb_sk4)
        self._lastSkill[4] = id

# Inserts the given skill into the combo box, maintaining order by the MSSkill enum value.
def InsertSkill(sk: MSSkill, cmb: QComboBox):
    for i in range(cmb.count()):
        if cmb.itemData(i) > sk:
            cmb.insertItem(i, SkillNames[sk], sk)
            break
    else:
        cmb.addItem(SkillNames[sk], sk)

# Ensures that the given combo box contains all prereqs for the given skill
def EnsurePrereqs(sk: MSSkill | list[MSSkill], cmb: QComboBox, exclusive: bool = False):
    if type(sk) is MSSkill:
        sk = [sk]
    for i in range(1, len(MSSkill)):
        is_prereq = False
        for s in sk:
            is_prereq |= IsPrereq(MSSkill(i), s)
        idx = cmb.findData(MSSkill(i))
        if idx >= 0:
            if exclusive and not is_prereq:
                cmb.removeItem(idx)
        elif is_prereq:
            InsertSkill(MSSkill(i), cmb)

# Ensures that the given combo box contains all postreqs for the given skill.
def EnsurePostreqs(sk: MSSkill | list[MSSkill], cmb: QComboBox, exclusive: bool = False):
    if type(sk) is MSSkill:
        sk = [sk]
    for i in range(1, len(MSSkill)):
        is_postreq = False
        for s in sk:
            is_postreq |= IsPostreq(MSSkill(i), s)
        idx = cmb.findData(MSSkill(i))
        if idx >= 0:
            if exclusive and not is_postreq:
                cmb.removeItem(idx)
        elif is_postreq:
            InsertSkill(MSSkill(i), cmb)

# Adds all skills of a given type to the combo box.
def AddAll(t: MSSkillType, cmb: QComboBox, exceptions: list[MSSkill] | None = None):
    if exceptions is None:
        exceptions = []
    for i in range(len(MSSkill)):
        if t == MSSkillType.NA or Types[i] == t and MSSkill(i) not in exceptions:
            cmb.addItem(SkillNames[i], MSSkill(i))

# Removes all skills of a given type from the combo box.
def RemoveAll(t: MSSkillType, cmb: QComboBox):
    if t == MSSkillType.NA:
        cmb.clear()
        cmb.addItem(SkillNames[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
    else:
        i = 1
        while i < cmb.count():
            if cmb.itemData(i) == t:
                cmb.removeItem(i)
            else:
                i += 1

# Checks if skill 1 is a prerequisite for skill 2
def IsPrereq(sk1: MSSkill, sk2: MSSkill) -> bool:
    return sk1 in Prereqs[sk2]

def IsPostreq(sk1: MSSkill, sk2: MSSkill) -> bool:
    return sk1 in Postreqs[sk2]