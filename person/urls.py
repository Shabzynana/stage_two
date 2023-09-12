from django.urls import re_path as url
from django.urls import path, include

from .views import (
    PersonApiView, PersonIdApiView
)

urlpatterns = [

    path('api', PersonApiView.as_view()),
    path('api/<person_id>', PersonIdApiView.as_view()),
]
