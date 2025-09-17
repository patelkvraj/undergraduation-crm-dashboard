from django.contrib import admin
from .models import Student, Interaction, InternalNote

# Register your models here so they appear in the Django admin
admin.site.register(Student)
admin.site.register(Interaction)
admin.site.register(InternalNote)
