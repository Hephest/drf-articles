from rest_framework import serializers
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Article
        fields = '__all__'
