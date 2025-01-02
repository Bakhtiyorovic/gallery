from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class Timeline_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline_category
        fields = '__all__'



class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'



class About_descriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_description
        fields = '__all__'


class About_blog_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = About_blog_1
        fields = '__all__'



class About_blog_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = About_blog_2
        fields = '__all__'


class About_title_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = About_title_1
        fields = '__all__'




class About_title_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = About_title_2
        fields = '__all__'



class About_title_3Serializer(serializers.ModelSerializer):
    class Meta:
        model = About_title_3
        fields = '__all__'