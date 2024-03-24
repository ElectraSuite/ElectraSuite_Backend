from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from handlers import mapping


# Create your views here.
  
@api_view(['POST'])
def post(request): 
    if request.method == 'POST':
        request_body = request.body
        request_body = request_body.decode()
        request_body = json.loads(request_body)
        print("checking", type(request_body), request_body)

    result = mapping.map_[request_body["name"]]["function"](request_body["params"])
    return  Response("chal gaya")