from rest_framework import serializers 
from .models import HomeFeed

class HomeFeedSerializer(serializers.HomeFeedSerializer):
    class Meta: 
        model = HomeFeed
        fields = ['id', 'title', 'content']
        
