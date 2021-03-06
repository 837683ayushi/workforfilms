# Generated by Django 2.0.3 on 2018-04-02 07:33

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
            name='ActionVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActionVehicle_Action_Vehicle_Id', models.CharField(max_length=100, unique=True)),
                ('ActionVehicle_Color', models.TextField(blank=True, max_length=100, null=True)),
                ('ActionVehicle_Company', models.TextField(max_length=100)),
                ('ActionVehicle_Daily_Rent', models.CharField(max_length=100)),
                ('ActionVehicle_Description', models.TextField(max_length=100)),
                ('ActionVehicle_Make', models.DateTimeField(auto_now_add=True)),
                ('ActionVehicle_Model', models.TextField(max_length=100)),
                ('ActionVehicle_Modification', models.BooleanField(default=False)),
                ('ActionVehicle_Monthly_Rent', models.CharField(max_length=100)),
                ('ActionVehicle_Ownership', models.BooleanField(default=False)),
                ('ActionVehicle_Registration_Number', models.TextField(max_length=100)),
                ('ActionVehicle_Rigging', models.BooleanField(default=False)),
                ('ActionVehicle_Weekly_Rent', models.CharField(max_length=50)),
                ('ActionVehicle_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('ActionVehicle_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActionVehicle_Action_Vehicle_Comment', models.CharField(max_length=150)),
                ('ActionVehicle_Comment_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionvehicle', to=settings.AUTH_USER_MODEL)),
                ('Comment_Action_Vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action', to='actionvehicle.ActionVehicle')),
            ],
        ),
    ]
