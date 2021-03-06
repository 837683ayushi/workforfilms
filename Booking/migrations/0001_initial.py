# Generated by Django 2.0.3 on 2018-04-02 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_Status', models.TextField(max_length=100, unique=True)),
                ('Booking_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('Booking_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_Comment', models.CharField(max_length=150)),
                ('Booking_Comment_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_comment', to=settings.AUTH_USER_MODEL)),
                ('Comment_Booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_Bookingnew', to='Booking.Booking')),
            ],
        ),
    ]
