import requests
import time

requests.packages.urllib3.disable_warnings()


# GET请求
def requestGET(url, headers=None, params=None, cookies=None, count=0):
    try:
        with requests.Session() as s:
            response = s.get(url, headers=headers, params=params, cookies=cookies, timeout=30, verify=False)
            if response.status_code == 200:
                return response
            raise ValueError('requestGET:' + str(url) + ' status_code:' + str(response.status_code))
    except Exception as e:
        count += 1
        if count < 5:
            time.sleep(1)
            return requestGET(url, headers, params, cookies, count)
        raise ValueError('requestGET: ' + str(e))
    finally:
        if 'response' in locals().keys():
            response.close()


# POST请求
def requestPOST(url, headers=None, data=None, json=None, cookies=None, count=0):
    try:
        with requests.Session() as s:
            response = s.post(url, headers=headers, data=data, json=json, cookies=cookies, timeout=10, verify=False)
            if response.status_code == 200:
                return response
            raise ValueError('requestGET:' + str(url) + ' status_code:' + str(response.status_code))
    except Exception as e:
        count += 1
        if count < 5:
            time.sleep(1)
            return requestPOST(url, headers, data, json, cookies, count)
        raise ValueError('requestPOST: ' + str(e))
    finally:
        if 'response' in locals().keys():
            response.close()
