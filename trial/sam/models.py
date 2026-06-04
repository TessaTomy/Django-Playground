from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=25)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=25)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    age= models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    course = models.CharField(
    max_length=25,
    choices=(
        ('CS', 'Computer Science'),
        ('Math', 'Mathematics'),
        ('Physics', 'Physics'),
        ('Chem', 'Chemistry'),
    )
)

    photo= models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name

