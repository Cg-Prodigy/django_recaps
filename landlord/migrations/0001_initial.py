# Generated by Django 4.1.2 on 2022-11-02 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandLord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('id_no', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('h_type', models.CharField(choices=[('BD', 'Bed seater'), ('OB', 'One Bedroom')], max_length=15)),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord.landlord')),
            ],
        ),
    ]