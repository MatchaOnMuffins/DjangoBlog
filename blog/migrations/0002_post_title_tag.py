# Generated by Django 4.0.5 on 2022-06-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='<django.db.models.fields.CharF...', max_length=100),
        ),
    ]
