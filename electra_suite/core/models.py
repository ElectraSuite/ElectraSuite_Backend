from django.db import models
 
 
class ParamModel(models.Model):
    title = models.CharField(max_length=200)
    arr_of_params = models.TextField()
 
    def __str__(self):
        return self.title