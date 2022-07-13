from pickletools import pyfloat
from factory.django import DjangoModelFactory
from .models import Scheme, Nav
import factory


class SchemeFactory(DjangoModelFactory):
    class Meta:
        model = Scheme
    fundname = factory.Faker(
        "sentence", nb_words=4
    )


class NavFactory(DjangoModelFactory):
    class Meta:
        model = Nav
    scheme = factory.SubFactory(SchemeFactory)
    nav = factory.Faker(
        "pyfloat",
        left_digits=2, right_digits=2, positive=True
    )
    date = factory.Faker("date")
