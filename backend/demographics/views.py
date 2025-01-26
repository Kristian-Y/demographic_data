
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StatePopulation
from .serializers import StatePopulationSerializer

class StatePopulationAPIView(APIView):

    def get(self, request):
        """Handles both returning all records and filtering by state name"""
        state_name = request.query_params.get('state_name', None)
        
        if state_name:
            queryset = StatePopulation.objects.filter(state_name__iexact=state_name)
        else:
            queryset = StatePopulation.objects.all()
        
        serializer = StatePopulationSerializer(queryset, many=True)
        return Response(serializer.data)