# SQL-RPG

This simple project aims to demonstrate the use of a local virtual environment with Python in a text editor (VS Code) to create or connect to SQLite databases, make queries, and fetch results.

To initiate the virtual environment we will need to run the commands "pipenv install", "pipenv shell", and "pipenv install pandas" in the root folder. Once it is initiated, we will create a new folder and paste our SQLite database, and create a new python file to make the connection (See .py file)

The whole code is actually replicable and can be used following the given instructions.

A .csv file was exported as an example from the second query's result and is included in this repository.

#### Example queries:


SELECT_ALL = 'SELECT character_id, name FROM charactercreator_character;'


(Limiting only to the first five rows)

Result: [(1, 'Aliquid iste optio reiciendi'), (2, 'Optio dolorem ex a'), (3, 'Minus c'), (4, 'Sit ut repr'), (5, 'At id recusandae expl')]


AVG_ITEM_WEIGHT_PER_CHARACTER = '''
SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight FROM charactercreator_character AS cc_char
JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id = cc_inv.character_id
JOIN armory_item AS ai
ON ai.item_id = CC_inv.item_id
GROUP BY cc_char.character_id
'''


Result (after turning it into a dataframe): 
                           name  average_item_weight
0  Aliquid iste optio reiciendi                  0.0
1            Optio dolorem ex a                  0.0
2                       Minus c                  0.0
3                   Sit ut repr                  0.0
4         At id recusandae expl                  0.0
