def test_salvar_usuario():
    # etapa de setup
    conexao = Conexao() # responsável por gerar a autenticação do banco, como login e senha do bd para poder se conectar.
    sessao = conexao.sessao() # serve para efetuar as alterações no bd, como salvamento, buscas, etc...
    usuario=Usuario(nome='Adilson') # criando um usuario
    sessao.salvar(usuario) # salva o usuario no bd
    assert isinstance(usuario.id, int) # certifica se o usuario foi salvo com um id numerico
    # etapa de fear down
    sessao.roll_back() # roll_back desfaz todas as alterações feitas no ambiente de teste
    sessao.fechar()
    conexao.fechar() # apos interagir com a conexão sw faz necessario fechar a sessao e conexao


def test_listar_usuarios():
    # etapa de setup
    conexao = Conexao() # responsável por gerar a autenticação do banco, como login e senha do bd para poder se conectar.
    sessao = conexao.sessao() # serve para efetuar as alterações no bd, como salvamento, buscas, etc...
    usuarios=[Usuario(nome='Adilson'), Usuario(nome='Rosana')] # criando um usuario
    for usuario in usuarios:
        sessao.salvar(usuario) # salva os usuarios no bd
    assert usuario == sessao.listar() # asserção onde certifica que a lista de usuarios que acabamos de salvar será retornada como uma sessao chamamos o metodo listar de uma sessao foi salvo com um id numerico
    # etapa de fear down
    sessao.roll_back() # roll_back desfaz todas as alterações feitas no ambiente de teste
    sessao.fechar()
    conexao.fechar() # apos interagir com a conexão sw faz necessario fechar a sessao e conexao
