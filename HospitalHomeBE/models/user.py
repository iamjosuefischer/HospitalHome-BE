from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key = True)
    username = models.CharField('Username', max_length = 15, unique = True)
    password = models.CharField('Password', max_length = 256)
    perfil = models.CharField('Rol', max_length = 30)
    name = models.CharField('Name', max_length = 50)
    telefono = models.CharField('Telefono', max_length = 30)
    genero = models.CharField('Genero', max_length = 30)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'