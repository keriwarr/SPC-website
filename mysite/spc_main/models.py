from django.db import models

class User(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    interests = models.ManyToManyField('Interest', blank=True)
    teams = models.ManyToManyField('Team', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + str(self.student_id)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_id(self):
        return self.student_id

class Team(models.Model):
    name = models.CharField(max_length=25)
    project = models.OneToOneField(
        'Project',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
