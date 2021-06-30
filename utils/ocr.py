# -*- coding: utf-8 -*-
import time
import base64
from utils.request import requestGET, requestPOST


class OCRClass():
    def __init__(self, API_Key, Secret_Key):
        self.API_Key = API_Key
        self.Secret_Key = Secret_Key

    # https://cloud.baidu.com/ > 管理控制台 > 文字识别 > 应用列表 > API Key Secret Key > 得到access_token
    def get_token(self):
        get_token_data = {
            'grant_type': 'client_credentials',
            'client_id': self.API_Key,
            'client_secret': self.Secret_Key,
        }
        get_token_url = 'https://aip.baidubce.com/oauth/2.0/token'
        response = requestPOST(get_token_url, data=get_token_data)
        return response.json()['access_token']

    # 二进制格式转base64编码
    def get_img_base64(self, img_path):
        with open(img_path, 'rb') as f:
            return base64.b64encode(f.read())

    # type(url | image)url:传入图片url,image:传入图片二进制格式转base64编码
    def ocr(self, type, img, count=0):
        try:
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            if type == 'url':
                ocr_data = {
                    'access_token': self.get_token(),
                    'url': img
                }
            elif type == 'image':
                ocr_data = {
                    'access_token': self.get_token(),
                    'image': img
                }
            ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
            response = requestPOST(ocr_url, headers=headers, data=ocr_data)
            return ' '.join([words.get('words') for words in response.json()['words_result']])
        except Exception as e:
            count += 1
            if count < 5:
                time.sleep(1)
                return self.ocr(type, img, count)
            raise ValueError(str(e))

    def run(self, path):
        img = self.get_img_base64(path)
        return self.ocr('image', img)


if __name__ == '__main__':
    path = 'd:/1.jpg'
    API_Key = 'ax2GW9oyT1TpEbkEt6wltBRM'
    Secret_Key = 'CjBL22E4tpwuTPYyiXcWyFAs9CWAaUv5'
    ocr_obj = OCRClass(API_Key, Secret_Key)
    text = ocr_obj.run(path)
    print(text)
