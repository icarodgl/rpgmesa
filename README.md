# TRABALHO INTEGRADO: RPG de Mesa

Trabalho desenvolvido durante as disciplinas de:
- Banco de Dados 2, 
- Engenharia de Software, 
- Programação Orientada a Objetos 2,
- Projeto de Sistemas


**INTEGRANTES DO GRUPO:** 
- Eduardo Couto Rodrigues
- Ícaro Duarte Gavazza Lima
        
# Sumário


#Gerência de Requisitos

## 1	Motivação e Propósito do Sistema 
O RPG de mesa foi projetado para auxiliar os jogadores de RPG de mesa a jogarem com seus amigos sem a necessidade de se encontrar em um lugar físico, pois as seções de RPG costumam durar horas e são marcadas com certa frequência tendo problemas com os encontros. O sistema torna o jogo mais fluido e interativo mesmo com a distancia entre os usuários.

## 2	Personas

* Mestres, são os usuários que narram a história e controlam os acontecimentos do jogo.
* Jogadores, são usuários que possuem um personagem e só podem decidir as ações do mesmo.
* NPCs, são personagens controlados pelo mestre.
## 3	Minimundo  
O sistema deve auxiliar os jogadores de RPG jogar partidas online permitindo os jogadores a salvar suas fichas de personagens (nome, descrição, raça , status, ataques), a interação entre os jogadores e o jogo deve ser ditada pelo mestre onde ele decide monstros (que possuem fichas de personagens) e cenários que são imagens disponibilizadas e visualizadas por todos. Ao encontrar um inimigo o mestre permite aos jogadores que façam suas ações que serão validadas por dados jogados por eles. O jogo deve mostrar os cenários já cadastrados a uma história dando a possibilidade do mestre percorre por eles de acordo com as decisões dos jogadores.

## 4	Requisitos de Usuários
### 4.1	Requisitos Funcionais (Histórias de Usuário)
> POO2

| ID | Categoria| História de Usuário | MosCoW| Estimativa | Real| Pronto?| Sprint|
| --- | --- | --- | --- | --- | --- | --- | --- |
| RF01 | Categoria X |EU, COMO  **QUEM**, QUERO/GOSTARIA/DEVO/POSSO **O QUE**, PARA QUE/DE/PARA **PORQUE/RESULTADO**.| Must| 2 | ? | Não | -|
|RF02 | Mestre|Eu, como mestre, posso criar monstros no jogo para tonar a história mais ludica. | Must |2|?|Não|-|
|RF03 | Mestre|Eu, como mestre, posso recompensar jogadores para que eles possam evoluir no jogo. | Must|1|?|Não|-|
|RF04 | Mestre|Eu, como mestre, posso consultar as fichas dos jogadores para avaliar suas ações.| Must|1|?|Não|-|
|RF05 | Jogador|Eu, como jogador, posso criar meu personagem para usar em um jogo.| Must|2|?|Não|-|
|RF06 | Jogador|Eu, como jogador, posso cadastrar a ficha do meu personagem para caracterizar o meu personagem.| Must|1|?|Não|-|
|RF07 | Jogador|Eu, como jogador, preciso visualizar o cenário que o mestre selecionou para interagir com o jogo.| Must|5|?|Não|-|
|RF08 | Jogador|Eu, como jogador, posso escolher o inimigo a ser atacado para interagir com o jogo.| Must|5|?|Não|-|
|RF09 | Jogador|Eu, como jogador, preciso rodar um dado pra validar a minha ação.| Must|1|?|Não|-|
|RF20 | Cenário|Um cenário pré cadastrada fica disponível para outros mestres. |Would|1|?|Não|-|
|RF21 || O mestre pode selecionar e cadastrar novas versões do jogo. | Would|5|?|Não|-|
|RF22 || As fichas cadastradas devem ser disponibilizadas a outros jogadores |Would|1|?|Não|-|
|RF23 || O sistema permite sons ambientes que mudam de acordo com o cenário. |Would|2|?|Não|-|
|RF24 || O sistema permite sons para ações determinadas. |Would|2|?|Não|-|

### 4.2	Requisitos Não Funcionais
| ID |Categoria| Descrição   |    MosCoW | Estimativa Planejada | Estimativa Real|Pronto?| Sprint|Histórias relacionadas |
| --- | ------ | ------------------------- | --- | --- |--- |--- |--- |--- |
| RNF01 |Facilidade de Operação |  A entrada de dados de efetuar locação pelo atendente deverá ser realizada em no máximo 30 segundos | Must | 2 | 5| Sim| 10|RF01|
| RNF02 | Eficiência de Tempo | O tempo de resposta de efetuar locação dever ser de no máximo 2 segundos a partir da entrada correta de dados | Should | 3 | ?| Não| -|RF01 e RF02|


