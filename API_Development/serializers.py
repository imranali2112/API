from rest_framework import serializers
from .models import Contact, UserModel, Testing


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # feilds = ['name', 'email', 'subject', 'message']
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class Testingserializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'