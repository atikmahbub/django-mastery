from django.db import models


class RejectedProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="RJ")
