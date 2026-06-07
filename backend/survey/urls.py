from django.urls import path
from .views import survey_test

urlpatterns = [
    path("test/", survey_test),
]