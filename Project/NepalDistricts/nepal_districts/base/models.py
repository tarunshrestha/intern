from django.db import models


# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length= 50)


class Country(BaseModel):

    def __str__(self):
        return self.name    

class Province(BaseModel):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='province', null=True, default=156)

    def __str__(self):
        return self.name  

class District(BaseModel):
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="district", null=True)

    def __str__(self):
        return self.name  


class Muncipality(BaseModel):
    district_id =  models.ForeignKey(District, on_delete=models.CASCADE, related_name="muncipality", null=True)
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="muncipality", null=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='muncipality', null=True, default=156)

    def __str__(self):
        return self.name  
