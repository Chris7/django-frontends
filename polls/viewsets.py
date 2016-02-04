from rest_framework import viewsets

from .models import Choice, Poll
from .serializers import ChoiceSerializer, PollSerializer

# ViewSets define the view behavior.
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer