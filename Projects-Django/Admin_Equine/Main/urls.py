from Main.views import index
from django.urls import path

app_name = 'Main'

urlpatterns = [
    path('', index, name='index'),
]
