from django.shortcuts import render
from django.http import JsonResponse
from .models import Scheme
from .serializers import FundSerializer


def scheme_list(request):
    funds = Scheme.objects.all()
    serializer = FundSerializer(funds, many=True)
    return JsonResponse(serializer.data, safe=False)
