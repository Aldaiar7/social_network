# Generated by Django 4.0.4 on 2022-06-11 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_mark_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reccomendation',
            name='post',
        ),
        migrations.AlterModelOptions(
            name='repost',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.AddField(
            model_name='message',
            name='thread_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.post'),
        ),
        migrations.AlterField(
            model_name='repost',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reposts', to='account.profile'),
        ),
        migrations.DeleteModel(
            name='ProfileReccomendation',
        ),
        migrations.DeleteModel(
            name='Reccomendation',
        ),
    ]
