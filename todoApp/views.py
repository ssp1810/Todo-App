import json
from django.shortcuts import render
from rest_framework import views 
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from todoApp.services import NotesService

class NotesView(views.APIView):
    def post(self, request, **kwargs):
        """
        To post notes
        """
        notes_service = NotesService(request)
        try:
            data = json.loads(request)
            notes_object = notes_service.create_note(request)
            return Response({"message": "Notes created successfully"}, status=HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": str(ex)}, status=HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        """
        To get list and individual notes
        """
        notes_service = NotesService(request=request)
        try:
            if pk:
                """
                Get data based on pk
                """
                data = notes_service.get_notes_details(request.user, pk)
                return Response(data, status=HTTP_200_OK)
            else:
                """
                Get list view data
                """
                response = notes_service.get_notes_list(request.user)
                return Response({"total": len(response[1]), "results": response[0]},
                                status=HTTP_200_OK)

        except Exception as ex:
            return Response({'message': 'Error occurred while fetching data'}, status=HTTP_400_BAD_REQUEST)