from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Product(TimeStamp):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    content = models.TextField(blank=True, null=True)

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
