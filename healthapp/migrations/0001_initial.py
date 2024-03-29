# Generated by Django 3.2.4 on 2021-10-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255, null=True)),
                ('sex', models.CharField(max_length=255, null=True)),
                ('nationality', models.CharField(max_length=255, null=True)),
                ('height', models.CharField(max_length=255, null=True)),
                ('weight', models.CharField(max_length=255, null=True)),
                ('hip_circumference', models.CharField(max_length=255, null=True)),
                ('waist', models.CharField(max_length=255, null=True)),
                ('wrist_circumference', models.CharField(max_length=255, null=True)),
                ('blood_pressure', models.CharField(max_length=255, null=True)),
                ('heart_rate_variability', models.CharField(max_length=255, null=True)),
                ('heart_rate_alone', models.CharField(max_length=255, null=True)),
                ('vo2max', models.CharField(max_length=255, null=True)),
                ('body_temparature', models.CharField(max_length=255, null=True)),
                ('common_diseases', models.CharField(max_length=255, null=True)),
                ('blood_glucose_level', models.CharField(max_length=255, null=True)),
                ('movement_sleep_pattern', models.CharField(max_length=255, null=True)),
                ('libido', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendaions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommdes', models.TextField()),
                ('cost', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Risks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riskdes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_name', models.CharField(max_length=255, null=True)),
                ('pack_exp', models.CharField(max_length=255, null=True)),
                ('cost_per_recom', models.CharField(max_length=255, null=True)),
                ('long_coin', models.CharField(max_length=255, null=True)),
                ('userid', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
