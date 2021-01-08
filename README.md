Estrutura Inicial de uma database usando o postgresql, sqlalchemy

<<<<<<< HEAD
Para Versionar a DB usando o terminal:
- iniciar o Python ou iPython
    - from app import db, create_app
    - db.create_all(app=create_app())


Para Versionar a estrutura (corpo, esqueleto) da DB usando o Flask-Migrations
    - Nas Models
        from flask_migrate import Migrate
        mg = Migrate()

    - No init app importa a mg e a db dos models
        from app.models import db, mg
        
        e start ele usando isso:
        
        db.init_app(app)
        mg.init_app(app, db)

    - O DB tem q estar vazio, (deleta as tabelas)

    - No terminal 
        flask db init

        flask db migrate -m "Initial Migration" (o "commit")

        flask db upgrade (o "push")


    
=======
No terminal:
  * iniciar o Python ou iPython
    - from app import db, create_app
    - db.create_all(app=create_app())
>>>>>>> fee678fffb4d36cd0bc297fe9c7a701546de659d
