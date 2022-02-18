# Generated by Django 4.0.2 on 2022-02-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_maininfo_catgry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catgry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='maininfo',
            name='catgrys',
            field=models.ManyToManyField(blank=True, null=True, to='app.Catgry'),
        ),
    ]