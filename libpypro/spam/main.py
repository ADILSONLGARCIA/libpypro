class EnviadorDeSpan:
    def __init__(self, sessao: object, enviador: object) -> object:
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, titulo, corpo):
        for user in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                titulo,
                corpo
            )


class EnviadorDeSpan :
    pass
