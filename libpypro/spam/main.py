class EnviadorDeSpan:
    def __init__(self, sessao: object, enviador: object) -> object:
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, corpo, usuario):
        for user in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                usuario.email,
                assunto,
                corpo
            )
