from rest_framework import serializers

from profiles_api import models ###to allow access to our user profile model that we previously created

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer): ###to work with a model serializer we need to use a meta class to configure
    """"Serializes a user profile object"""               ###the serializer to point to a specific model

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password') ### our list of fields
        extra_kwargs = {
            'password': {
                'write_only': True, ### to avoid users to be able to access the password hash due to security breach
                'style':{'input_type':'password'} ### to hide password as we type (only for browsable API)
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user( ###Override the create function and call our create user function that we previously defined
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
