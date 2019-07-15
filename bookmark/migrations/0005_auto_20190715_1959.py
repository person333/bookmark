# Generated by Django 2.2.3 on 2019-07-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_auto_20190715_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='memo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date_published'),
        ),
    ]