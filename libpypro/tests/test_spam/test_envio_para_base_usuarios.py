from libpypro.spam.enviador_de_email import Enviador
from libpypro.spam.main import EnviadorDeSpan


def test_envio_de_spam(sessao):
    enviador_de_span = EnviadorDeSpan(sessao, Enviador() )
    enviador_de_span.enviar_emails(
        'adilson.garcia2006@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
