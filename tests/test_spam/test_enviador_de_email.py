import pytest

from spam.enviador_de_email import Enviador, EmailInvalido


def test_ciar_enviador_de_email() :
    enviador = Enviador ()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['adilson.garcia2006@hotmail.com',
    'rosana.garcia2009@gmail.com.br'])

def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'adilson.garcia2006@hotmail.com',
        'Título: Viagem para as barramas',
        'Passagens de 1ª classe já compradas.'
        )
    assert destinatario in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'adilson.garcia2006@hotmail.com']
)

def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'rosana.garcia2006@hotmail.com',
            'Título: Viagem para as barramas',
            'Passagens de 1ª classe já compradas.'
            )
        assert remetente in resultado
