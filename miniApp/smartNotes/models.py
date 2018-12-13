from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class SmartNotes(models.Model):
    title = models.CharField(max_length=64, unique=True)
    subjectName = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mentorName = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
