from django.urls import path
from short import views


urlpatterns=[
    path('shorten', views.short_url, name="ShortUrl"),
]



