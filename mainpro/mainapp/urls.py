
from django.urls import path
from mainapp.views import test
urlpatterns = [
    path('hello/', view=test, name='test'),
]