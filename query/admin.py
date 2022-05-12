from django.contrib import admin
from query import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.RejectedProduct)
admin.site.register(models.ProductLocations)
