from rest_framework import serializers
from blog_app.models import Articles

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ["id", "title", "body", "date"]
        
        