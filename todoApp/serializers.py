from rest_framework import serializers
from todoApp.models import Notes

class NoteSerializer(serializers.ModelSerializer):
      class Meta:
            model = Notes
            fields = ["note_id", "note_title", "note_body", "user"]
            