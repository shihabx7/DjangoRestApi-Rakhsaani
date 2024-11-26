# Generated by Django 4.1.3 on 2022-11-27 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("language", "0001_initial"),
        ("surah", "0017_audio_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="language",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="language.language"
            ),
        ),
        migrations.AlterField(
            model_name="audio",
            name="surah",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="surah.surah"
            ),
        ),
    ]