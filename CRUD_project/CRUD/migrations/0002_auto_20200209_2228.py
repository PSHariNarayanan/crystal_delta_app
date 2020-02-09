# Generated by Django 3.0.2 on 2020-02-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=225),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=225),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=225),
        ),
    ]
