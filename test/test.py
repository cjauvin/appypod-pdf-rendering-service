import json
import requests
from io import StringIO


values = {
    'answer': 'You bet!',
    'rows': [('aaa', 'bbb'), ('ccc', 'ddd')]
}

files = {
    'tmpl': ('test_from_python.odt', open('test.odt', 'rb'), 'application/vnd.oasis.opendocument.text', {'Expires': '0'}),
    'values': StringIO(json.dumps(values))  # could also be a file
}

# expects that service port 12345 has been mapped to 80
r = requests.post(
    'http://localhost', files=files
)

with open('test.pdf', 'wb') as f:
    f.write(r.content)
