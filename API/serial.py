from rest_framework import serializers
from API.models import Users, ActivityPeriod,  Members
import json

# This package can also be used for Nested objects
## from drf_nested_serializer import NestedModelSerializer


# Activity Serializer
class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

# Users Serializer


class UsersSerializer(serializers.ModelSerializer):
    activity_periods = ActivitiesSerializer(many=True)

    class Meta:
        model = Users
        fields = ['uid', 'real_name', 'tz', 'activity_periods']
        ## nested_fields = {'activity_periods': 'user_activities'}

    def create(self, validated_data):
        activity_validated_data = validated_data.pop('activity_periods')
        user_activities = Users.objects.create(**validated_data)
        activity_set_serializer = self.fields['activity_periods']
        for each in activity_validated_data:
            each['user_activities'] = user_activities
        activities = activity_set_serializer.create(activity_validated_data)
        return user_activities

# Members Serializer (Additionally Implemented)


class MembersSerializer(serializers.ModelSerializer):
    members = UsersSerializer(many=True)

    class Meta:
        model = Members
        fields = ['ok', 'members']

    def create(self, validated_data):
        user_validated_data = validated_data.pop('members')
        user_lists = Members.objects.create(**validated_data)
        user_set_serializer = self.fields['members']
        for each in user_validated_data:
            each['user_lists'] = user_lists
        users = user_set_serializer.create(user_validated_data)
        return user_lists
