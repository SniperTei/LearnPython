from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_s.models import User_S
from user_s.serializers import User_SSerializer

class User_SView(APIView):
  def get(self, request):
    # Implement your logic to retrieve all users
    users = User_S.objects.all()
    serializer = User_SSerializer(users, many=True)

    resp = {
      "code": "000000",
      "message": "success",
      "data": {
        "users": serializer.data
      }
    }
    # Return the list of users in the response
    return Response(resp, status=status.HTTP_200_OK)

  # def post(self, request):
    # Implement your logic to create a new user
    # You can access the request data using request.data

    # Return the created user in the response
    # return Response(user, status=status.HTTP_201_CREATED)

  # def put(self, request, pk):
  #   # Implement your logic to update a user with the given primary key (pk)
  #   # You can access the request data using request.data

  #   # Return the updated user in the response
  #   return Response(user, status=status.HTTP_200_OK)

  # def delete(self, request, pk):
  #   # Implement your logic to delete a user with the given primary key (pk)

  #   # Return a success message in the response
  #   return Response(status=status.HTTP_204_NO_CONTENT)