from .models import *
from rest_framework import serializers
from decimal import Decimal


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
            model = Genre
            fields = '__all__'
            


class BookSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source ='inventory')
    price_after_discount = serializers.SerializerMethodField(method_name= 'calculate_discount')
    genre = GenreSerializer
    genre_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Book
        fields = ['id','title','author','price','stock', 'price_after_discount','genre','genre_id']
        depth=1
        extra_kwargs = {'price':{'min_value':1}, 'inventory':{'min_value':0}}       #min vals for variables

    def calculate_discount(self, product:Book):
        return round(product.price * Decimal(0.8), ndigits=2)
    
class BookSerializerRead(serializers.ModelSerializer):
    stock = serializers.IntegerField(source ='inventory')
    price_after_discount = serializers.SerializerMethodField(method_name= 'calculate_discount')
    genre = serializers.StringRelatedField() #to show only a name of genre
    genre_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Book
        fields = ['id','title','author','price','stock', 'price_after_discount','genre','genre_id']
        depth=1

    def calculate_discount(self, product:Book):
        return round(product.price * Decimal(0.8), ndigits=2)

class BookSerializerURLtoBook(serializers.HyperlinkedModelSerializer):     #also link to a single book
    stock = serializers.IntegerField(source ='inventory')
    price_after_discount = serializers.SerializerMethodField(method_name= 'calculate_discount')
    genre = GenreSerializer
    class Meta:
        model = Book
        fields = ['id','title','author','price','stock', 'price_after_discount','genre','genre_id']
        depth=1

    def calculate_discount(self, product:Book):
        return round(product.price * Decimal(0.8), ndigits=2)

class BookSerializerURLtoGenre(serializers.ModelSerializer):
    stock = serializers.IntegerField(source ='inventory')
    price_after_discount = serializers.SerializerMethodField(method_name= 'calculate_discount')
    genre = serializers.HyperlinkedRelatedField(
    queryset = Genre.objects.all(),
    view_name='genre-detail'
    )
    class Meta:
        model = Book
        fields = ['id','title','author','price','stock', 'price_after_discount','genre','genre_id']
        depth=1

    def calculate_discount(self, product:Book):
        return round(product.price * Decimal(0.8), ndigits=2)
    
