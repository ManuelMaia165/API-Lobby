# API Game com Flask

## Requisitos

```
    Python 3 ou superior
    pip
    Flask
        Flask-Cors
        Flask-Marshmallow
        Flask-SqlAlchemy
    MySQL
```
## Models da aplicação
---

- ### Alternative
    A classe `Alternative` herda de `db.Model`, que é uma classe do `Flask-SQLAlchemy`, um módulo que fornece uma interface para trabalhar com bancos de dados SQL usando o `Flask`.

    A classe possui três atributos:

    - `id`: é um campo inteiro que representa o identificador único de cada alternativa. É definido como uma chave primária e é gerado automaticamente pelo banco de dados (autoincrement).

    - `question_id`: é um campo inteiro que armazena o identificador da pergunta a qual a alternativa pertence. É definido como uma chave estrangeira e não pode ser nulo.

    - `text`: é um campo de string que armazena o texto da alternativa. Não pode ser nulo.
    
    A classe `AlternativeSchema` é um esquema de serialização/deserialização que é usado para converter objetos da classe `Alternative` para um formato que pode ser facilmente convertido para JSON e vice-versa. Ela é usada pelo módulo `Flask-Marshmallow` para facilitar essa conversão. O esquema define os campos que devem ser incluídos na serialização/deserialização, que são os mesmos atributos da classe `Alternative`.

    Por fim, as variáveis `alternative_schema` e `alternative_schema_schema` são instâncias do esquema de serialização/deserialização, sendo a primeira para trabalhar com uma única alternativa e a segunda para trabalhar com uma lista de alternativas.

- ### Lobby
    Este código define uma classe chamada `Lobby` que representa um lobby em uma aplicação. A classe Lobby é uma subclasse de `db.Model`, que é uma classe fornecida por uma biblioteca chamada `Flask-SQLAlchemy`. Isso indica que a classe `Lobby` é um modelo que será armazenado em um banco de dados usando o `Flask-SQLAlchemy`.

    A classe `Lobby` tem várias variáveis de classe, cada uma das quais representa uma coluna na tabela do banco de dados que armazenará instâncias da classe `Lobby`. As variáveis são decoradas com `db.Column`, o que especifica o tipo da coluna e quaisquer opções adicionais para a coluna.

    O método `__init__` é um método especial em classes Python que é chamado quando uma instância da classe é criada. Ele é usado para inicializar os atributos da instância. Neste caso, o método `__init__` recebe cinco argumentos: user, max_player, tema, tempo e status. Esses argumentos são usados para definir os valores dos atributos correspondentes da instância `Lobby`.

    A classe `LobbySchema` é uma subclasse de `ma.Schema`, que é uma classe fornecida por uma biblioteca chamada `Marshmallow`. Ela é usada para definir um esquema para serializar e desserializar instâncias da classe `Lobby` para e de formato `JSON`. A classe interna `Meta` especifica os campos que devem ser incluídos no esquema.

    Finalmente, duas variáveis são definidas no final do código: `lobby_schema` e `lobbys_schema`. Essas variáveis são instâncias da classe `LobbySchema` e são usadas para serializar e desserializar instâncias individuais de `Lobby` e listas de instâncias de `Lobby`, respectivamente.

- ### Player
    Este código define uma classe chamada `Player` que representa um jogador em uma aplicação. A classe Player é uma subclasse de `db.Model`, que é uma classe fornecida por uma biblioteca chamada `Flask-SQLAlchemy`. Isso indica que a classe `Player` é um modelo que será armazenado em um banco de dados usando o `Flask-SQLAlchemy`.

    A classe `Player` tem várias variáveis de classe, cada uma das quais representa uma coluna na tabela do banco de dados que armazenará instâncias da classe `Player`. As variáveis são decoradas com `db.Column`, o que especifica o tipo da coluna e quaisquer opções adicionais para a coluna.

    O método `__init__` é um método especial em classes Python que é chamado quando uma instância da classe é criada. Ele é usado para inicializar os atributos da instância. Neste caso, o método `__init__` recebe um número arbitrário de argumentos de palavra-chave usando a sintaxe `**kwargs`. Esses argumentos são passados para o método `__init__` da classe pai usando a função `super()`.

    A classe `PlayerSchema` é uma subclasse de `ma.Schema`, que é uma classe fornecida por uma biblioteca chamada `Marshmallow`. Ela é usada para definir um esquema para serializar e desserializar instâncias da classe `Player` para e de formato `JSON`. A classe interna `Meta` especifica os campos que devem ser incluídos no esquema.

    Finalmente, duas variáveis são definidas no final do código: `player_schema` e `player_schema_schema`. Essas variáveis são instâncias da classe `PlayerSchema` e são usadas para serializar e desserializar instâncias individuais de `Player` e listas de instâncias de `Player`, respectivamente.

