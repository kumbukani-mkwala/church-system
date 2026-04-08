from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video_link = models.URLField(blank=True, null=True)
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    document = models.FileField(upload_to='sermons/docs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title