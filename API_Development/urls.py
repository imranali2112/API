from django.urls import path, include
from .import views
from .routers import routers
urlpatterns = [
    path('', views.index, name='index'),
    path('api/',include(routers.urls)),
]