from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from snipermovie.user_s.models import User_S
from snipermovie.user_s.serializers import User_SSerializer

class SUserList(APIView):
  def get(self, request):
    # Implement your logic to retrieve all users
    # 打印request对象
    print("request: ", request)

    # Retrieve all users
    # user_lists = User_S.objects.all()
    # print("user_lists: ", user_lists)
    # Serialize the users
    # serializer = User_SSerializer(user_lists, many=True)

    # Return the list of users in the response
    # return Response(serializer.data, status=status.HTTP_200_OK)

    resp = {
      "code": "000000",
      "message": "success",
      "data": {
        "users": "hello world"
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