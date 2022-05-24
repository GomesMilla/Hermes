#coding: utf-8
from Store.models import Category, Descreption
'''
Código para executar o script
$ python manage.py shell
$ exec(open('Apps/Scripts/CreateCategory.py').read())
'''

list_category = {
    'category':
    [
        {
            'name': 'Hardware',
            'descreption': 'Artigos das mais diversas areas! Tudo para facilitar sua vida academica e profissional',
        },
        {
            'name': 'Periféricos',
            'descreption': 'Sobre o mundo profissional e academico para se manter atualizado!',
        },
        {
            'name': 'Computadores',
            'descreption': 'Os mais diversos podcast com o intuito de levar a melhor educação possível até voce!',
        },
        {
            'name': 'Monitores',
            'descreption': 'Documentários diversificado! A sensação é de estar assistindo a série do momento!',
        },
         {
            'name': 'Cadeiras e Mesas Gamer e Escritório',
            'descreption': 'Artigos das mais diversas areas! Tudo para facilitar sua vida academica e profissional',
        },
        {
            'name': 'Eletronicos',
            'descreption': 'Sobre o mundo profissional e academico para se manter atualizado!',
        },
        {
            'name': 'Notebooks e Portáteis',
            'descreption': 'Os mais diversos podcast com o intuito de levar a melhor educação possível até voce!',
        },
        {
            'name': 'Redes e Wireless',
            'descreption': 'Documentários diversificado! A sensação é de estar assistindo a série do momento!',
        },
         {
            'name': 'Realidade Virtual',
            'descreption': 'Artigos das mais diversas areas! Tudo para facilitar sua vida academica e profissional',
        },
        {
            'name': 'Casa Inteligente',
            'descreption': 'Sobre o mundo profissional e academico para se manter atualizado!',
        },
        {
            'name': 'Mundo Geek',
            'descreption': 'Os mais diversos podcast com o intuito de levar a melhor educação possível até voce!',
        },
        {
            'name': 'Openbox',
            'descreption': 'Documentários diversificado! A sensação é de estar assistindo a série do momento!',
        },
         {
            'name': 'Casa e Lazer',
            'descreption': 'Artigos das mais diversas areas! Tudo para facilitar sua vida academica e profissional',
        },
    ],
}


def validar(valor):
    try:
        Category.objects.get(name=valor)
        return False
    except:
        return True



for category in list_category['category']:
    name = category['name']
    descreption = category['descreption']
    
    if validar(name):
        objCategory = Category()
        objCategory.name = name
        objCategory.descreption = descreption
        objCategory.save()
    
        print(f'Categoria = {name} foi CADASTRADA!!')
    else:
        print(f'A Categoria usuario = {name} já esta cadastrada!!')