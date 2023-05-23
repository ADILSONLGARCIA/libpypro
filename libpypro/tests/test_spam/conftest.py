import pytest

from libpypro.tests.test_spam.test_usuarios import Conexao


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
