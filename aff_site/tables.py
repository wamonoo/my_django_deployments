import django_tables2 as tables
from aff_site.models import Participant

class ParticipantTable(tables.Table):
    class Meta:
        model = Participant
