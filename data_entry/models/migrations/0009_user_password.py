# Generated by Django 5.0.1 on 2024-02-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_remove_user_created_by_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]