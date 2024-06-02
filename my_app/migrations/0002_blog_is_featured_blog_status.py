# Generated by Django 4.1 on 2024-06-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED')], max_length=20, null=True),
        ),
    ]