import pytest
import requests
import json

def test():
    response = requests.post(
        'http://localhost:8080/api/v1/ping',
        headers={'Content-Type': 'application/json'}, 
        data=json.dumps({'url': 'http://ReceiverService:8080/api/v1/info'})
      )
    print(response.text)
    # import pdb; pdb.set_trace()
    assert response.text == '"{\\n    \\"Receiver\\": \\"Cisco is the best!\\"\\n}\\n"\n'

# curl -X POST http://localhost:8080/api/v1/ping -H "Content-Type: application/json" -d '{"url":"http://ReceiverService:8080/api/v1/info"}'
