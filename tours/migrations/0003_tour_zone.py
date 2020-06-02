# Generated by Django 3.0.6 on 2020-06-02 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_user_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('operator', models.CharField(blank=True, max_length=50, null=True)),
                ('tour_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('img', models.URLField()),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('arrival_zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_arrival', to='tours.Zone')),
                ('takeoff_zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_takeoff', to='tours.Zone')),
            ],
        ),
    ]
