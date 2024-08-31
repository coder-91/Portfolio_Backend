from django.urls import path
from .views import ContactFormAPIView

urlpatterns = [
    path('contact-form/', ContactFormAPIView.as_view(), name='contact-form'),
]
