# Generated by Django 5.0.3 on 2024-03-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_teammember_deleted_at_teammember_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
