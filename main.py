import oportunidadesColeta;
import operacoes;

def imprimirTela():
    op = operacoes.Operacoes();
    print("=====================================================================");
    print("\nMENU DE FUNCIONALIDADES\n");
    statusLista = op.verificarLista();
    if statusLista: print(
        '''1. Ler Pontos de Coleta
        \n2. Cadastrar Pontos
        \n3. Atualizar Informações
        \n4. Excluir Ponto de Coleta
        \n5. Sair''');
    else: print("1. Ler Pontos de Coleta\n2. Cadastrar Pontos\n5. Sair");

if(__name__=="__main__"):

    operar = int(0);

    while(operar != 5):
        op = operacoes.Operacoes();
        oc = oportunidadesColeta.OportunidadesColeta();
        imprimirTela();
        try:
            operar = int(input("\nEscolha a funcionalidade: "));
            match operar:
                case 1:
                    print("1. Ler cadastros...");
                    statusLista = op.verificarLista();
                    if statusLista: op.ler();
                    else: print("\nNo momento não há Pontos de Coleta cadastrados no sistema!");

                case 2:
                    print("2. Cadastrar Ponto de Coleta:");
                    tituloColeta     = str(input("\nDigite o Título da Coleta: "));
                    pontoColeta      = str(input("Digite o Número do Ponto de Coleta: "));
                    dataCriacao      = str(input("Digite a Data de criação do Ponto de Coleta:"));
                    nomeCidadao      = str(input("Digite o Nome do Cidadão responsável pelo Ponto de Coleta:"));
                    descricaoColeta  = str(input("Digite uma Descrição para o Ponto de Coleta:"));
                    status           = str(input("Informe o Status do Ponto de Coleta:"));
                    oc.setTituloColeta(tituloColeta);
                    oc.setPontoColeta(pontoColeta);
                    oc.setDataColeta(dataCriacao);
                    oc.setNomeCidadao(nomeCidadao);
                    oc.setDescricaoColeta(descricaoColeta);
                    oc.setStatus(status);
                    print(
                        f'''\nInformações do ponto: {oc.tituloColeta},
                        Número do ponto: {oc.pontoColeta},
                        Data de criação: {oc.dataCriacao},
                        Responsável: {oc.nomeCidadao},
                        Descrição: {oc.descricaoColeta},
                        Status: {oc.status}''');
                    op.cadastrar(
                        oc.tituloColeta,
                        oc.pontoColeta,
                        oc.dataCriacao,
                        oc.nomeCidadao,
                        oc.descricaoColeta,
                        oc.status);
                    confirmar = op.pesquisar(
                        oc.tituloColeta,
                        oc.pontoColeta,
                        oc.dataCriacao,
                        oc.nomeCidadao,
                        oc.descricaoColeta,
                        oc.status);
                    if confirmar: print("Cadastrado com sucesso!");
                    else: print("Não foi possível cadastrar esse aluno!");

                case 3:
                    statusLista = op.verificarLista();
                    if statusLista:
                        print("Atualizar Ponto de Coleta:");
                        op.ler();
                        idRegistro  = str(input("Informe o Id de registro: "));
                        resultadoPesquisa = op.pesquisarID(idRegistro);
                        while resultadoPesquisa == False:
                            print("Id de registro não está cadastrado! Tente novamente.");
                            idRegistro = str(input("Informe o Id de registro: "));
                            resultadoPesquisa = op.pesquisarID(idRegistro);
                        for i in resultadoPesquisa:
                            print(f'''
                                Registro encontrado: 
                                ID: {i[0]},
                                Título: {i[1]},
                                Ponto: {i[2]},
                                Data: {i[3]},
                                Nome: {i[4]},
                                Descrição: {i[5]},
                                Status: {i[6]}''');
                        print("\n");
                        tituloColeta     = str(input("\nDigite o Título da Coleta: "));
                        pontoColeta      = str(input("Digite o Número do Ponto de Coleta: "));
                        dataCriacao      = str(input("Digite a Data de criação do Ponto de Coleta:"));
                        nomeCidadao      = str(input("Digite o Nome do Cidadão responsável pelo Ponto de Coleta:"));
                        descricaoColeta  = str(input("Digite uma Descrição para o Ponto de Coleta:"));
                        status           = str(input("Informe o Status do Ponto de Coleta:"));
                        oc.setTituloColeta(tituloColeta);
                        oc.setPontoColeta(pontoColeta);
                        oc.setDataCriacao(dataCriacao);
                        oc.setNomeCidadao(nomeCidadao);
                        oc.setDescricaoColeta(descricaoColeta);
                        oc.setStatus(status);
                        print(f'''
                            \nInformações do ponto: {oc.tituloColeta},
                            Número do ponto: {oc.pontoColeta},
                            Data de criação: {oc.dataCriacao},
                            Responsável: {oc.nomeCidadao},
                            Descrição: {oc.descricaoColeta},
                            Status: {oc.status}''');
                        op.atualizar(
                            idRegistro,
                            oc.tituloColeta,
                            oc.pontoColeta,
                            oc.dataCriacao,
                            oc.nomeCidadao,
                            oc.descricaoColeta,
                            oc.status);
                        confirmar   = op.pesquisar(
                            idRegistro,
                            oc.tituloColeta,
                            oc.pontoColeta,
                            oc.dataCriacao,
                            oc.nomeCidadao,
                            oc.descricaoColeta,
                            oc.status);
                        if confirmar: print("Atualizado com sucesso!");
                        else: print("Não foi possível cadastrar esse aluno!");
                    else: print("Operação Inválida! Não há alunos cadastrados no sistema!");
                case 4:
                    statusLista = op.verificarLista();
                    if statusLista:
                        print("4. Deletar Ponto de Coleta:");
                        op.ler();
                        idRegistro = str(input("Informe o Id de registro: "));
                        resultadoPesquisa = op.pesquisarID(idRegistro);
                        while resultadoPesquisa == False:
                            print("Id de registro não está cadastrado! Tente novamente.");
                            idRegistro = str(input("Informe o Id de registro: "));
                            resultadoPesquisa = op.pesquisarID(idRegistro);
                        for i in resultadoPesquisa:
                            print(f'''
                                Registro encontrado: 
                                ID: {i[0]},
                                Título: {i[1]},
                                Ponto: {i[2]},
                                Data: {i[3]},
                                Nome: {i[4]},
                                Descrição: {i[5]},
                                Status: {i[6]}''');
                        print("\n");
                        confirmar = int(0);
                        while confirmar < 1 and confirmar > 2:
                            confirmar = int(input("Tem certeza que deseja excluir o registro?\n1. Sim\n2. Não, cancelar: "));
                            match confirmar:
                                case 1: 
                                    op.deletar(idRegistro);
                                    print("Ponto de coleta excluído com sucesso!");
                                case 2: print("Exclusão de ponto de coleta cancelada com sucesso...");
                                case _: print("Operação inválida! Tente novamente.");
                    else: print("Operação Inválida! Não há alunos cadastrados no sistema!");
                case 5: print("5. Saindo do sistema...");
                case _: print("ERRO: Esta funcionalidade não existe. Tente novamente.");
        except:
            print("Por favor, escolha somente números.");