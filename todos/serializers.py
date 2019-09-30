from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'published_date',
            'boast',
            'roast'
        )
        model = Post
