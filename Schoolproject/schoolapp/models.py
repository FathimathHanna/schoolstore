from django.db import models

# Create your models here.
class Department(models.Model):
    Name=models.CharField(max_length=250)
    wikipedia_link=models.URLField()

    def __str__(self):
        return '{}'.format(self.Name)

class Course(models.Model):
    name=models.CharField(max_length=250)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)