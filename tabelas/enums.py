from enum import Enum


class WeightClass(Enum):
    E1 = 'E1'
    E2 = 'E2'
    F1 = 'F1'
    F2 = 'F2'
    M1 = 'M1'
    M2 = 'M2'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class WeightMaterials(Enum):
    ACO_INOXIDAVEL = 'Aço Inoxidável'
    FERRO_FUNDIDO = 'Ferro Fundido'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
