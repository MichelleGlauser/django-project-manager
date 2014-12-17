from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    difficulty_level = models.IntegerField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name