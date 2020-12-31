from django.db import models

class FormResponse(models.Model):

    gender_choices = [
        ['Male','Male'],
        ['Female','Female'],
        ['Other','Other']
    ]

    timestamp = models.DateTimeField()
    user = models.CharField(max_length=500)
    name_of_respondent = models.CharField(max_length=500)
    gender_of_respondent = models.CharField(choices=gender_choices, max_length=7)
    reading_books = models.BooleanField()
    listening_music = models.BooleanField()
    mobile_no = models.CharField(max_length=15)
    record_latitude = models.DecimalField(decimal_places=6, max_digits=9)
    record_longitude = models.DecimalField(decimal_places=6, max_digits=9)
