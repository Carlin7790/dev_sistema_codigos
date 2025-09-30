from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///teste8.db", echo = True, future = True)

with engine.connect() as conn:
    conn.execute(text("""
                    CREATE TABLE IF NOT EXISTS alunos(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome VARCHAR(50) NOT NULL,
                      idade INTERGER NOT NULL,
                      email VARCHAR(80) UNIQUE NOT NULL
                       )
                      """))
    conn.commit()

with engine.connect() as conn:
        conn.execute(text("INSERT INTO alunos (nome,idade,email)" \
        "VALUES (:nome,:idade,:email)"),
        [ {"nome":"David","idade":21,"email":"davidvarao@senai.br"},
         {"nome":"Geovanni","idade":23,"email":"geovannicurica@senai.br"},
         {"nome":"Silvio","idade:":25,"email":"silviogaladaglobo@senai.br"}
        ]
        
        
        )
        conn.commit()
with engine.connect() as conn:
    resultado =  conn.execute(text("SELECT * FROM alunos"))
    for dado in resultado:
        print(dado.id,dado.nome,dado.idade,dado.email)
                          
                          


        
