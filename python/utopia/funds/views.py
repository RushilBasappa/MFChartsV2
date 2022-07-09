from django.shortcuts import render
from django.http import JsonResponse
from requests import Response, request
from .models import Fund, Nav, Date
from .serializers import FundSerializer, NavSerializer, DateSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def fund_list(request):
    funds = Fund.objects.all()
    serializer = FundSerializer(funds, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def fund_detail(request, id):
    try:
        fund = Fund.objects.get(pk=id)
    except Fund.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FundSerializer(fund)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def date_list(request):
    dates = Date.objects.all()
    serializer = DateSerializer(dates, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def date_detail(request, id):
    try:
        date = Date.objects.get(pk=id)
    except Date.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DateSerializer(date)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def nav_list(request):
    nav = Nav.objects.all()
    serializer = NavSerializer(nav, many=True)
    # import pdb
    # pdb.set_trace()
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def nav_detail(request, id):
    try:
        nav = Nav.objects.get(pk=id)
        # import pdb
        # pdb.set_trace()
    except Nav.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NavSerializer(nav)
    return Response(serializer.data)
