# Generated by Django 4.2.4 on 2024-09-17 15:41

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
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MediaUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_type', models.CharField(choices=[('personal', 'Personal'), ('prescription', 'Prescription')], max_length=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='uploads/videos/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('availability', models.CharField(blank=True, max_length=100, null=True)),
                ('desired_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('skills', models.ManyToManyField(blank=True, to='profiles.skill')),
                ('user', models.OneToOneField(limit_choices_to={'role': 'job_seeker'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]