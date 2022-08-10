from django.db import models


class Parcel(models.Model):
    tracking_id = models.CharField(unique=True, max_length=40, blank=True, null=True)

    class Meta:
        db_table = "parcel"

    def __str__(self):
        return f"id={self.pk}, tracking_id={self.tracking_id}"
