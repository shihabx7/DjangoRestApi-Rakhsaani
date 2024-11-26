from django.contrib import admin
from .models import Surah, SurahDetail, SurahDuration, Audio

# Register your models here.
admin.site.register(Surah)
admin.site.register(Audio)
admin.site.register(SurahDuration)
admin.site.register(SurahDetail)
