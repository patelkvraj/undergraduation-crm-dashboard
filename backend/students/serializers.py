# backend/students/serializers.py

from rest_framework import serializers
from .models import Student, Interaction, InternalNote


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "email",
            "country",
            "application_status",
            "last_active",
        ]  # Fields for the Student Directory View


class StudentProfileSerializer(serializers.ModelSerializer):
    # Serializer to handle related models for the individual student profile
    interactions = serializers.SerializerMethodField()
    notes = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "grade",
            "country",
            "application_status",
            "last_active",
            "interactions",
            "notes",
        ]

    def get_interactions(self, obj):
        # Retrieve all interactions for the student
        interactions = Interaction.objects.filter(student=obj).order_by("-timestamp")
        return InteractionSerializer(interactions, many=True).data

    def get_notes(self, obj):
        # Retrieve all internal notes for the student
        notes = InternalNote.objects.filter(student=obj).order_by("-created_at")
        return InternalNoteSerializer(notes, many=True).data


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ["id", "student", "type", "timestamp", "details"]


class InternalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalNote
        fields = ["id", "student", "note", "created_at"]
