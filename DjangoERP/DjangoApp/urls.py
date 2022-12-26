from django.urls import path
from .import views

urlpatterns = [
    path("", views.index),  # /DjangoApp
    path("<int:month>/", views.allmonths_challenge_by_number),
    # Dynamic - placeholders angle brackets for all months instead of each path
    path("<str:month>/", views.allmonths_challenge, name="month-challenge")

]
