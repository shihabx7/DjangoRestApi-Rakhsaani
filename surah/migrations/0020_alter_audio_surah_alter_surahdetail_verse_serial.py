# Generated by Django 4.1.3 on 2022-11-27 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surah", "0019_surahdetail_verse_serial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="surah",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="surah.surah"
            ),
        ),
        migrations.AlterField(
            model_name="surahdetail",
            name="verse_serial",
            field=models.IntegerField(),
        ),
    ]