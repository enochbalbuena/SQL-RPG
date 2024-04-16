# SQL-RPG

This simple project aims to demonstrate the use of a local virtual environment with Python in a text editor (VS Code) to create or connect to SQLite databases, make queries, and fetch results.

To initiate the virtual environment we will need to run the commands "pipenv install" and "pipenv shell" in the root folder. Once it is initiated, we will create a new folder and paste our SQLite database, and create a new python file to make the connection (See .py file)

#### Example query after the connection is made:

<SELECT_ALL = 'SELECT character_id, name FROM charactercreator_character;'>

(Limiting only to the first five rows)

Result: [(1, 'Aliquid iste optio reiciendi'), (2, 'Optio dolorem ex a'), (3, 'Minus c'), (4, 'Sit ut repr'), (5, 'At id recusandae expl')]

The whole code is actually replicable and can be used following the given instructions.
