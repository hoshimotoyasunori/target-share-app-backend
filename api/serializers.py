from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Target, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwards = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'userProfile', 'created_at', 'img')
        extra_kwards = {'userProfile': {'read_only': True}}


class TargetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Target
        fields = (
            'id',
            'main',
            'sub1',
            'sub2',
            'sub3',
            'sub4',
            'sub6',
            'sub7',
            'sub8',
            'sub9',
            'userTarget',
            'created_at',
            'liked',
            'todo1_1',
            'todo1_2',
            'todo1_3',
            'todo1_4',
            'todo1_6',
            'todo1_7',
            'todo1_8',
            'todo1_9',
            'todo2_1',
            'todo2_2',
            'todo2_3',
            'todo2_4',
            'todo2_6',
            'todo2_7',
            'todo2_8',
            'todo2_9',
            'todo3_1',
            'todo3_2',
            'todo3_3',
            'todo3_4',
            'todo3_6',
            'todo3_7',
            'todo3_8',
            'todo3_9',
            'todo4_1',
            'todo4_2',
            'todo4_3',
            'todo4_4',
            'todo4_6',
            'todo4_7',
            'todo4_8',
            'todo4_9',
            'todo6_1',
            'todo6_2',
            'todo6_3',
            'todo6_4',
            'todo6_6',
            'todo6_7',
            'todo6_8',
            'todo6_9',
            'todo7_1',
            'todo7_2',
            'todo7_3',
            'todo7_4',
            'todo7_6',
            'todo7_7',
            'todo7_8',
            'todo7_9',
            'todo8_1',
            'todo8_2',
            'todo8_3',
            'todo8_4',
            'todo8_6',
            'todo8_7',
            'todo8_8',
            'todo8_9',
            'todo9_1',
            'todo9_2',
            'todo9_3',
            'todo9_4',
            'todo9_6',
            'todo9_7',
            'todo9_8',
            'todo9_9',
        )
        extra_kwargs = {'userTarget': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'userComment', 'target')
        extra_kwargs = {'userComment': {'read_only': True}}
