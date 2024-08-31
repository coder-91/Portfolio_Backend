from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from contact_form.serializers import ContactFormSerializer


# Create your views here.
class ContactFormAPIView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']

            email_message = (
                f"Name: {name}\n\n"
                f"Email: {email}\n\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}"
            )

            send_mail(
                subject=f'New Message from {name} via Portfolio Contact Form',
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.NOTIFY_EMAIL],
                fail_silently=False,
            )
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
