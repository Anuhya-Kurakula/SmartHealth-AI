from django.db import models

class SurveyResponse(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    age = models.IntegerField()

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    village = models.CharField(max_length=100)

    health_issue = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.village} - {self.health_issue}"