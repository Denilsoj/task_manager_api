from django.db import models
from datetime import time
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    time_start = models.TimeField(null=True, blank=True, default=time(0,0))
    time_end = models.TimeField(null=True, blank=True, default=time(23,59,59))
    created_at = models.DateTimeField(auto_now=True)
    google_event_id = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'user', 'date'], name='unique_title_per_user_date')
        ]
    
    def __str__(self):
        return self.title
