import operacoes;

op = operacoes.Operacoes();

def imprimirTela():
    op = operacoes.Operacoes();
    print("=====================================================================");
    print("\nMENU DE FUNCIONALIDADES\n");
    statusLista = op.verificarLista();
    if statusLista: print("1. Ler Pontos de Coleta\n2. Cadastrar Pontos\n3. Atualizar Informações\n4. Excluir Ponto de Coleta\n5. Sair");
    else:
        print("No momento, não há nenhum Ponto de Coleta cadastrado.")
        print("2. Cadastrar Pontos\n5. Sair");

def atribuirValores():
    op.tituloColeta     = str(input("\nDigite o Título da Coleta: "));
    op.pontoColeta      = str(input("Número do Ponto: "));
    op.dataCriacao      = str(input("Data de criação: "));
    op.nomeCidadao      = str(input("Nome do Cidadão responsável: "));
    op.descricaoColeta  = str(input("Descrição: "));
    op.status           = str(input("Informe o Status do Ponto de Coleta: "));
    print(f'''\nInformações do cadastro: Título do Ponto: {op.tituloColeta}, Número do ponto: {op.pontoColeta}, Data de criação: {op.dataCriacao}, Responsável: {op.nomeCidadao}, Descrição: {op.descricaoColeta}, Status: {op.status}''');

if(__name__=="__main__"):

    operar = int(0);

    while(operar != 5):
        imprimirTela();
        try:
            operar = int(input("\nEscolha a funcionalidade: "));
            match operar:
                case 1:
                    print("1. Ler cadastros...");
                    statusLista = op.verificarLista();
                    op.ler();

                case 2:
                    print("2. Cadastrar Ponto de Coleta:");
                    atribuirValores();
                    op.cadastrar();
                    confirmar = op.pesquisar();
                    if confirmar: print("Cadastrado com sucesso!");
                    else: print("Não foi possível cadastrar esse Ponto de Coleta! Por favor, tente novamente.");

                case 3:
                    statusLista = op.verificarLista();
                    if statusLista:
                        print("Atualizar Ponto de Coleta:");
                        op.ler();
                        idRegistro = str(input("Informe o ID do Ponto de Coleta: "));
                        resultadoPesquisa = op.pesquisarID(idRegistro);
                        while resultadoPesquisa == False:
                            print("Este Ponto de Coleta não está cadastrado! Tente novamente.");
                            idRegistro = str(input("Informe o ID do Ponto de Coleta: "));
                            resultadoPesquisa = op.pesquisarID(idRegistro);
                        for i in resultadoPesquisa: print(f'''ID: {i[0]}, Título do Ponto: {i[1]}, Nome do Ponto: {i[2]}, Data de Criação: {i[3]}, Nome do Responsável: {i[4]}, Descrição: {i[5]}, Status: {i[6]}''');
                        print("\n");
                        atribuirValores();
                        op.atualizar(idRegistro);
                        confirmar = op.pesquisarID(idRegistro);
                        if confirmar: print("Atualizado com sucesso!");
                        else: print("Não foi possível atualizar os dados do Ponto de Coleta!");
                    else: print("Operação Inválida! Não há alunos cadastrados no sistema!");
                case 4:
                    statusLista = op.verificarLista();
                    if statusLista:
                        print("4. Deletar Ponto de Coleta:");
                        op.ler();
                        idRegistro = str(input("Informe o ID do Ponto de Coleta: "));
                        resultadoPesquisa = op.pesquisarID(idRegistro);
                        while resultadoPesquisa == False:
                            print("Este Ponto de Coleta não está cadastrado! Tente novamente.");
                            idRegistro = str(input("Informe o ID do Ponto de Coleta: "));
                            resultadoPesquisa = op.pesquisarID(idRegistro);
                        for i in resultadoPesquisa: print(f'''ID: {i[0]}, Título do Ponto: {i[1]}, Nome do Ponto: {i[2]}, Data de Criação: {i[3]}, Nome do Responsável: {i[4]}, Descrição: {i[5]}, Status: {i[6]}''');
                        print("\n");
                        confirmar = int(0);
                        while confirmar < 1 or confirmar > 2:
                            confirmar = int(input("Tem certeza que deseja excluir o registro?\n1. Sim\n2. Não, cancelar: "));
                            match confirmar:
                                case 1: 
                                    op.deletar(idRegistro);
                                    print("Ponto de Coleta excluído com sucesso!");
                                case 2: print("Exclusão de ponto de coleta cancelada com sucesso...");
                                case _: print("Operação inválida! Tente novamente.");
                    else: print("Operação Inválida! Não há alunos cadastrados no sistema!");
                case 5: print("5. Sistema finalizado com sucesso!");
                case _: print("ERRO: Esta funcionalidade não existe. Tente novamente.");
        except ValueError:
            print("Por favor, digite apenas números...");