# Generated by Django 4.0.2 on 2022-02-14 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_maininfo_des_maininfo_imdb_maininfo_rottom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='hero_img',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='post_img',
            field=models.URLField(null=True),
        ),
    ]
