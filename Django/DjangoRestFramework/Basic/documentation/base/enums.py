from django_enumfield import enum

class Gender_choice(enum.Enum):
    Male = 1
    Female = 2
    Others = 3

    __labels__ = {
        Male : 'Male',
        Female : 'Female',
        Others : 'Others'

    }