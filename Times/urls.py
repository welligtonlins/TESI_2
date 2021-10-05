from Times.views import  dados_time, adiciona_time
from django.urls import path

urlpatterns = [
   # path('', index, name='index'),
    path('dados_time', dados_time, name='dados_time'),
    path('adiciona_time', adiciona_time, name= 'adiciona_time'),
]