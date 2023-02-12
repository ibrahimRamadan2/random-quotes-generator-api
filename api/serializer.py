from rest_framework import serializers
from .models import Quote


class qoute_serializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Quote
        fields = '__all__'
