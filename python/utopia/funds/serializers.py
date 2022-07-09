from rest_framework import serializers
from .models import Fund, Nav, Date


class FundSerializer(serializers.ModelSerializer):
    # Fund_name = serializers.ReadOnlyField(source='Fund.name')
    # navs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Fund
        fields = ['id', 'name']


class DateSerializer(serializers.ModelSerializer):
    # date_date = serializers.ReadOnlyField(source='Date.date')

    class Meta:
        model = Date
        fields = '__all__'


class NavSerializer(serializers.ModelSerializer):
    fund_id = FundSerializer(many=False)
    date_id = DateSerializer(many=False)

    class Meta:
        model = Nav
        fields = ['id', 'fund_id', 'date_id', 'nav']
