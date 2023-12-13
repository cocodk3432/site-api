import requests as r
import json

def req1():
    try:
        url = ''
        headers = {'Accept': 'application/json'}
        postdata = {'url': url, 'headers': headers, 'data': postdata}
    
        response = r.post(url, postdata=postdata)
        if response.status_code == 200:
            print('success => 200')
        else:
            print('Error =>', response.status_code)
    except Exception as e:
        print(e)
        
    result = json.loads(response.text)
    return result[''] # add what data you want to return

def req2():
    try:
        url = 'http://'
        headers = {'Accept': 'application/json'}
        postdata = {}
        response = r.post(url, postdata=postdata)
        # add any condition if you want 
        if response.status_code == 200:
            print('success => 200')
        else:
            print('Error =>', response.status_code)
    except Exception as e:
        return response.text

if __name__ == '__main__':
    req1()
    req2()
