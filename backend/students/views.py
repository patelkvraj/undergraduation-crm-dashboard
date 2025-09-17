# backend/students/views.py


from rest_framework import viewsets
from .models import Student, Interaction, InternalNote
from .serializers import (
    StudentSerializer,
    StudentProfileSerializer,
    InteractionSerializer,
    InternalNoteSerializer,
)


# This ViewSet will handle listing all students and creating a new student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# This ViewSet is for the individual student profile
class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer


# This ViewSet handles all interactions
class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer


# This ViewSet handles all internal notes
class InternalNoteViewSet(viewsets.ModelViewSet):
    queryset = InternalNote.objects.all()
    serializer_class = InternalNoteSerializer
