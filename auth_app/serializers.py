from user_app.models import OrganizationUsers
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUsers
        fields = ["id", "first_name", "last_name", "email", "active", "is_admin", "left", "password"]

    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)

    def validate(self, data):
        # Validate password
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                raise serializers.ValidationError({'password': list(e.messages)})
        if first_name == last_name:
            raise serializers.ValidationError({'first_name': 'First name and last name cannot be the same'})

        return data

    def create(self, validated_data):
        # Use the set_password method to handle password hashing
        user = OrganizationUsers(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            active=validated_data.get('active', True),
            is_admin=validated_data.get('is_admin', False),
            left=validated_data.get('left', False)
        )
        user.set_password(validated_data.get('password'))  # Hash the password
        user.save()
        return user

    def update(self, instance, validated_data):
        # Update fields, except for the password field
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.active = validated_data.get('active', instance.active)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.left = validated_data.get('left', instance.left)

        # Update the password if provided and hash it
        if 'password' in validated_data:
            instance.set_password(validated_data.get('password'))

        instance.save()
        return instance

