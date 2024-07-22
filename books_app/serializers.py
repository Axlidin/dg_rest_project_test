from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'summry', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        ##titleni harflaigini tekshirish
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitobning sarlavhasi harflardan iborat bo'lishi kerak."
                }
            )

        ##borligini tekshirish
        if Book.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlavhasi va mualifi kitoblar bazasida mavjud."
                }
            )
        return data

    def validate_price(self, price):
        print(price)
        if price < 0 or price >= 1000000:
            raise ValidationError(
                {
                    'status': False,
                    'message': "Narxi 0 va 1000000 gacha bo'lishi kerak."
                }
            )
        return price