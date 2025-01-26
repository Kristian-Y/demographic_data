from rest_framework import serializers
from .models import StatePopulation

class StatePopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatePopulation
        fields = ['state_name', 'population', 'updated_at']