- ### Question
    Este código define uma classe chamada `Question` que é usada para representar uma questão em um aplicativo. A classe `Question` é derivada da classe `db.Model`, que é parte de uma biblioteca chamada `Flask-SQLAlchemy`. Isso significa que a classe `Question` é uma tabela do banco de dados e cada instância da classe é uma linha na tabela.

    A classe `Question` tem três atributos: `id`, `text` e `correct_answer`. O atributo `id` é uma chave primária da tabela e é um número inteiro que é gerado automaticamente pelo banco de dados.
    
    O atributo `text` é o texto da questão e o atributo `correct_answer` é a resposta correta para a questão.
    
    Além disso, há um atributo chamado `theme` que representa o tema da questão.

    O código também define uma classe chamada `QuestionSchema`, que é derivada da classe `ma.Schema` da biblioteca `Flask-Marshmallow`. A classe `QuestionSchema` é usada para serializar instâncias da classe Question em um formato que possa ser facilmente convertido em `JSON` e enviado pela rede. A classe `QuestionSchema` tem um atributo chamado `fields` que especifica quais atributos da classe `Question` devem ser incluídos na serialização.

    Por fim, o código cria duas instâncias da classe `QuestionSchema`: `question_schema` e `question_schemas`. A primeira é usada para serializar uma única instância da classe `Question`, enquanto a segunda é usada para serializar uma lista de instâncias da classe `Question`.

## Views da aplicação
---
- ### Alternative
    Este código define uma classe chamada `AlternativeController` que tem um método chamado `get_alternatives_by_question_id`. Esse método é usado para recuperar todas as alternativas de uma questão específica de um banco de dados.

    A classe `AlternativeController` depende de três outras classes: `Alternative`, `AlternativeSchema` e `alternative_schema_schema`. A classe `Alternative` é usada para representar uma alternativa em um aplicativo. A classe `AlternativeSchema` é usada para serializar instâncias da classe `Alternative` em um formato que possa ser facilmente convertido em `JSON` e enviado pela rede. A classe `alternative_schema_schema` é uma instância da classe `AlternativeSchema` que é usada para serializar uma única instância da classe `Alternative`.

    O método `get_alternatives_by_question_id` começa recuperando todas as alternativas para a questão com o ID especificado. Isso é feito usando o método `query` da sessão do banco de dados e o método `filter` do objeto `query`. O método `filter` é usado para especificar que somente as alternativas cujo atributo `question_id` corresponda ao ID da questão devem ser incluídas na consulta. O método `all` é usado para recuperar todas as alternativas que correspondem aos critérios da consulta.

    Por fim, o método `get_alternatives_by_question_id` retorna a lista de alternativas recuperadas.

- ### Game
    Este código define uma classe chamada `Game` que é usada para representar um jogo em um aplicativo. A classe `Game` tem vários métodos que são usados para gerenciar o fluxo de um jogo, incluindo métodos para iniciar um jogo, iniciar uma rodada, encerrar uma rodada e encerrar um jogo.

    O construtor da classe `Game` aceita vários parâmetros, incluindo o ID do lobby em que o jogo está sendo jogado, o número de rodadas do jogo e o tema do jogo. O construtor também aceita um parâmetro opcional chamado host, que é o endereço do servidor `RabbitMQ` que será usado para enviar e receber mensagens durante o jogo.

    O método `start` é usado para iniciar um jogo com um determinado tema. O método começa recuperando uma lista de perguntas aleatórias do banco de dados para o tema especificado. Em seguida, o método recupera as alternativas para cada pergunta e armazena essas perguntas e alternativas em atributos da classe `Game`. Por fim, o método `start_round` é chamado para iniciar a primeira rodada do jogo.

    O método `start_round` é usado para iniciar uma nova rodada do jogo. Ele recupera uma pergunta aleatória do banco de dados e as alternativas para essa pergunta. Em seguida, cria uma nova instância da classe Round com essa pergunta e alternativas e armazena essa instância em um atributo da classe `Game`.

    O método `end_round` é usado para encerrar uma rodada do jogo. Ele atualiza a pontuação de cada jogador com base nas respostas dadas durante a rodada e, em seguida, envia a pontuação atualizada para todos os jogadores. Se ainda houver rodadas, o método `start_round` é chamado para iniciar a próxima rodada. Caso contrário, o método `finish_game` é chamado para encerrar o jogo.

    O método `_send_question` é usado para enviar uma pergunta para os jogadores durante uma rodada. Ele usa uma instância da classe `RabbitMQClient` para conectar-se ao servidor `RabbitMQ` e enviar a pergunta como uma mensagem.

    O método `_send_ranking` é usado para enviar o ranking atualizado para os jogadores após o término de uma rodada. Ele usa a mesma instância da classe `RabbitMQClient` para conectar-se ao servidor `RabbitMQ` e enviar o ranking atualizado da rodada como uma mensagem.

