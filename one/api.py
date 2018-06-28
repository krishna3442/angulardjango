#from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from one.serializers import ListSerializer,CardSerializer
from one.models import List,Card

class ListViewSet(ModelViewSet):
    queryset=List.objects.all()
    serializer_class=ListSerializer

class CardViewSet(ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSerializer


'''class Listapi(ListAPIView):
    queryset=List.objects.all()
    serializer_class=ListSerializer

class Cardapi(ListAPIView):
    queryset=Card.objects.all()
    serializer_class=CardSerializer'''
