from enum import Enum


class StatusClass(Enum):
    PROCESSING = 'processing'
    FINISHED = 'finished'
    ABORTED = 'Aborted'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]