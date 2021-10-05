from django.urls import path
from Juizes.views import juizes, adiciona_juiz

urlpatterns = [
    path('juizes', juizes),
    path('adiciona_juiz', adiciona_juiz, name= 'adiciona_juiz'),
]