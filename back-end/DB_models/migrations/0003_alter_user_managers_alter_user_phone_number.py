# Generated by Django 5.1.6 on 2025-03-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB_models', '0002_remove_user_username_user_user_id_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
