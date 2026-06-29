from rest_framework import serializers
from page.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
        ]

    def validate_title(self, attr):
        if attr == 'bugun':
            raise serializers.ValidationError("Bugun so'zidan foydalanish mumkin emas")
        return attr