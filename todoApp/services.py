import json
from django.db import transaction
from todoApp.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR

class NotesService:
    """
    Service layer for operations on notes
    """
    def __init__(self, request):
        self.request = request
        
    def create_note(self, request):
        """
        Creating a new note
        """
        try:
            data = json.loads(request)
            with transaction.atomic():
                serialized_notes_data = NoteSerializer(data = data)
                if serialized_notes_data.is_valid():
                    serialized_notes_data.save()
                    return Response(serialized_notes_data.data, status=HTTP_201_CREATED)
                
                else:
                    return Response({"Error":"Internal Server Error"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({"Error":"Internal Server Error"}, status=HTTP_500_INTERNAL_SERVER_ERROR)