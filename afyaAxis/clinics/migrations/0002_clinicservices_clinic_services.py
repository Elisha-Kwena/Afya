# Generated by Django 5.1.6 on 2025-02-22 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clinicServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='clinics_images')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='services',
            field=models.ManyToManyField(related_name='clinics', to='clinics.clinicservices'),
        ),
    ]
