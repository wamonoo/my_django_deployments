#from django.contrib.auth.models import Participant, Group
from aff_site.models import Participant
from rest_framework import serializers


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        #fields = ('url', 'username', 'email', 'groups')
        fields = '__all__'
