from django.db import models

# Student Directory View fields
APPLICATION_STATUS_CHOICES = [
    ("Exploring", "Exploring"),
    ("Shortlisting", "Shortlisting"),
    ("Applying", "Applying"),
    ("Submitted", "Submitted"),
]


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100)
    grade = models.CharField(max_length=50, blank=True, null=True)
    application_status = models.CharField(
        max_length=50,
        choices=APPLICATION_STATUS_CHOICES,
        default="Exploring",
    )
    last_active = models.DateTimeField(auto_now=True)

    # make the object more readable
    def __str__(self):
        return self.name


# Interaction Timeline and Communication Log
class Interaction(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="interactions"
    )
    type = models.CharField(
        max_length=100
    )  # e.g., 'login', 'AI question', 'document submitted', 'email', 'call'
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} with {self.student.name} at {self.timestamp}"


# Internal Notes
class InternalNote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note for {self.student.name}"
