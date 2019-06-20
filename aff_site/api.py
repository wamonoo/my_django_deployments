from rest_framework.generics import ListAPIView

from .serializers import ParticipantSerializer
from .models import Participant

class ParticipantApi(ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
