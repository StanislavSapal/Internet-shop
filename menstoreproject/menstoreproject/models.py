from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, null=True, db_index=True)

    class Meta:
        abstract = True
