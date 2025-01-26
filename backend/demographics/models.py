from django.db import models
from django.utils.timezone import now

class StatePopulation(models.Model):
    state_name = models.CharField(max_length=255, unique=True)
    population = models.BigIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