- ### Lobby
    Este código define uma classe chamada `LobbyController` que é usada para gerenciar os lobbys em um aplicativo. A classe `LobbyController` tem vários métodos que são usados para criar, atualizar, obter e excluir lobbys no banco de dados.

    O método `create_lobby` é usado para criar um novo lobby. Ele recupera os dados da requisição `HTTP` e usa esses dados para criar uma nova instância da classe `Lobby`. Em seguida, adiciona a instância ao banco de dados e retorna a instância criada.

    O método `update_lobby` é usado para atualizar um lobby existente. Ele recupera o lobby com o ID especificado e, em seguida, atualiza os campos do lobby com os dados da requisição `HTTP`.

    O método `get_lobby` é usado para recuperar um lobby específico do banco de dados. Ele recupera o lobby com o ID especificado e, em seguida, retorna o lobby.

    O método `get_all_lobbys` é usado para recuperar todos os lobbys do banco de dados. Ele recupera todos os lobbys e retorna a lista de lobbys.

    O método `delete_lobby` é usado para excluir um lobby do banco de dados. Ele recupera o lobby com o ID especificado e, em seguida, exclui o lobby do banco de dados.

    O método `finish_game` é usado para finalizar um jogo em um lobby. Ele recupera o lobby com o ID especificado e, em seguida, atualiza o status do lobby para 0 (__finalizado__).

- ### Player
    Esse código é uma classe em Python que representa um controlador de jogadores. Ele contém métodos para `criar`, `atualizar`, `obter`, `excluir` e `atualizar` a pontuação de jogadores, bem como para obter todos os jogadores de um determinado lobby.

    O método `join_lobby` permite que um jogador se junte a um lobby especificado, criando um novo jogador no banco de dados com os dados obtidos da requisição. O método `get_player_by_lobby` retorna o jogador associado a um determinado lobby. O método `get_players_by_lobby` retorna todos os jogadores associados a um determinado lobby. O método `leave_lobby` permite que um jogador saia de um lobby especificado, excluindo o jogador do banco de dados. O método `update_score` atualiza a pontuação de um determinado jogador associado a um determinado lobby.

- ### Question
    Esse código é uma classe em Python que representa um controlador de perguntas. Ela contém dois métodos:

    `get_all_questions`: esse método retorna todas as perguntas do banco de dados.

    `get_random_question_by_theme`: esse método retorna uma pergunta aleatória do banco de dados filtrada pelo tema especificado como parâmetro. Ele usa uma consulta do `SQLAlchemy` para selecionar todas as perguntas com o tema especificado e ordená-las de forma aleatória, e retorna apenas a primeira pergunta da lista ordenada aleatoriamente.

    Os métodos dessa classe fazem uso de três objetos importados de `app.models.question`: `Question`, `QuestionSchema` e `question_schemas`. Question é uma classe que representa uma pergunta no banco de dados, `QuestionSchema` é um esquema de serialização/deserial.

- ### RabbitMQ
    O código acima define a classe `RabbitMQClient`, que é um cliente para se conectar a um servidor `RabbitMQ` e enviar mensagens através dele. A classe tem três métodos: `connect`, que estabelece uma conexão com o servidor `RabbitMQ`; `close_connection`, que fecha a conexão com o servidor; e `send_message`, que envia uma mensagem para o servidor `RabbitMQ`.

    O método `connect` cria uma conexão com o servidor `RabbitMQ` através da biblioteca `pika`, utilizando os parâmetros de conexão especificados (__no caso, o endereço do host__). Em seguida, cria um canal de comunicação através da conexão estabelecida.

    O método `close_connection` fecha a conexão com o servidor `RabbitMQ`.

    O método `send_message` envia uma mensagem para o servidor `RabbitMQ` através do canal de comunicação. Ele recebe três parâmetros: o `exchange` (__intercâmbio__) a ser utilizado, o `routing key` (__chave de encaminhamento__) a ser utilizado e o corpo da mensagem a ser enviada. O `exchange` é um ponto de encontro para as mensagens.

