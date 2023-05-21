from libpypro.spam.enviador_de_email import Enviador


def test_envio_de_span ():
    enviador_de_span = EnviadorDeSpan(Sessao, Enviador())
    enviador_de_span.enviar_emails()
