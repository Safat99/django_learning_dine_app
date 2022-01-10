from django.db import models

# Create your models here.
class List(models.Model): #table er naam dewa hoise List
    name = models.CharField(max_length= 200)
    location = models.CharField(max_length= 200)
    intro = models.CharField(max_length=500)
    
    #ekhon admin panel e show koranor jonno
    def __str__(self):
        return str(self.name) + " | " + str(self.location)
        