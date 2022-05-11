from django.urls import include, path
from query import views
from rest_framework import routers


app_name = "query"

# router = routers.SimpleRouter()
# router.register(r"products", views.ProductView)

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("rejected-products/", views.RejectedProductView.as_view()),
]
