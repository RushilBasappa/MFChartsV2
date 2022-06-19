from django.shortcuts import render
from django.http import JsonResponse
from .models import Fund
from .serializers import FundSerializer


def fund_list(request):
    funds = Fund.objects.all()
    serializer = FundSerializer(funds, many=True)
    return JsonResponse(serializer.data, safe=False)
