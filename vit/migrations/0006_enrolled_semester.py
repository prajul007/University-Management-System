# Generated by Django 2.1.7 on 2019-03-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vit', '0005_remove_enrolled_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolled',
            name='semester',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
