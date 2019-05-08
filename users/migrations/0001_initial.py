# Generated by Django 2.0.6 on 2019-05-07 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to=users.models.upload_pic_to)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.CharField(max_length=255, verbose_name='Present Address')),
                ('nid', models.CharField(max_length=23, verbose_name='NID')),
                ('nid_front', models.ImageField(upload_to=users.models.upload_pic_to, verbose_name='NID Front Picture')),
                ('nid_back', models.ImageField(upload_to=users.models.upload_pic_to, verbose_name='NID Back Picture')),
                ('nid_selfie', models.ImageField(upload_to=users.models.upload_pic_to, verbose_name='Selfie With Holding Your NID')),
                ('utility', models.ImageField(upload_to=users.models.upload_pic_to, verbose_name='NID')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
