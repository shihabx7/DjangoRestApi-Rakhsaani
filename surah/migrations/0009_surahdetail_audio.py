# Generated by Django 4.1.3 on 2022-11-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surah", "0008_surahdetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="surahdetail",
            name="audio",
            field=models.FileField(default=1, upload_to="media/audio/"),
            preserve_default=False,
        ),
    ]
