from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default = False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=120)
    style = models.CharField(choices =STYLES_CHOICES, default = 'friendly', max_length=150)

    class Meta:
        ordering =['created']

    @property
    def get_skill(self):
        return f'{self.language}: {self.style}'
    
    def __str__(self):
        return self.title