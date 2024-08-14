from django.urls import path
from . import views

urlpatterns = [
    path(
        "",views.tryview, name ="try"
    ),
    path(
        "home/",views.homeview, name ="home"
    )
]
