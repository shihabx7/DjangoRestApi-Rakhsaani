from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer

# Create your views here.


class LanguageList(APIView):
    """
    List all languages.
    """
    def get(self, request, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)