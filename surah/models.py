from django.db import models
from language.models import Language

# Create your models here.


class Surah(models.Model):
    surah_number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.surah_number} - {self.name}'


class Audio(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    language = models.OneToOneField(Language, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return f'{self.surah.surah_number} - {self.surah.name} - {self.language.name}'


class SurahDuration(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.surah.surah_number} - {self.surah.name} - duration({self.duration}) - {self.language.name}'


class SurahDetail(models.Model):
    verse_serial = models.IntegerField()
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    verse = models.CharField(max_length=10)
    time_in = models.CharField(max_length=50)
    time_out = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self) -> str:
        return f'Serial - {self.verse_serial} -{self.surah.surah_number} - {self.surah.name} - verse({self.verse}) - {self.language.name}'
