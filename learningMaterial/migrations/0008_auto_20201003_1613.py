# Generated by Django 3.1.2 on 2020-10-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningMaterial', '0007_auto_20201003_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturenote',
            name='title',
            field=models.CharField(blank=True, default='Note', max_length=80, null=True),
        ),
    ]
