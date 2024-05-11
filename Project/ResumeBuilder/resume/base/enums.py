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


class Education_choice(enum.Enum):
    School = 1 
    College = 2
    Bachelors = 3 
    Masters = 4

    __labels__ = {
        School : 'School',
        College : 'College',
        Bachelors : 'Bachelors',
        Masters : 'Masters'
    }
