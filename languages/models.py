from django.db import models


class Paradigm(models.Model):
     name = models.CharField(max_length=50)

     def __str__(self):
         return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete= models.CASCADE)
    framework = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name
    
class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name