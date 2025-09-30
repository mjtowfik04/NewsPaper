from rest_framework import serializers
from News.models import Category, News, ImageModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']  

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['id','image']

class NewsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()  # <-- শুধুমাত্র এভাবেই
    image = ImageSerializer(many=True, read_only=True)  # যদি News এর অনেক image থাকে

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'category', 'url',
                  'image', 'is_featured', 'is_published', 'created_at', 'updated_at', 'published_at']

    def get_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/api/news/{obj.pk}/")
