# Generated by Django 3.2.18 on 2023-09-25 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_merge_20230924_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresponse',
            name='id',
        ),
        migrations.AddField(
            model_name='quizresponse',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.user_id'),
            preserve_default=False,
        ),
    ]