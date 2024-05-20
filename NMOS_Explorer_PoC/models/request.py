import ipaddress

from django.db import models

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    device = ipaddress
    path = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id, self.path

    class Meta:
        app_label = 'NMOS_Explorer_PoC'