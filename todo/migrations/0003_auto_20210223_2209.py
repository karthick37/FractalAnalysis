# Generated by Django 3.1.7 on 2021-02-23 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='bucket_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='todo.user'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='bucket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buckets', to='todo.bucket'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
