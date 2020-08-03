from django.db import models

# Create your models here.
class RouteRank(models.Model):
    src = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    train_no = models.CharField(max_length=100)
    score = models.IntegerField()


class FindTrains(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    src = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    int_stop = models.CharField(max_length=100)
    train_no_src_to_intStop = models.CharField(max_length=100)
    train_no_intStop_to_dest = models.CharField(max_length=100)


