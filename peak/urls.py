from django.urls import path

from peak.views import peak

urlpatterns = [
    path('<int:peak_id>', peak),
    path('', peak)
]
