from django.db import models
from uuid import uuid4


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(verbose_name='email',
                              max_length=100, unique=True)
    username = models.CharField(
        verbose_name='username', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=100)
    last_name = models.CharField(verbose_name='last name', max_length=128)
    password = models.CharField(verbose_name='password', max_length=100)
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, default='avatars/default_avatar.png')
    created_at = models.DateTimeField(
        verbose_name='date registered', auto_now_add=True, null=True)
    last_login = models.DateTimeField(
        verbose_name='last login', auto_now=True, null=True)
    created_by = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='created by')

    ACCOUNT_STATUS_CHOICES = (
        ('active', 'Active'),
        ('blocked', 'Blocked'),
    )

    status = models.CharField(verbose_name='status', max_length=20,
                              choices=ACCOUNT_STATUS_CHOICES, default='active')
    
    def __str__(self):
        return self.username
