# Generated by Django 4.1.2 on 2022-10-30 01:39

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_user_post_publish_61a97a_idx_blog_post_publish_bb7600_idx_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('pp', django.db.models.manager.Manager()),
            ],
        ),
    ]