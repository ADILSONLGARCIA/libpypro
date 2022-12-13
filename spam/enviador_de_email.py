class Enviador :
    def enviar(self, remetente, destinatario, titulo, corpo) :
        if '@' not in remetente :
            raise EmailInvalido ( f'Email do remetente invalido {remetente}' )
        return remetente


class EmailInvalido ( Exception ) :
    pass
