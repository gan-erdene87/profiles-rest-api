from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'aaa',
            'bbb',
            'ccc',
            'ddd',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

