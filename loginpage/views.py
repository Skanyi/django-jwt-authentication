from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Account
from .serializers import AccountSerializer

class UserRegister(APIView):
    serializer_class = AccountSerializer
    permission_class = (AllowAny,)

    def post(self, request, format=None):
        '''
        Register a new user
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


