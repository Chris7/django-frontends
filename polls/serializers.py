from rest_framework import serializers

from .models import Choice, Poll

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    poll = serializers.PrimaryKeyRelatedField(queryset=Poll.objects.all())
    class Meta:
        model = Choice
        fields = ('poll', 'choice_text', 'votes')


# Serializers define the API representation.
class PollSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True)
    class Meta:
        model = Poll
        fields = ('pk', 'question', 'pub_date', 'choices')