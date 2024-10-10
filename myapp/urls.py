from django.urls import path
from .views import rawdata

urlpatterns = [
    path('rawdata/', rawdata, name='rawdata'),  # Add the URL for the rawdata API
]

