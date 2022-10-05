from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Debe existir un nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser, PermissionsMixin):
        id= models.BigAutoField(primary_key=True)
        username = models.CharField('username', max_length=15, unique=True)
        password = models.CharField('Password', max_length=256)
        perfil = models.CharField('Perfil', max_length=30)
        nombre = models.CharField('Nombre', max_length=30)
        apellidos = models.CharField('Apellidos', max_length=30)
        telefono = models.CharField('Telefono', max_length=30)
        direccion = models.CharField('Dirección', max_length=30)
        
        def save(self, **kwargs):
            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            self.password = make_password(self.password, some_salt)
            super().save(**kwargs)
            
        objects = UsuarioManager()
        USERNAME_FIELD = 'username'