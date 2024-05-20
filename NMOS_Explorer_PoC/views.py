from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from NMOS_Explorer_PoC.models import Request
from NMOS_Explorer_PoC.serializers import RequestSerializer
from NMOS_Explorer_PoC.utils import nmos

@api_view(['GET', 'POST'])
def request_list(request):
    if request.method == 'GET':
        requests = Request.objects.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        data['nmos_data'] = nmos.fetch_data(data['path'])
        serializer = RequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)