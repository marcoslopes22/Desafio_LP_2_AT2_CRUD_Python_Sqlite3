class OportunidadesColeta:
    
    __tituloColeta = str("");
    __pontoColeta = str("");
    __dataCriacao = str("");
    __nomeCidadao = str("");
    __descricaoColeta = str("");
    __status = str("");

    # TituloColeta;
    def getTituloColeta(self):
        return self.__tituloColeta;

    def setTitutloColeta(self,tituloColeta):
        self.__tituloColeta = tituloColeta;

    # PontoColeta;
    def getPontoColeta(self):
        return self.__pontoColeta;

    def setPontoColeta(self,pontoColeta):
        self.__pontoColeta = pontoColeta;
    
    # Data Criacao;
    def getDataCriacao(self):
        return self.__dataCriacao;

    def setDataCriacao(self,dataCriacao):
        self.__dataCriacao = dataCriacao;
    
    # NomeColeta;
    def getNomeCidadao(self):
        return self.__nomeCidadao;

    def setNomeCidadao(self,nomeCidadao):
        self.__nomeCidadao = nomeCidadao;

    # DescricaoColeta;
    def getDescricaoColeta(self):
        return self.__descricaoColeta;

    def setDescricaoColeta(self,descricaoColeta):
        self.__descricaoColeta = descricaoColeta;
    
    # Status;
    def getStatus(self):
        return self.__status;

    def setStatus(self,status):
        self.__status = status;