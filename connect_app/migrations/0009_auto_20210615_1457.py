# Generated by Django 3.2 on 2021-06-15 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect_app', '0008_auto_20210614_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='editprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255, null=True)),
                ('yearofexperiance', models.IntegerField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('EmailID', models.CharField(max_length=255)),
                ('mobileno', models.IntegerField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connect_app.agent')),
            ],
        ),
        migrations.DeleteModel(
            name='industries',
        ),
    ]