### 4.3	Regras de Negócio
| ID | Descrição | MosCoW | Estimativa Planejada| Estimativa Real| Pronto?| Sprint|Histórias relacionadas |
| --- | ------------------- | --- | --- | --- | --- | --- | --- |
| RN01 | Uma reserva expira quando passadas mais do que 24h de sua comunicação para o cliente. | Must |1|5|Sim|2|RF01|
| RN02 | Clientes em atraso não podem efetuar nem locações nem reservas. | Should |10|5|Sim|2|RF02|

# Desenvolvimento do Sistema
## 1.    Análise de Sistemas:
### 1.1  Subsistemas
inserir diagrama dos subsistemas UML
### 1.2  Modelagem de Casos de uso 
inserir diagramas dos Casos de Uso (UML) e descrever brevemente.

### 1.3  Modelagem Estrutural (Modelo Conceitual)
** ATENÇO: USAR Notação Entidade-Relacionamentos se estiver fazendo BD2 e o diagrama de classes se estiver fazendo Projeto de Sistemas**
![Alt text](https://github.com/discipbd2/topicos-trabalho/blob/master/sample_MC.png?raw=true "Modelo Conceitual")
### 1.4  Modelagem Comportamental
inserir principais diagramas comportamentais da análise (principalmente, estados)
### 1.5  Dicionário de Dados
[classe/entidade]: [descrição da classe]
    
    EXEMPLO:
    CLIENTE: classe/entidade que representa as informações relativas ao cliente<br>
    CPF: atributo que representa o número de Cadastro de Pessoa Física para cada cliente da empresa.<br>
    
## 2.    Projeto de Sistemas:
### 2.1  Projeto Arquitetural 
#### 2.1.1   Plataforma de Implementação e Tecnologias
descrever tecnologias usadas no sistema, justificando cada uma delas com base no contexto

#### 2.1.2   Atributos de Qualidade e Táticas
 CATEGORIAS | RNF'S | TÁTICAS | 
| --- | --- | --- |
| Facilidade de Operação | RNF03, RNF08| Prover ao usuário a capacidade de entrar com comandos que permitam operar o sistema de modo mais eficiente. Para tal, as interfaces do sistema devem permitir, sempre que possível, a entrada por meio de seleção ou leitura de código de barras ao invés da digitação de campos. | 


#### 2.1.3   Arquitetura de Software
apresentar diagrama UML da arquitetura do sistema. justificar as decisões tomadas.

### 2.2. Projeto Detalhado
OBS: repetir as seções abaixo para cada subsistema
#### 2.2.1.   Projeto da Lógica de Negócio
##### Projeto do Domínio
apresentar diagrama de classes do domínio
##### Projeto da Aplicação
apresentar diagramas de sequência e mapeamento dos casos de uso para classes
#### 2.2.2.  Projeto da Interface com Usuário
##### Projeto da Visão
apresentar protótipos de telas e diagramas de classes UML (caso realizado)
OBS: Essa visão não tem nada a ver com Views de Banco de Dados

__OBS DE BD2__: neste ponto a codificação não e necessária, somente as ideias de telas devem ser criadas, o princípio aqui é pensar na criação da interface para identificar possíveis informações a serem armazenadas ou descartadas <br>

Sugestão: https://balsamiq.com/products/mockups/<br>

![Alt text](https://github.com/discipbd2/topicos-trabalho/blob/master/balsamiq.png?raw=true "Title")
##### Projeto da Interação Humana
apresentar diagrama de classes da IU com controladores e diagrama de sequências. Apresentar diagrama com estados de navegação.
#### 2.2.3.  Projeto da Persistência de Dados
apresentar classes de acesso ao banco de dados. apresentar diagramas de sequência.

#### 2.4.   Padrões
##### Padrões Arquiteturais
##### Padrões de Projeto


No diagrama abaixo é destacado o padrão de projeto método fabrica. Ele foi utilizado para gerar diferentes tipos de objetos da Interface Acao. Sendo eles AcaoAtaque, AcaoTrocaCena e AcaoIteracao. Esse padrão facilita o entendimento das ações realizadas pelos personagens e também facilita a adição de novos tipos de ações, pelo motivo das implementações estarem isoladas.

![Alt text](https://github.com/icarodgl/rpgmesa/blob/master/Doc/FabricaAcao.PNG)



O padrão foi utilizado para resolver o problema de .....

O padrão foi utilizado para resolver o problema de .....


## 3.    Banco de Dados (BD)


### 3.1 Decisões do Projeto 
    [atributo]: [descrição da decisão]
    
    EXEMPLO:
    a) Campo endereço: em nosso projeto optamos por um campo multivalorado e composto, pois a empresa 
    pode possuir para cada departamento mais de uma localização... 
    b) justifique!


### 3.2	Modelo Lógico<br>
### 3.3	MODELO FÍSICO<br>
### 3.4	INSERT APLICADO NAS TABELAS DO BANCO DE DADOS<br>
#### 3.4.1 DETALHAMENTO DAS INFORMAÇÕES
        Detalhamento sobre as informações e processo de obtenção ou geração dos dados.
        Informar/referenciar todas as fontes usadas para:
        a) obtenção dos dados
        b) obtenção de códigos reutilizados (caso tenha feito uso destes)
        c) fontes de estudo para desenvolvimento do projeto
        
