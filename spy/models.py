from django.db import models

class LoginAttempt(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    attempt_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} at {self.attempt_time}"
