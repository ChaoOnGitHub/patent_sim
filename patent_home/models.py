from __future__ import unicode_literals

from django.db import models
from picklefield.fields import PickledObjectField

# Create PatentClaim model and LSI Model

class LSIModel(models.Model):
    models_pickle    =PickledObjectField()
    run_date         =models.DateTimeField()


class ClaimText(models.Model):
    Event_id         =models.CharField(primary_key=True,max_length=200)
    patent_Num       =models.TextField()
    claim            =models.TextField()
    sim_patent       =models.TextField()
    run_date         =models.DateTimeField()