#### 3.4.2 INCLUSÃO DO SCRIPT PARA CRIAÇÃO DE TABELAS E INSERÇÃO DOS DADOS (ARQUIVO ÚNICO COM):
        a) inclusão das instruções para criação das tabelas e estruturas de amazenamento do BD
        b) inclusão das instruções de inserção dos dados nas referidas tabelas
        c) inclusão das instruções para execução de outros procedimentos necessários
        d) estes dados serão utilizados como exemplo nas consultas e views e portanto devem ter 
        informações pertinentes e consistentes (não devem ser gerados aleatoriamente)
        

### 3.5	TABELAS E PRINCIPAIS CONSULTAS<br>
#### 3.5.1	GERACAO DE DADOS (MÍNIMO DE 1,5 MILHÃO DE REGISTROS PARA PRINCIPAL RELAÇAO)<br>
    Estes dados podem ser gerados de modo aleatório por funções de geração de dados, 
    mas devem possuir uma petinência mínima com os atributos aos quais pertencem.
<br>
OBS: Incluir para os tópicos 3.5.2 e 3.5.3 as instruções SQL + imagens (print da tela) mostrando os resultados.<br>

#### 3.5.2	SELECT DAS TABELAS COM PRIMEIROS 10 REGISTROS INSERIDOS<br> 
    Esta atividade deve incluir todas as tabelas existentes no sistema
<br>

#### 3.5.3	SELECT DAS VISÕES COM PRIMEIROS 10 REGISTROS<br>
    a) Descrição da view sobre que grupos de usuários (operacional/estratégico) <br>
    e necessidade ela contempla.
    b) Descrição das permissões de acesso e usuários correlacionados (após definição <br>
    destas características)
    c) Devem ser criadas no mínimo 5 views
    d) Estas vises devem refletir os principais relatórios que serão fornecidos pelo sistema
    Data de Entrega: (Data a ser definida)
<br>

#### 3.5.4	LISTA DE CODIGOS DAS FUNÇÕES, ASSERÇOES E TRIGGERS<br>
        Detalhamento sobre funcionalidade de cada código.
        a) Objetivo
        b) Código do objeto (função/trigger/asserção)
        c) exemplo de dados para aplicação
        d) resultados em forma de tabela/imagem
        e) Mínimo de 2 funções, 2 asserções e 2 triggers (6 no mínimo)
<br>

#### 3.5.5	Administração do banco de dados<br>
        Descrição detalhada sobre como serão executadas no banco de dados as <br>
        seguintes atividades.
        a) Segurança e autorização de acesso:
        b) Estimativas de aquisição de recursos para armazenamento e processamento da informação
        c) Planejamento de rotinas de manutenção e monitoramento do banco
        d) Plano com frequencia de análises visando otimização de performance
<br>

#### 3.5.6	Backup do Banco de Dados<br>
     Detalhamento do backup.
     a) Tempo
     b) Tamanho
     c) Teste de restauração (backup)
     d) Tempo para restauração
     e) Teste de restauração (script sql)
     f) Tempo para restauração (script sql)
<br>

