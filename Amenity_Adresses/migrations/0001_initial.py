# Generated by Django 2.0.3 on 2018-04-02 06:35

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
            name='Amenity_Adresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amenity_Adresses_Car_Parking', models.CharField(blank=True, max_length=100, null=True)),
                ('Amenity_Adresses_Catering_Base', models.CharField(blank=True, max_length=100, null=True)),
                ('Amenity_Adresses_Genset_Parking', models.CharField(blank=True, max_length=100, null=True)),
                ('Amenity_Adresses_Location_Id', models.CharField(max_length=100, unique=True)),
                ('Amenity_Adresses_Truck_Parking', models.CharField(blank=True, max_length=100, null=True)),
                ('Amenity_Adresses_Vanity_Parking', models.CharField(blank=True, max_length=100, null=True)),
                ('Amenity_Adresses_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('Amenity_Adresses_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amenity_Adresses_Comment', models.CharField(max_length=150)),
                ('Amenity_Adresses_Comment_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenity_adresses', to=settings.AUTH_USER_MODEL)),
                ('Comment_Amenity_Adresses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenity_adress', to='Amenity_Adresses.Amenity_Adresses')),
            ],
        ),
    ]
