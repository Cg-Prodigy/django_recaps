# Generated by Django 4.1.2 on 2022-10-30 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_publish'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='post',
            new_name='user_post_publish_61a97a_idx',
            old_name='blog_post_publish_bb7600_idx',
        ),
        migrations.AlterModelTable(
            name='post',
            table='user_post',
        ),
    ]