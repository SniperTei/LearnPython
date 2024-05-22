from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
  # Call DRF's default exception handler first
  response = exception_handler(exc, context)
  print('exception response:', response)

  # 服务器错误
  if response is None: 
    # If the default handler doesn't handle the exception, customize the response here
    error_message = str(exc)  # Get the error message from the exception
    status_code = 500  # Set the status code for the response

    default_err_msg = 'A server error occurred.'
    error_message = error_message if error_message != '' else default_err_msg
    # Create a custom response
    response_data = {
      'code': '999999', # Custom error code
      'msg': error_message, # Custom error message
      'status_code': status_code, # Custom status code
    }
    response = Response(response_data, status=status_code)

  return response