#### 3.5.7	APLICAÇAO DE ÍNDICES E TESTES DE PERFORMANCE<br>
    a) Lista de índices, tipos de índices com explicação de porque foram implementados
    b) Performance esperada VS Resultados obtidos
    c) Tabela de resultados comparando velocidades antes e depois da aplicação dos índices
    d) Incluir nas explicações imagens e tuplas do analyse postgres
    e) Mínimo de 5 análises nas principais tabelas
<br>

#### 3.5.8	ANÁLISE DOS DADOS COM ORANGE<br>    
    a) aplicação de algoritmos e interpretação dos resultados
    b) o método utilizado para paresentação dos dados deve ser comparado com o exemplo padrão do Orange
        (ex: Tree Decision usa dataset Iris, Sieve diagram usa dataset Titanic, K-means usa dataset Iris, etc...)
    c) devem ser apresentadas no mínimo 4 análises.

### 3.6	ATUALIZAÇÃO DA DOCUMENTAÇÃO/ SLIDES E ENTREGA FINAL<br>
<br>
    Data de Entrega: (Data a ser definida)
<br>

### 3.7	DIFICULDADES ENCONTRADAS PELO GRUPO<br>  

# Gestão de Configuração
## 1.    Metodologia
descrever metodologias e políticas que serão usadas para realizar a gestão de configuração como, por exemplo, Gitflow, rastreabilidade de requisitos e mudanças. É necessário descrever em detalhes os procedimentos.
## 2.    Arquitetura
descrever ferramentas e a integração dessas para a arquitetura. 
## 3.    Integração Contínua e Delivery Contínua
Descrever como será aplicado esses conceitos.

# Gestão de Projetos
## 1.    Project Model Canvas (PMC)
Visão geral do projeto.
## 2.    Cronograma macro de sprints 
datas dos sprints.
## 3.    Backlog de histórias de Usuário 
lista de histórias de usuário categorizadas, priorizadas e com o esforço. A categorização deve utilizar a técnica MoSCoW. 
Acompanhamento do projeto: o grupo deve apresentar histórico, por sprint,  do acompanhamento do projeto da seguinte forma:
- Apresentando o Burndown do projeto.
- Apresentando a velocidade do time.
- Modificações do backlog.
## 4.    Burn down dos sprints
acompanhamento dos sprints. Cada Sprint deve ter uma seção descrevendo o que foi realizado e o planejado (por meio do  o gráfico e Burndown do Sprint).
## 5.    Retrospectiva 
Apresentar a retrospectiva da equipe do sprint realizado.

# Gerência de Qualidade
## 1.    Métricas de qualidade 
definir métricas de qualidade para cada artefato do projeto como, por exemplo, quantidade de codesmell, complexidade ciclomática e outras. 
## 2.    Classes de equivalência e particionamento de equivalência 
*** Defina as classes de equivalências para as métricas de qualidade. ***

| Entrada | Classe de Equivalência| Tipo de Classe de Equivalência| 
| --- | --- | --- | 
| Valor | valor é um valor monetário entre 0,00 e 1.710,78 |Válida
| Valor | valor é um valor monetário entre 1.710,79 e 2.563,91  |Válida
| Valor | valor é um valor monetário entre 2.563,92 e 3.418,59 |Válida
| Valor | valor é um valor monetário entre 3.418,59 e 4.271,59  |Válida
| Valor | valor é um valor monetário maior do que 4.271,59  |Válida
| Valor | valor não é um valor monetário | inválida
| Valor | valor é um valor monetário menor do que 0 |inválida


## 3.    Medição 
seção que descreve com será feita a medição das métricas. Essa seção deve ser atualizada por sprint. 
## 4.    Testes
***Técnicas utilizadas para os testes: apresentar as técnicas utilizadas para o planejamento e execução de testes como, por exemplo, teste funcional sistemático e testes estruturais.***

## 5.    Cenário de Teste
apresentar todos os cenários de teste sucesso e falhas das histórias de usuário.  


## 6.    Histórico  
O grupo deve apresentar a evolução da qualidade dos itens ao longo das entregas, ou seja, em outras palavras, o grupo deve apresentar o histórico de evolução da qualidade dos artefatos de software e discursar o motivo da evolução.

# Diário de Bordo

o grupo deve apresentar semanalmente um relato da atividade do grupo. O relato pode conter qualquer tipo de informação (fotos, vídeos) que possam auxiliar no entendimento das atividades do grupo. 

OBS: organize o diário para que não se misture com a documentação. de preferência, coloque-o em outra página.

**FORMATACAO NO GIT:** https://help.github.com/articles/basic-writing-and-formatting-syntax/
