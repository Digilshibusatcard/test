from django.db import models

class RawPayload(models.Model):
    """This stores the raw data payload received from the WMS."""
    timestamp = models.DateTimeField(auto_now=True)
    payload = models.TextField()

    def __str__(self):
    	return str(self.timestamp)