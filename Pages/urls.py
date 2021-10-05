from django.urls import path
from Pages.views import index, suporte

urlspatterns = [
    path('', index, name='index'),
    path('suporte', suporte, name='suporte')
]