from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ProfileService

class ProfileView(APIView):
    def get(self, request):
        profile_data = ProfileService.get_profile_data()
        return Response(profile_data, status=status.HTTP_200_OK)