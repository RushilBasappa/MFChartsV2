from django.db import models

# Create your models here.


class Scheme(models.Model):
    id = models.AutoField(primary_key=True)
    fundname = models.CharField(max_length=50)


class Nav(models.Model):
    id = models.AutoField(primary_key=True)
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE)
    nav = models.DecimalField(max_digits=8, decimal_places=4)
    date = models.DateField()

    class Meta:
        unique_together = ('scheme_id', 'date')
