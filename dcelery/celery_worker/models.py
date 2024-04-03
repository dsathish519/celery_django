from django.db import models

class ScrapeData(models.Model):
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ip}:{self.port} - {self.protocol}"
