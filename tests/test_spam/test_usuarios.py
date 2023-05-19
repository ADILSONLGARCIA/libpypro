import pytest
from time import sleep


class Sessao :
    contador = 0
    usuario = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id=Sessao.contador
        self.usuario.append(usuario)

    def listar(self):
        return self.usuario

    def roll_back(self):
        self.usuario.clear()

    def fechar(self):
        pass


class Conexao:
    def __init__(self):
        sleep(10)
    def gerar_sessao(self) :
        return Sessao()

    def fechar(self):
        pass


class Usuario :
    def __init__(self, nome):
        self.nome = nome
        self.id=None

@pytest.fixture
def conexao():
    # Setup
    # etapa de setup
    # responsável por gerar a autenticação do banco, como login e senha do bd para poder se
    # conectar.
    # serve para efetuar as alterações no bd, como salvamento, buscas, etc...
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()
@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # etapa de fear down
    # apos interagir com a conexão sw faz necessario fechar a sessao e conexao
    sessao_obj.roll_back ()  # roll_back desfaz todas as alterações feitas no ambiente de teste
    sessao_obj.fechar()


def test_salvar_usuario(sessao):

    # criando um usuario
    usuario=Usuario(nome='Adilson')
    # salva o usuario no bd
    sessao.salvar(usuario)
    # certifica se o usuario foi salvo com um id numerico
    assert isinstance(usuario.id, int)



def test_listar_usuarios(conexao, sessao):
    # etapa de setup
    # responsável por gerar a autenticação do banco, como login e senha do bd para poder
    # se conectar.
    # serve para efetuar as alterações no bd, como salvamento, buscas, etc...
    usuarios=[Usuario(nome='Adilson'), Usuario(nome='Rosana')]
    # criando um usuario
    for usuario in usuarios:
        # salva os usuarios no bd
        sessao.salvar(usuario)
    # asserção onde certifica que a lista de usuarios que acabamos de salvar será retornada
    # como uma sessao chamamos o metodo listar de uma sessao foi salvo com um id numerico
    assert usuarios == sessao.listar()
    # etapa de fear down

