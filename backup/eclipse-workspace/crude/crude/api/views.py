from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
  d = {'A':1,'B':2}
  return Response(d)