- ### Round
    Este código define a classe `Round`, que representa uma rodada de um jogo. A classe possui os seguintes atributos:

    - `game`: uma referência para o jogo ao qual a rodada pertence

    - `question`: a pergunta da rodada

    - `alternatives`: as alternativas da pergunta

    - `answers`: um dicionário que mapeia os usuários para as respostas que eles deram à 
    pergunta, junto com o tempo restante para responder a pergunta

    - `time_left`: o tempo restante para responder à pergunta

    A classe possui os seguintes métodos:

    - `add_answer`(self, user, answer, time_left): adiciona a resposta de um usuário à rodada. O parâmetro user é o usuário que deu a resposta, answer é a resposta dada pelo usuário e time_left é o tempo restante para responder à pergunta quando a resposta foi dada.

    - `finish`(self): finaliza a rodada. Esse método atualiza a pontuação de cada usuário de acordo com as respostas dadas e o tempo restante para responder à pergunta.

    - `get_score`(self): retorna uma lista com as pontuações dos usuários. Cada pontuação é o resultado de 100 pontos menos o tempo restante para responder à pergunta.

    Observe que a classe `Round` depende de uma instância da classe `PlayerController` para atualizar a pontuação dos usuários. Por isso, há uma linha de código no final que cria uma instância da classe `PlayerController` e a atribui à variável `player_controller`.

## Routes da aplicação
---
- ### Game
    Este código é um conjunto de rotas Flask para controlar o jogo. A primeira rota, `'/start_game'`, inicia um novo jogo, que é uma instância da classe `'Game'`. Ela espera receber um objeto `JSON` com os seguintes campos:

    `'id_lobby'`: ID do lobby onde o jogo será realizado.

    `'theme'`: Tema do jogo.

    `'rounds'`: Número de rodadas do jogo.

    `'time_left'`: Tempo restante para a primeira rodada.

    A rota `'/submit_answer'` espera receber um objeto `JSON` com os seguintes campos:

    `'id_lobby'`: ID do lobby onde o jogo está sendo realizado.

    `'user'`: Nome do usuário que enviou a resposta.

    `'answer'`: Resposta do usuário.

    `'time_left'`: Tempo restante para o término da rodada atual.

    Essa rota adiciona a resposta do usuário à rodada atual do jogo e verifica se a rodada foi finalizada. Se a rodada foi finalizada, ela finaliza a rodada e, se ainda houver mais rodadas, inicia a próxima rodada.

    A rota `'/finish_round'` espera receber um objeto JSON com o seguinte campo:

    `'id_lobby'`: ID do lobby onde o jogo está sendo realizado.

    Essa rota finaliza a rodada atual do jogo e, se ainda houver mais rodadas, inicia a próxima rodada. Se o jogo já tiver sido finalizado, ele envia um sinal para o RabbitMQClient para encerrar o jogo.

- ### Lobby

    Este código define uma série de rotas (__endpoints__) para uma aplicação web escrita em Python usando o framework `Flask`. Cada rota é mapeada para uma função específica, que é chamada quando uma solicitação `HTTP` é feita para a rota correspondente.

    A primeira linha importa a aplicação `Flask` da arquivo `"app.py"` e a segunda linha importa a classe `"request"` do módulo `Flask`, que permite acessar os detalhes da solicitação `HTTP`. As próximas duas linhas importam as classes `"LobbyController"` e `"PlayerController"` de algum local não especificado.

    Em seguida, as duas últimas linhas instanciam as classes `"LobbyController"` e `"PlayerController"` e atribuem as instâncias às variáveis ​​"`lobby_controller"` e `"player_controller"`, respectivamente.

    As linhas seguintes definem as rotas da aplicação:
    
    - A primeira rota é a `"/lobby"`, que é mapeada para a função `"create_lobby()"` e só aceita solicitações `HTTP` do tipo `"POST"`.
    
    - A segunda rota é a `"/lobby/<id>"`, que é mapeada para a função `"update_lobby(id)"` e só aceita solicitações `HTTP` do tipo `"PUT"`.
    
    - A terceira rota é a `"/lobby/<id>"`, que é mapeada para a função `"get_lobby(id)"` e só aceita solicitações `HTTP` do tipo `"GET"`.
    
    - A quarta rota é a `"/lobbys"`, que é mapeada para a função `"get_all_lobbys()"` e só aceita solicitações `HTTP` do tipo `"GET"`.
    
    - A quinta rota é a `"/lobby/<id>"`, que é mapeada para a função `"delete_lobby(id)"` e só aceita solicitações `HTTP` do tipo `"DELETE"`.

    As rotas seguintes são semelhantes e mapeiam para as funções:
    
    `"join_lobby()"`, `"get_players_by_lobby(id_lobby)"`, `"get_player_by_lobby(id_lobby, user)"`, `"update_player_score(id_lobby, user)"` e `"leave_lobby(id_lobby, user)"` respectivamente.

    Essas funções são implementadas nas classes `"LobbyController"` e `"PlayerController"` e são chamadas quando uma solicitação `HTTP` é feita para a rota correspondente. Por exemplo, quando uma solicitação `"POST"` é feita para a rota `"/lobby"`, a função `"create_lobby()"` será chamada e seu resultado será retornado como resposta à solicitação.