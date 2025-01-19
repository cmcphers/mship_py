from enum import IntEnum

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

