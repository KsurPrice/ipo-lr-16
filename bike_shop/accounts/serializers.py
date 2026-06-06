from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True, required=False, allow_blank=True)
    delivery_city = serializers.CharField(write_only=True, required=False, allow_blank=True)
    favorite_category = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'phone', 'delivery_city', 'favorite_category']

    def create(self, validated_data):
        full_name = validated_data.pop('full_name')
        phone = validated_data.pop('phone', '')
        delivery_city = validated_data.pop('delivery_city', '')
        favorite_category = validated_data.pop('favorite_category', '')
        user = User.objects.create_user(**validated_data)
        profile = user.profile
        profile.full_name = full_name
        profile.phone = phone
        profile.delivery_city = delivery_city
        profile.favorite_category = favorite_category
        profile.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'full_name', 'phone', 'address', 'role', 'delivery_city', 'favorite_category']