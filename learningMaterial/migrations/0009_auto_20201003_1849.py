# Generated by Django 3.1.2 on 2020-10-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningMaterial', '0008_auto_20201003_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
