# Generated by Django 4.2.3 on 2023-07-24 19:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=128, verbose_name='last name')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('avatar', models.ImageField(blank=True, default='avatars/default_avatar.png', upload_to='avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date registered')),
                ('last_login', models.DateTimeField(auto_now=True, null=True, verbose_name='last login')),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=20, verbose_name='status')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='created by')),
            ],
        ),
    ]