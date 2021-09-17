# Generated by Django 3.2.7 on 2021-09-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_commentsandlikes_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsandlikes',
            name='reply',
        ),
        migrations.AddField(
            model_name='commentsandlikes',
            name='replies',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentsandlikes',
            name='comments',
            field=models.CharField(max_length=1000),
        ),
    ]