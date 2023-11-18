from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, agent_id, password=None, **extra_fields):
        if not agent_id:
            raise ValueError('The agent_id field must be set')
        user = self.model(agent_id=agent_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, agent_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(agent_id, password, **extra_fields)



class Agents(AbstractBaseUser, PermissionsMixin):
    
    set_account_type = (
        ('DEV', 'Developer'),
        ('MAN', 'Manager'),
        ('AGT', 'Agent')
    )

    img_profile = models.ImageField(null=True, blank=True, upload_to="imgProfile/")
    agent_id = models.CharField(unique=True, max_length=20)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=30, null=False, default='first_name')
    last_name = models.CharField(max_length=30, default='last_name')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    permissions = models.CharField(max_length=255, blank=True, null=True)
    account_type = models.CharField(max_length=3, choices=set_account_type, null=False, default="AGT")
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'agent_id'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number', 'password']

    def __str__(self):
        return self.agent_id