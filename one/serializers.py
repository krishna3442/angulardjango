from rest_framework import serializers
from one.models import Card,List


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model=Card
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    cards=CardSerializer(many=True,read_only=True)
    class Meta:
        model=List
        fields = '__all__'
