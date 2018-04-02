# Generated by Django 2.0.3 on 2018-04-02 08:34

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
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actor_Id', models.CharField(max_length=100, unique=True)),
                ('Actor_Body_Type', models.TextField(max_length=100)),
                ('Actor_Description', models.TextField(max_length=100)),
                ('Actor_Ethnicity', models.TextField(max_length=100)),
                ('Actor_Eye_Color', models.TextField(max_length=100)),
                ('Actor_Favorite_Acting_Styles', models.TextField(max_length=100)),
                ('Actor_Height', models.CharField(max_length=100)),
                ('Actor_Rates', models.CharField(max_length=100)),
                ('Actor_SceneComfort', models.TextField(max_length=100)),
                ('ACTOR_Skin_Color', models.TextField(max_length=100)),
                ('Actor_Smoker', models.BooleanField(default=False)),
                ('Actor_Weight', models.CharField(max_length=100)),
                ('Actor_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('Actor_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actors_Comment', models.CharField(max_length=150)),
                ('Actors_Comment_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actors', to=settings.AUTH_USER_MODEL)),
                ('Comment_Actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actors.Actors')),
            ],
        ),
    ]
