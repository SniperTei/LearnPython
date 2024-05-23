from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
  def render(self, data, accepted_media_type=None, renderer_context=None):
    print('data:', data)
    status_code = renderer_context['response'].status_code
    # 如果data是数组 最好不要返回数组吧。
    # if isinstance(data, list):
    #   modified_data = {
    #     'result': data,
    #     'msg': 'success',
    #     'code': '000000'
    #   }
    #   return super().render(modified_data, accepted_media_type, renderer_context)
    # 如果有error_code字段，说明是异常响应 不搞这一步了， 如果有错，让上一层直接给错误code
    # if data.get('error_code', None) is not None:
    #   modified_data = {
    #     'data': data.get('data', None),
    #     'msg': data.get('error_msg', None),
    #     'code': data.get('error_code', None)
    #   }
    #   return super().render(modified_data, accepted_media_type, renderer_context)
    # 如果没有error_code字段，说明是正常响应
    # Modify the data or format the response as needed
    modified_data = self.modify_data(data, status_code)
    
    # Call the parent class's render method
    return super().render(modified_data, accepted_media_type, renderer_context)
  
  def modify_data(self, data, status_code):
    code = data.get('code', '000000')
    msg = data.get('msg', 'success')
    # 如果code不是000000，data就是None
    if code != '000000':
      data = None
    # Add the code, msg and status_code to the response
    modified_data = {
      'data': data,
      'msg': msg,
      'code': code,
      'status_code': status_code
    }
    
    return modified_data