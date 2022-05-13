from django.db import models


class RejectedProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="RJ")

    def create(self, status, **kwargs):
        product = self.model(status="RJ", **kwargs)
        product.save()
        return product
