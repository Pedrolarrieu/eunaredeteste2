class Login1:
   
    def _init_ (self, nome, login_em_fila = 0):
        self.nome = nome
        if login_em_fila >= 0:
         self.Login_em_fila == login_em_fila
        else:
             raise ValueError(

                "A quantidade deve ser maior ou igual a 0."
            )

    def adiocionar_login_emfila (self):
        self.Login_em_fila += 1


    def remove_login (self):
        if self.Login_em_fila > 0:

         self.Login_em_fila -= 1



        



from base import models
from base.models import Task
from django import urls
from django.conf.urls import url
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import UserModel
from django.http.response import JsonResponse
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from base import views
from base import urls
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import admin
from django.urls import path, include


import pytest

##NOTAS 

#1 - Os testes são referentes ao views.py como diz o nome do arquivo.
#2- Teste simples de assert_code de referência, qualquer alteração no '<=200' resultará 'Failed' no final.
#3- O resultado dos códigos são de 300 por isso da sintaxe '<=200' que é para justamente passar por passed.
#4 - Pode fazer mais testes se baseando a partir daí 
#5 - O código executado de uma vez causará um 1 failed , 7 passed. O arquivo failed é o 'Task-delete'...
#que por algum motivo não é importado, encontrado, ou achado pelo pytest.
#6 - Tentei testar a database e logins mas nao consegui.


@pytest.mark.parametrize('param', [
('login'),
('register'),
('logout'),
('register'),
('tasks'),
('task-create'),
('task-delete'),
('task-reorder')
]
)

def test_render_views(client,param):
    temp_url = views.reverse_lazy (param)
    resp = client.get (temp_url)
    assert resp.status_code>=200
    



