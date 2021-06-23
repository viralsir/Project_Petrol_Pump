from django.urls import path
from nozzel.views import *
urlpatterns=[
    path("entry/",NewNozzelView.as_view(),name="nozzel-entry"),
    path("view/",ListNozzelView.as_view(),name="nozzel-view"),
    path("update/<int:pk>",UpdateNozzelView.as_view(),name="nozzel-update"),
    path("delete/<int:pk>",DeleteNozzelView.as_view(),name="nozzel-delete")
]