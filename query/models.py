from django.db import models
from query.managers import managers

# Create your models here.


PRODUCT_STATUS = (
    ("SL", "Sale"),
    ("NW", "NEW"),
    ("RJ", "REJECTED"),
)


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Can be used for common fields accross models


class Product(TimeStamp):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=PRODUCT_STATUS, blank=True, help_text="Product Status"
    )

    @property
    def discount_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "%.2f" % (float(self.price) * 0.8)

    class Meta:
        ordering = ["-id"]
        get_latest_by = "price"

    def __str__(self):
        return str(self.name)


class RejectedProduct(Product):
    objects = managers.RejectedProductManager()

    class Meta:
        proxy = True  # Copy of the actual model

    def rejected_date(self):
        return self.updated_at
