from django.db import models

# Create your models here.

class Scholarship(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    credit = models.CharField(max_length=50, blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    impaired = models.CharField(max_length=10, blank=True, null=True)
    merit = models.CharField(max_length=10, blank=True, null=True)
    major = models.CharField(max_length=50, blank=True, null=True)
    regular_decision = models.CharField(max_length=10, blank=True, null=True)
    period = models.CharField(max_length=50, blank=True, null=True)
    benefit = models.CharField(max_length=50, blank=True, null=True)
    spec = models.CharField(max_length=60, blank=True, null=True)
    stype = models.CharField(max_length=50)




#gggg