from rest_framework.serializers import ModelSerializer
from .models import Type1, Type2, Type3, Type4, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class Type1Serializer(ModelSerializer):
    class Meta:
        model = Type1
        fields='__all__'

class Type2Serializer(ModelSerializer):
    class Meta:
        model = Type2
        fields = '__all__'

class Type3Serializer(ModelSerializer):
    class Meta:
        model = Type3
        fields = '__all__'

class Type4Serializer(ModelSerializer):
    class Meta:
        model = Type4
        fields = '__all__'