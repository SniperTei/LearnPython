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
    # 如果data是字典
    if isinstance(data, dict):
      code = data.get('code', '000000')
      msg = data.get('msg', 'success')
      # data0 = data.get('data', None)
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
    else:
      modified_data = {
        'data': data,
        'msg': 'success',
        'code': '000000',
        'status_code': status_code
      }
    
    # Call the parent class's render method
    return super().render(modified_data, accepted_media_type, renderer_context)
