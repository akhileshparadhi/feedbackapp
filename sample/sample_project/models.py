from django.db import models

# Create your models here.
class Feedback(models.Model):
    firstName = models.CharField("First name", max_length=255, blank=True, null=True)
    lastName = models.CharField("Last name", max_length=255, blank=True, null=True)
    email = models.EmailField()
    country = models.CharField("country", max_length=255, blank=True, null=True)
    feed =models.TextField(blank=True, null=True)
    class Meta:
        db_table = "feedback"
