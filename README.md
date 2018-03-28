# API Rest Utilizando Django Rest Framework

O Django Rest Framework (DRF) é uma biblioteca para o Framework Django que 
disponibiliza funcionalidades para implementar APIs Rest de forma extremamente rápida.

### Instalando e configurando o DRF, Django-Filter e Django OAuth Toolkit

Partindo do pressuposto que já tenha um ambiente virtual 
com Django instalado, é necessário instalar o DRF, Django-Filter e Django OAuth Toolkit com os seguintes comandos
no terminal:

$ pip install djangorestframework

$ pip install django-oauth-toolkit

$ pip install django-filter

### Arquivo settings.py

DEFAULT_APPS = [

    'django.contrib.admin',
    
    'django.contrib.auth',
    
    'django.contrib.contenttypes',
    
    'django.contrib.sessions',
    
    'django.contrib.messages',
    
    'django.contrib.staticfiles',
    
]

THIRD_PARTY_APPS = [

    'rest_framework',
    
    'oauth2_provider',
    
    'django_filters',
    
]

LOCAL_APPS = [

    'seu_app',
    
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DEFAULT_APPS

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': ('oauth2_provider.contrib.rest_framework.OAuth2Authentication',),
    
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    
}

OAUTH2_PROVIDER = {

    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
    
}

-----

### Documentação do django-rest-auth
https://django-portuguese.readthedocs.io/en/1.0/topics/auth.html

-----


### Tutoriais para implementar o projeto por *Marcos Rabaioli* - marcosrabaioli/django-rest

###### Models, serializers e views ######

- Instalando e configurando o DRF
- Criando o Primeiro Modelo
- Criando o Serializador da Classe Music
- Criando a View da Classe Music

https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa


###### Permissões e autenticações ######

- Ampliando Models, Serializers e Views
- Autenticação e Permissões

https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-rest-framework-parte-2-b14fa9495660


###### django-filter ######

- Instalando o Django-Filter
- Preparando as Views
- Customizando os Filtros

https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-3-fcbf5de22eaa

###### Django Rest Framework e Django OAuth Toolkit ######

- Instalando o Django OAuth Toolkit
- Iniciando e Configurando o Projeto
- Registrando Aplicação de Autenticação
- Criando Algumas Views
- Testando

https://medium.com/@marcosrabaioli/django-rest-framework-e-django-oauth-toolkit-c71f8920db08
