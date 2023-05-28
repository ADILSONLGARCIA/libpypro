import pytest

from libpypro.spam.enviador_de_email import Enviador
from libpypro.spam.main import EnviadorDeSpan
from libpypro.tests.test_spam.test_usuarios import Usuario


def test_envio_de_spam(sessao):
    enviador_de_span = EnviadorDeSpan(sessao, Enviador() )
    enviador_de_span.enviar_emails(
        'adilson.garcia2006@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )


@pytest.mark.parametrize(
    'usuarios',
    [
        Usuario(nome='Adilson', email='adilson.garcia2006@hotmail.com'),
        Usuario(nome='Rosana', email='rosana.garcia2009@gmail.com.br')
    ],
    [
        Usuario(nome='Adilson', email='adilson.garcia2006@hotmail.com')
    ]
)


def test_qtde_de_spam(sessao, usuarios, enviar=0):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador_de_span = EnviadorDeSpan(sessao, Enviador() )
    enviador_de_span.enviar_emails(
        'adilson.garcia2006@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == Enviador.qtd_email_enviados

