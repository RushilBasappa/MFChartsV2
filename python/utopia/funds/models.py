from django.db import models

# Create your models here.


class Fund(models.Model):
    name = models.CharField(max_length=50)

    # @property
    # def fund_id(self):
    #     return self.name


class Date(models.Model):
    date = models.DateField(auto_now_add=True)

    # @property
    # def date_id(self):
    #     return self.date


class Nav(models.Model):
    fund_id = models.ForeignKey(
        Fund, on_delete=models.CASCADE)
    date_id = models.ForeignKey(Date, on_delete=models.CASCADE)
    nav = models.DecimalField(max_digits=8, decimal_places=4)
