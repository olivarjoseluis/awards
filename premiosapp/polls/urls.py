from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="index"),
    path("<int:question_id>/results/", views.result, name="index"),
    path("<int:question_id>/votes/", views.votes, name="index")
]
