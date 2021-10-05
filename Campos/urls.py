from django.conf.urls.static import static
from django.urls import path
from Campos.views import campos, c1, adiciona_campo
from ProjetoCampeonato import settings

urlpatterns = [
    path('campos', campos, name='lista_campos'),
    path('c1', c1),
    path('adiciona_campo', adiciona_campo, name='adiciona_campo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)