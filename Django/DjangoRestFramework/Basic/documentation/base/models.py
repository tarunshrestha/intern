from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    url_id = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def title_and_des(self):
        return f'{self.title}: {self.description}'
