import mysql.connector

# Cria uma conexão com o banco de dados
conn = mysql.connector.connect(
    user='root',
    password='admin',
    host='127.0.0.1',
    database='api2'
)

# Cria um cursor
cursor = conn.cursor()

# Cria a tabela 'questions'
cursor.execute('''
    CREATE TABLE questions (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        text TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        theme VARCHAR(255) NOT NULL
    )
''')

# Insere algumas perguntas
cursor.execute('''
    INSERT INTO questions (text, correct_answer, theme) VALUES
        ('Qual é a capital do Brasil?', 'Brasília', 'Geografia'),
        ('Qual é a moeda do Japão?', 'Yen', 'Geografia'),
        ('Qual é o menor país do mundo?', 'Vaticano', 'Geografia'),
        ('Qual é o recorde de pontos em uma partida da NBA?', '100', 'Esporte'),
        ('Qual é o jogo mais vendido da história?', 'Minecraft', 'Games'),
        ('Quem foi o primeiro presidente dos Estados Unidos?', 'George Washington', 'História'),
        ('Qual é a maior cordilheira do mundo?', 'Andes', 'Geografia'),
        ('Qual é o animal mais rápido do mundo?', 'Leão', 'Geografia'),
        ('Qual é a cidade mais populosa do mundo?', 'Tóquio', 'Geografia'),
        ('Qual é a maior floresta do mundo?', 'Amazônia', 'Geografia')
''')




# Crie a tabela "alternatives" se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS alternatives (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  question_id INTEGER,
  text VARCHAR(255) NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
)
''')


# Inserir alternativas
cursor.execute('''
    INSERT INTO alternatives (question_id, text) VALUES
        (1, 'Rio de Janeiro'),
        (1, 'São Paulo'),
        (1, 'Belo Horizonte'),
        (1, 'Brasília'),
        (2, 'Dólar'),
        (2, 'Euro'),
        (2, 'Libra'),
        (2, 'Yen'),
        (3, 'Mônaco'),
        (3, 'Vaticano'),
        (3, 'Singapura'),
        (3, 'San Marino'),
        (4, '100'),
        (4, '95'),
        (4, '110'),
        (4, '105'),
        (5, 'Minecraft'),
        (5, 'Tetris'),
        (5, 'Grand Theft Auto V'),
        (5, 'PlayerUnknowns Battlegrounds'),
        (6, 'George Washington'),
        (6, 'John Adams'),
        (6, 'Thomas Jefferson'),
        (6, 'James Madison'),
        (7, 'Andes'),
        (7, 'Himalaias'),
        (7, 'Alpes'),
        (7, 'Rocky Mountains'),
        (8, 'Leão'),
        (8, 'Guepardo'),
        (8, 'Tigre'),
        (8, 'Onça'),
        (9, 'Tóquio'),
        (9, 'Deli'),
        (9, 'Mumbai'),
        (9, 'Cidade do México'),
        (10, 'Amazônia'),
        (10, 'Floresta Amazônica'),
        (10, 'Selva Amazônica'),
        (10, 'Mata Atlântica')
''')
# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
conn.close()