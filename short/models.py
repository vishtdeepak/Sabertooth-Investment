from django.db import models


class URL(models.Model):
    full_url=models.TextField(null=True)
    hash=models.TextField(unique=True)

    class Meta:
        db_table='url_shortener'