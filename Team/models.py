from django.db import models


class VideoFile(models.Model):
    file = models.FileField(upload_to='videos/')  # Файли будуть зберігатися у папці 'media/videos/'
    uploaded_at = models.DateTimeField(auto_now_add=True)
