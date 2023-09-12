from .models import *
from rest_framework import serializers
from decimal import Decimal
from rest_framework.validators import UniqueValidator
import bleach
from .utils import bleachvalidate

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
            model = Genre
            fields = '__all__'
            extra_kwargs = {
    'slug': {
        'validators': [
            UniqueValidator(queryset=Genre.objects.all())]
            }}


class BookSerializer(serializers.ModelSerializer):
    # stock = serializers.IntegerField(source ='inventory')
    price_after_discount = serializers.SerializerMethodField(method_name= 'calculate_discount')
    genre = GenreSerializer
    genre_id = serializers.IntegerField(write_only=True)
    def validate(self, attrs):
        bleachvalidate(attrs, 'title', 'author')        #next 2 rows, but by using .utils
        # attrs['title'] = bleach.clean(attrs['title'])
        # attrs['author'] = bleach.clean(attrs['author'])
        if (attrs['price_after_discount'] < 0.1):
            raise serializers.ValidationError('Price should not be less than 0.1')
        return super().validate(attrs)
    class Meta:
        model = Book
        fields = ['id','title','author','price','stock', 'price_after_discount','genre','genre_id']
        depth=1
        extra_kwargs = {
            'price':{'min_value':1},
            'stock':{'source':'inventory', 'min_value': 0},
            }       #min vals for variables
    def calculate_discount(self, product:Book):
        return round(product.price * Decimal(0.8), ndigits=2)


class BookSerializerRead(BookSerializer):
    genre = serializers.StringRelatedField()        #to show only a name of genre


class BookSerializerURLtoBook(BookSerializer, serializers.HyperlinkedModelSerializer): #also link to a single book
    class Meta:
        model = Book
        fields = ['id','title','author','genre', 'price','stock', 'price_after_discount']
        extra_kwargs = {
            'price':{'min_value':1},
            'stock':{'source':'inventory', 'min_value': 0},
            }


class BookSerializerURLtoGenre(BookSerializer, serializers.ModelSerializer):
    genre = serializers.HyperlinkedRelatedField(
    queryset = Genre.objects.all(),
    view_name='genre-detail'
    )
