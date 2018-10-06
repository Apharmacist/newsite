from django.db import models

# Create your models here.

class Projects(models.Model):
    pname = models.CharField(max_length=20)
    pdate = models.DateTimeField()
    pboynum = models.IntegerField()
    pgirlnum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.pname

class Peoples(models.Model):
    pname = models.CharField(max_length=20)
    p_age = models.IntegerField()
    pgender = models.BooleanField(default=False)
    pcontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname


