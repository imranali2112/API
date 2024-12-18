from rest_framework import viewsets
from .models import Contact, UserModel, Testing
from .serializers import ContactSerializer, UserModelSerializer, Testingserializer


class ContactViewSets(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class UserModelViewSets(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class TestingViewSets(viewsets.ModelViewSet):
    queryset = Testing.objects.all()
    serializer_class = UserModelSerializer

