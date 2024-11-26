from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Q

from .models import Surah, SurahDuration, SurahDetail, Audio
from .serializers import SurahSerializer, SurahDurationSerializer, SurahDetailSerializer

import json
# Create your views here.


class SurahList(APIView):
    """
    List all surah.
    """

    def get(self, request, language, format=None):
        surah_list = SurahDuration.objects.filter(language__name=language)
        serializer = SurahDurationSerializer(surah_list, many=True)
        return Response(serializer.data)


class SurahDetails(APIView):
    """
    Retrieve surah instance.
    """

    def get_object(self, pk):
        try:
            return Surah.objects.get(surah_number=pk)
        except Surah.DoesNotExist:
            raise Http404

    def get(self, request, pk, language, format=None):
        surah = self.get_object(pk)
        surah_serializer = SurahSerializer(surah)
        surah_details = SurahDetail.objects.filter(Q(language__name=language) | Q(
            language__name='Arabic'), surah__surah_number=pk).order_by('verse_serial')
        surah_details_serializer = SurahDetailSerializer(
            surah_details, many=True)
        audio = Audio.objects.filter(
            language__name=language, surah__surah_number=pk).last()
        data = surah_serializer.data
        data.update({"audio": "/media/"+str(audio.audio), "verse_and_time": json.loads(
            json.dumps(surah_details_serializer.data))})
        return Response(data)
