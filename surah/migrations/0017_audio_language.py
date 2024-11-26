# Generated by Django 4.1.3 on 2022-11-27 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("language", "0001_initial"),
        ("surah", "0016_remove_surah_audio_audio"),
    ]

    operations = [
        migrations.AddField(
            model_name="audio",
            name="language",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="language.language",
            ),
            preserve_default=False,
        ),
    ]