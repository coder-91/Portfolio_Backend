from django.urls import path
from .views import ContactFormDataAPIView

urlpatterns = [
    path('message/', ContactFormDataAPIView.as_view(), name='message'),
]