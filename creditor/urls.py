from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewCreditorView.as_view(),name="creditor-new"),
    path("view/",ListCreditorView.as_view(),name="creditor-view"),
    path("update/<int:pk>",UpdateCreditorView.as_view(),name="creditor-update"),
    path("delete/<int:pk>",DeleteCreditorView.as_view(),name="creditor-delete"),
    path("detail/<int:pk>",DetailCreditorView.as_view(),name="creditor-detail")
]