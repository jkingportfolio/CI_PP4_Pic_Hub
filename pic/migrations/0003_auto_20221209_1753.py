# Generated by Django 3.2.16 on 2022-12-09 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pic', '0002_auto_20221209_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='following',
        ),
        migrations.AddField(
            model_name='feed',
            name='following_accounts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_followed_accounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='following_account_user', to=settings.AUTH_USER_MODEL),
        ),
    ]