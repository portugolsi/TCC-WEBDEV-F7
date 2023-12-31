# Generated by Django 4.1.3 on 2023-11-10 20:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('nome', models.CharField(help_text='Digite seu nome aqui', max_length=40)),
                ('contato', models.CharField(help_text='Digite seu numero aqui', max_length=11)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuarios',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(blank=True, null=True, upload_to='imoveis/')),
                ('tipo_imovel', models.CharField(choices=[('casa', 'Casa'), ('apto', 'Apartamento'), ('sitio', 'Sitio'), ('kitnet', 'Kitnet')], max_length=50)),
                ('estado', models.CharField(help_text='Digite o estado do imóvel', max_length=30)),
                ('cidade', models.CharField(help_text='Digite a cidade do imóvel', max_length=30)),
                ('bairro', models.CharField(help_text='Digite o bairro do imóvel', max_length=30)),
                ('rua', models.CharField(help_text='Digite a rua do imóvel', max_length=30)),
                ('preco', models.FloatField(help_text='Digite o preço do imóvel', max_length=30)),
                ('area', models.FloatField(help_text='Digite a área do imóvel', max_length=30)),
                ('disponibilidade', models.CharField(choices=[('disponivel', 'Disponivel'), ('indisponivel', 'Indisponivel')], max_length=50)),
                ('descricao', models.TextField(max_length=500)),
                ('usuario', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Imovel',
                'verbose_name_plural': 'Imoveis',
            },
        ),
    ]
