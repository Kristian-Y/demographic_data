from django.urls import path
from .views import StatePopulationAPIView


urlpatterns = [
    path('state-populations/', StatePopulationAPIView.as_view(), name='state-population-list'),
]