from django.contrib.auth.models import User
from rest_framework import serializers

from .models import News, Comments, Category


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True, format='%H:%M:%S %Y-%m-%d')
    author_news = serializers.HyperlinkedRelatedField(many=True, view_name='news-detail', read_only=True)
    author_comments = serializers.HyperlinkedRelatedField(many=True, view_name='comments-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'author_news', 'author_comments')


class CategorySerializer(serializers.ModelSerializer):
    news_category = serializers.HyperlinkedRelatedField(many=True, view_name='news-detail', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.HyperlinkedRelatedField(view_name='category-detail', queryset=Category.objects.all())
    created_at = serializers.DateTimeField(read_only=True, format='%H:%M:%S %Y-%m-%d')
    updated_at = serializers.DateTimeField(read_only=True, format='%H:%M:%S %Y-%m-%d')
    news_comments = serializers.HyperlinkedRelatedField(many=True, view_name='comments-detail', read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    news = serializers.HyperlinkedRelatedField(view_name='news-detail', queryset=News.objects.all())
    created_at = serializers.DateTimeField(read_only=True, format='%H:%M:%S %Y-%m-%d')

    class Meta:
        model = Comments
        fields = '__all__'
