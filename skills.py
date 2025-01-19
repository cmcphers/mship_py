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

Names = ["--Select Skill--","Linguistics","Zoology","Botany","Geology","Industrial Eqpt.","Jury Rigging",
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
    def __init__(self, parent):
        super(MSSkillBlock, self).__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)
        self._charClass = MSClass.NO_CLASS

        # Create subwidgets
        v_main = QVBoxLayout()
        h_top = QHBoxLayout()
        self._cmb_sk1 = QComboBox()
        self._cmb_sk1.addItem(Names[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk1.currentTextChanged.connect(self._onSK1Changed)
        self._cmb_sk2 = QComboBox()
        self._cmb_sk2.addItem(Names[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk2.currentTextChanged.connect(self._onSK2changed)
        self._cmb_sk3 = QComboBox()
        self._cmb_sk3.addItem(Names[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk3.currentTextChanged.connect(self._onSK3Changed)
        h_bot = QHBoxLayout()
        self._cmb_sk4 = QComboBox()
        self._cmb_sk4.addItem(Names[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
        self._cmb_sk4.currentTextChanged.connect(self._onSK4Changed)
        self._cmb_sk5 = QComboBox()
        self._cmb_sk5.addItem(Names[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
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
        pass

    @pyqtSlot(str)
    def _onSK1Changed(self, sk: str):
        pass

    @pyqtSlot(str)
    def _onSK2Changed(self, sk: str):
        pass

    @pyqtSlot(str)
    def _onSK3Changed(self, sk: str):
        pass

    @pyqtSlot(str)
    def _onSK4Changed(self, sk: str):
        pass

    @pyqtSlot(str)
    def _onSK5Changed(self, sk: str):
        pass

# Inserts the given skill into the combo box, maintaining order by the MSSkill enum value.
def InsertSkill(sk: MSSkill, cmb: QComboBox):
    for i in range(cmb.count()):
        if cmb.itemData(i) > sk:
            cmb.insertItem(i, Names[sk], sk)
            break
    else:
        cmb.addItem(Names[sk], sk)

# Ensures that the given combo box contains all prereqs for the given skill
def EnsurePrereqs(sk: MSSkill, cmb: QComboBox, exclusive: bool = False):
    for i in range(1, len(MSSkill)):
        is_prereq = IsPrereq(MSSkill(i), sk)
        idx = cmb.findData(MSSkill(i))
        if idx >= 0:
            if exclusive and not is_prereq:
                cmb.removeItem(idx)
        elif is_prereq:
            InsertSkill(MSSkill(i), cmb)

# Ensures that the given combo box contains all postreqs for the given skill.
def EnsurePostreqs(sk: MSSkill, cmb: QComboBox, exclusive: bool = False):
    for i in range(1, len(MSSkill)):
        is_postreq = IsPostreq(MSSkill(i), sk)
        idx = cmb.findData(MSSkill(i))
        if idx >= 0:
            if exclusive and not is_postreq:
                cmb.removeItem(idx)
        elif is_postreq:
            InsertSkill(MSSkill(i), cmb)

# Adds all skills of a given type to the combo box.
def AddAll(t: MSSkillType, cmb: QComboBox):
    for i in range(len(MSSkill)):
        if t == MSSkillType.NA or Types[i] == t:
            cmb.addItem(Names[i], MSSkill(i))

# Removes all skills of a given type from the combo box.
def RemoveAll(t: MSSkillType, cmb: QComboBox):
    if t == MSSkillType.NA:
        cmb.clear()
        cmb.addItem(Names[MSSkill.NO_SKILL], MSSkill.NO_SKILL)
    else:
        i = 1
        while i < cmb.count():
            if cmb.itemData(i) == t:
                cmb.removeItem(i)
            else:
                i += 1

# Checks if skill 1 is a prerequisite for skill 2
def IsPrereq(sk1: MSSkill, sk2: MSSkill) -> bool:
    for i in range(len(Prereqs[sk2])):
        if sk1 == Prereqs[sk2][i]:
            break
    else:
        return False
    return True

def IsPostreq(sk1: MSSkill, sk2: MSSkill) -> bool:
    for i in range(len(Postreqs[sk2])):
        if sk1 == Postreqs[sk2][i]:
            break
    else:
        return False
    return True