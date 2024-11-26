from rest_framework import serializers
from .models import Surah, SurahDetail, SurahDuration


class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surah
        fields = '__all__'


class SurahDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurahDuration
        fields = '__all__'
        depth = 1


class SurahDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurahDetail
        fields = ['verse_serial', 'verse', 'time_in', 'time_out', 'text']
        depth = 1
