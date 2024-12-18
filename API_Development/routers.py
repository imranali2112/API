from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContactViewSets, UserModelViewSets, TestingViewSets

routers = DefaultRouter()
routers.register(r'contact', ContactViewSets)
routers.register(r'usermodel', UserModelViewSets)
routers.register(r'testing', TestingViewSets)