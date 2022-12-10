from spam.enviador_de_email import Enviador


def test_ciar_enviar_email() :
    enviador = Enviador ()
    assert enviador is not None