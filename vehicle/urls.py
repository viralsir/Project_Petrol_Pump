from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewVehicleView.as_view(),name="Vehicle-new"),
    path("view/",ListVehicleView.as_view(),name="Vehicle-view"),
    path("update/<int:pk>",UpdateVehicleView.as_view(),name="Vehicle-update"),
    path("delete/<int:pk>",DeleteVehicleView.as_view(),name="Vehicle-delete"),
    path("detail/<int:pk>",DetailVehicleView.as_view(),name="Vehicle-detail")
]