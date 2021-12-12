# Generated by Django 3.2.9 on 2021-12-09 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_by_email', '0004_auto_20211208_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='djgrammuser',
            name='following',
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='following',
            constraint=models.UniqueConstraint(fields=('follower_user', 'following_user'), name='unique_follow'),
        ),
    ]
