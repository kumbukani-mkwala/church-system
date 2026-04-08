from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class PrayerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prayer by {self.user}"