import requests

def ocr_space_file(filename, api_key='helloworld', language='chs'):
    payload = {
        'apikey': api_key,
        'language': language,
        'isOverlayRequired': False
    }
    with open(filename, 'rb') as f:
        r = requests.post(
            'https://api.ocr.space/parse/image',
            files={'file': f},
            data=payload
        )
    return r.text

print(ocr_space_file('/home/ralmia/.openclaw/media/inbound/d4c49d0d-e897-49a6-99ec-2e5cc741771e.jpg', language='chs'))
