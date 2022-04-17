from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, name, last_name, email, password=None):

        if name is None:
            raise TypeError('User must have a name')
        if last_name is None:
            raise TypeError('User must have a last_name')
        if email is None:
            raise TypeError('User must have a email')

        user = self.model(name=name, last_name=last_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, last_name,  email, password):

        if password is None:
            raise TypeError('Superuser must have a password')

        user = self.create_user(name, last_name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    """ Custom User model """

    email = models.EmailField(max_length=255, db_index=True, unique=True, verbose_name='Почта')
    name = models.CharField(max_length=255, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, db_index=True, verbose_name='Фамилия')
    is_active = models.BooleanField(default=True, verbose_name='Состояние профиля пользвателя')
    is_staff = models.BooleanField(default=False, verbose_name='Права администрации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь - {self.name} ({self.last_name})'

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def get_short_name(self):
        return f'{self.name}'
