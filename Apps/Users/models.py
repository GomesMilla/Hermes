from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.db.models.deletion import CASCADE, SET_NULL
from smart_selects.db_fields import ChainedForeignKey

class UsuarioManager(BaseUserManager):
    def create_user(self,email,password=None):
        usuario = self.model(email = email)
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)        
        usuario.save()
        
        return usuario
    
    def create_superuser(self,email,password):
        usuario = self.create_user(email = email, password = password)
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario

class BaseModels(models.Model):
    name = models.CharField("Name", max_length=100)
    date_create = models.DateTimeField("Date Create", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="Usuário está ativo",default=True)
    deactivation_date =  models.DateTimeField("Date Create", auto_now_add=False, auto_now=True, blank=True, null=True)

    class Meta:
       abstract =True

class State(BaseModels): 
    sigla = models.CharField("Sigla", max_length=100)
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural="States"
        ordering = ['name']
        app_label = 'Users'

    def __str__(self):
        return self.name

class City(BaseModels):
    state = models.ForeignKey(State, max_length=100, on_delete=CASCADE)
    
    class Meta:
        verbose_name = "Citys"
        verbose_name_plural="Citys"
        ordering = ['name']
        app_label = 'Users'


    def __str__(self):
        return self.name
   
class Profile(AbstractBaseUser,PermissionsMixin,BaseModels):
    birth_date = models.DateField("Birth Date", auto_now=False, auto_now_add=False, blank=True, null=True)
    email = models.EmailField(max_length=194, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    profile_picture = models.ImageField("Foto de Perfil",  null=True, blank=True, upload_to="FotodePerfil/")
    is_active = models.BooleanField(verbose_name="Usuário está ativo",default=True)
    is_staff  = models.BooleanField(verbose_name="Usuário é da equipe de desenvolvimento", default= False)
    is_superuser = models.BooleanField(verbose_name= "Usuário é um superusuario",default=False)

    USERNAME_FIELD = "email"
    objects = UsuarioManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural="Users"
        ordering = ['name']
        app_label = 'Users'
        
    def __str__(self):
        return str(self.name)

# class Profile(models.Model):
#     user = models.OneToOneField("User")
#     state = models.ForeignKey("State", on_delete=CASCADE, related_name="state_of_user")
#     city = ChainedForeignKey(
#         City,
#         chained_field="state",
#         chained_model_field="state",
#         show_all=False,
#         auto_choose=True,
#         sort=True
#         )    

# class FavoritosUsuarios(models.Model):
#     usuario = models.ForeignKey("Usuario", on_delete=CASCADE, related_name="FavoritosdoUsuario")
#     publicacao = models.ForeignKey("Publicacoes.Publicacao", on_delete=CASCADE, related_name="PublicacoesFavoritas")
#     dataFavoritad = models.DateTimeField("Data da favoritação", auto_now_add=True)

#     class Meta:
#         verbose_name = "Favoritos Usuarios"
#         verbose_name_plural="Favoritos Usuarios"
#         ordering = ['usuario']
#         app_label = 'Usuarios'
        
#     def __str__(self):
#         return str(self.usuario)
