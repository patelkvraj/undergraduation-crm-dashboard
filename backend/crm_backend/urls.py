"""
URL configuration for crm_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import (
    StudentViewSet,
    StudentProfileViewSet,
    InteractionViewSet,
    InternalNoteViewSet,
)

# Create a router to automatically generate URL patterns for our ViewSets
router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(
    r"student-profiles", StudentProfileViewSet
)  # We'll use this for the individual profile view
router.register(r"interactions", InteractionViewSet)
router.register(r"notes", InternalNoteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/", include(router.urls)
    ),  # Include the API URLs under the 'api/' namespace
]
