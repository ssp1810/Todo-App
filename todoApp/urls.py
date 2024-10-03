from django.contrib import admin
from django.urls import path, include
from todoApp.views import NotesView
urlpatterns = [
    path('post-note/', NotesView.as_view),
]