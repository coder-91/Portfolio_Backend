from rest_framework import serializers


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    subject = serializers.CharField()
    message = serializers.CharField()
    isPrivacyPolicyAccepted = serializers.BooleanField()
