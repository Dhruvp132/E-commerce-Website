from django.urls import path
from .import views 

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("about/", views.index, name = "About Us"),
    path("contact/", views.contact, name = "ContactUs"),
    path("tracker/", views.tracker, name = "TrackingStatus"),
    path("search/", views.search, name = "Search"),
    path("productview/", views.productView, name = "Search"),
    path("checkout/", views.checkout, name = "Checkout")
]
