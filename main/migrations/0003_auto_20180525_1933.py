# Generated by Django 2.0.5 on 2018-05-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180517_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
