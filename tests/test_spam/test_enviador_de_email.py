from spam.enviador_de_email import Enviador


def test_ciar_enviar_email() :
    enviador = Enviador ()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    enviador.enviar(
        'adilsom.garcia2006@hotmail.com',
    'rosana.garcia2009@gmail.com.br',
    'Título: Viagem para as barramas',
    'Passagens de 1ª classe já compradas.')
