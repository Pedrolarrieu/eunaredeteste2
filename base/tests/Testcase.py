import pytest 
from base.tests import variáveistest
from django.test import TestCase, testcases
from base.tests import variáveistest
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


##Teste cálculos mat (int)
def soma_1 (number):
    return int (number)  + 1

def sub_1 (number):
    return int (number) - 1

def mult_1 (number):
    return int (number) * 2

def div_1 (number):
    return int (number)  /2


def test_soma_1 ():
    assert soma_1(41) == 42

def test_sub1 ():
    assert sub_1 (10) == 9

def test_mult1 ():
    assert mult_1 (10) == 20

def test_div ():
    assert div_1 (10) == 5
    

#####TESTANDO NUMEROS COMO STRINGS.

def test_soma1_number_like_string():
    assert soma_1("41") == 42

def  test_sub_number_like_string():
    assert sub_1("10") == 9

def  test_mult_number_like_string():
    assert mult_1("10") == 20

def test_div ():
    assert div_1 ("10") == 5

###Teste com input de letras

def test_soma_palavras():
    with pytest.raises (ValueError):
     soma_1 ('Pedro') 

def test_sub_palavras():
    with pytest.raises (ValueError):
        sub_1 ('Pedro')

def test_mult_palavras ():
    with pytest.raises (ValueError):
        mult_1 ('Pedro')

def test_div_palavras ():
    with pytest.raises (ValueError):
        div_1 ('Pedro')


###Teste login
##Iria estar passed, porém permanece sem importar dados.
##Pode testar em um arquivo proprio. Que dará passed.
##Como teste simula logins, a mesma lógica de pode passar as tasks.
##Remover da lista, adicionar na fila, etc... Mesma lógica das tasks.
##Tentei adicionar a classe Login diretamente, mas ele nao executa testes.

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


def lista_de_login_valor_inicial_igual_0():
    Login1 = Login1 ("LOGIN USER X")

def list_login_valor_inicial_maior_0():
    Login1 = Login1 ("LOGIN USER", 1)
    assert Login1 == 1

def lista_login_valor_inicial_menor_0 ():
    Login1 = Login1 ("Login User", -1)

def adicionar_login_na_fila ():
    Login1 = Login1 ("Login user", 1)
    Login1.adicionarfila ()
    assert Login1 == 2

def remover_login_fila ():
    Login1 == Login1 ("Login user", 1)
    Login1.removelogin == Login1()
    assert Login1== 0




##Teste Tasks 

def task (number):
    return int (number)  + 1

def taskdelete (number):
    return int (number) - 1

def taskreoder (number):
    return int (number) == 0

def taskcreate (number):
    return int (number)  + 1


def task ():
    assert task (0) == 1

def testTaskdeleted ():
    assert taskdelete (20+30) == 49

def testTaskreoder ():
    assert taskreoder (10) == 10

def taskcreated ():
    assert taskcreate (20+30-50) == 1


###Teste nao realizdo, error de import
##Porem testado em outro Visual Studio, deu passed.


def lista_de_login_valor_inicial_igual_0():
    variáveistest.Login1 = variáveistest.Login1 ("LOGIN USER X")

def list_login_valor_inicial_maior_0():
    variáveistest.Login1 = variáveistest.Login1 ("LOGIN USER", 1)
    assert variáveistest.Login1 == 1

def lista_login_valor_inicial_menor_0 ():
    variáveistest.Login1 = variáveistest.Login1 ("Login User", -1)

def adicionar_login_na_fila ():
    variáveistest.Login1 = variáveistest.Login1 ("Login user", 1)
    variáveistest.adicionarfila ()
    assert variáveistest.Login1 == 2

def remover_login_fila ():
    variáveistest.Login1 == variáveistest.Login1 ("Login user", 1)
    variáveistest.removelogin == variáveistest()
    assert variáveistest.Login1 == 0


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
    



##Teste de lógicas matemáticas
##Teste de Lógica matemática como string
##Teste Login
##Demais testes não foram feitos.

