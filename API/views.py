# Django Imports
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# rest_framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, request
# rest_framework Authtoken Imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Application Imports
from API.models import Users, Members, ActivityPeriod
from API.serial import UsersSerializer, MembersSerializer, ActivitiesSerializer


# Create your views here.

# My Home Page with all details for my repositories & API related queries
def home(request):
    return render(request, "home.html")

# API to generate token key if user is authenticated & should be authorized in future to access resource


class UsersAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serial = self.serializer_class(
            data=request.data, context={'request': request})
        serial.is_valid(raise_exception=True)
        user = serial.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

# API to view All Users List


class UsersList(APIView):

    def get(self, request):
        queryset = Users.objects.all()
        serial = UsersSerializer(queryset, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    def post(self, request):
        serial = UsersSerializer(data=request.data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# API to view user detail


class UsersDetail(APIView):

    def getuser(self, user_id):
        try:
            model = Users.objects.get(id=user_id)
            return model
        except Users.DoesNotExist:
            return

    def get(self, request, user_id):
        if not self.getuser(user_id):
            return Response(f'User with ID {user_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

        serial = UsersSerializer(self.getuser(user_id))
        return Response(serial.data)

    def put(self, request, user_id):
        if not self.getuser(user_id):
            return Response(f'User with ID {user_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

        serial = UsersSerializer(self.getuser(user_id), data=request.data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        if not self.getuser(user_id):
            return Response(f'User with ID {user_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

        model = self.getuser(user_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API to view all  Activities list


class ActivitiesList(APIView):

    def get(self, request):
        queryset = ActivityPeriod.objects.all()
        serial = ActivitiesSerializer(queryset, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)


""" These Methods can be used to create new activities if required & assign to users """
# def post(self, request):
#     serial = ActivitiesSerializer(data=request.data)
#     if(serial.is_valid()):
#         serial.save()
#         return Response(serial.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivitiesDetail(APIView):

    def getactivity(self, activity_id):
        try:
            model = ActivityPeriod.objects.get(id=activity_id)
            return model
        except ActivityPeriod.DoesNotExist:
            return

    def get(self, request, activity_id):
        if not self.getactivity(activity_id):
            return Response(f'Activity for User ID {activity_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

        serial = ActivitiesSerializer(self.getactivity(activity_id))
        return Response(serial.data)


""" These Methods can be used to update & delete activities if required """
# # def put(self, request, activity_id):
# #     if not self.getactivity(activity_id):
# #         return Response(f'Activity for User ID {activity_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

# #     serial = ActivitiesSerializer(self.getactivity(
# #         activity_id), data=request.data)
# #     if(serial.is_valid()):
# #         serial.save()
# #         return Response(serial.data, status=status.HTTP_201_CREATED)
# #     else:
# #         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# # def delete(self, request, activity_id):
# #     if not self.getactivity(activity_id):
# #         return Response(f'Activity for User ID {activity_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

# #     model = self.getactivity(activity_id)
# #     model.delete()
# #     return Response(status=status.HTTP_204_NO_CONTENT)

# API to view all  members list


class MembersList(APIView):

    def get(self, request):
        queryset = Members.objects.all()
        serial = MembersSerializer(queryset, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    #  """ These Methods can be used to create new activities if required & assign to users """
    def post(self, request):
        serial = MembersSerializer(data=request.data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


# API to view member details
class MembersDetail(APIView):

    def getmember(self, member_id):
        try:
            model = Members.objects.get(id=member_id)
            return model
        except Members.DoesNotExist:
            return

    def get(self, request, member_id):
        if not self.getmember(member_id):
            return Response(f'Member with ID {member_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

        serial = MembersSerializer(self.getmember(member_id))
        return Response(serial.data)


""" These Methods can be used to create new members if they are valid i.e OK & assign as a member """
# def put(self, request, member_id):
#     if not self.getmember(member_id):
#         return Response(f'Member with ID {member_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

#     serial = MembersSerializer(
#         self.getmember(member_id), data=request.data)
#     if(serial.is_valid()):
#         serial.save()
#         return Response(serial.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# def delete(self, request, member_id):
#     if not self.getmember(member_id):
#         return Response(f'Member with ID {member_id} is not found in database', status=status.HTTP_404_NOT_FOUND)

#     model = self.getmember(member_id)
#     model.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
