# Generated by Django 4.1.3 on 2022-11-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surah", "0014_surahduration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="surah",
            name="audio",
            field=models.FileField(upload_to="audio/"),
        ),
    ]
