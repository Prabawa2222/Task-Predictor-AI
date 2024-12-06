# Generated by Django 5.1.4 on 2024-12-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='priority',
            new_name='priority_score',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='hours_until_deadline',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
    ]