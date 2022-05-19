from rest_framework import serializers

from .models import News, Comments


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = News
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    news = serializers.HyperlinkedRelatedField(view_name='news-detail', queryset=News.objects.all())

    class Meta:
        model = Comments
        fields = '__all__'
