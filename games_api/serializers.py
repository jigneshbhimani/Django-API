from games_api.models import *
from rest_framework import serializers

# Create your serializers here

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'category'
        ]


# Available on which Devices Serializer
class AvailableOnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Available_on
        fields = [
            'available_on_which_device'
        ]


# System requirements Serializer
class SystemRequirementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = System_requirements
        fields = [ 
            'os', 
            'architecture', 
            'notes'
        ]


# Publishers Serializer
class PublishersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publishers
        fields = [
            'id',
            'name'
        ]


# Language Supported Serializer
class LanguageSupportedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language_supported
        fields = [
            'id',
            'language'
        ]


# Capabilities Serializer
class CapabilitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Capabilities
        fields = [
            'id',
            'capabilities'
        ]


# Games Serializer
class GamesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=False)
    publishers = PublishersSerializer(many=False, read_only=True)
    available_on = AvailableOnSerializer(many=True, read_only=False)
    language_supported = LanguageSupportedSerializer(many=True)    # many=True
    system_requirements = SystemRequirementsSerializer(many=True, read_only=False)
    capabilities = CapabilitiesSerializer(many=True, read_only=False)

    class Meta:
        model = Games 
        fields = [
            'id', 
            'name', 
            'game_profile_pic', 
            'size', 
            'category', 
            'publishers', 
            'available_on', 
            'description', 
            'language_supported', 
            'system_requirements', 
            'capabilities', 
            'best_of_all_time', 
            'trending', 
            'release_date', 
            'age_rating', 
            'price', 
            'game_price_if_paid'
        ]