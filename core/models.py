from django.db import models



# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True)
    course = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name