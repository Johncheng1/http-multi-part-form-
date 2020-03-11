import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import time
#请求地址
url = 'http://192.168.30.203/api/app/compalDetect/upload'
dst_path = f'/root/Pictures/test_data'

#头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Referer': url
}
for file in os.listdir(dst_path):
    print(file)
    multipart_encoder = MultipartEncoder(
            fields={#这里根据需要进行参数格式设置
                    'sn': file.split('.')[0], 'modelName': 'EDC40', 'projectId': '92',
                    'file': (file, open(os.path.join(dst_path, file), 'rb'), 'image/jpeg'),
                    })
    headers['Content-Type'] = multipart_encoder.content_type
    #请求头必须包含Content-Type: multipart/form-data; boundary=${bound}
    #这里也可以自定义boundary
    r = requests.post(url, data=multipart_encoder, headers=headers)
    #print(r.text)
    time.sleep(10)



