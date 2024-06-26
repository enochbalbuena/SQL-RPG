#importing sqlite
import sqlite3
import queries as q
import pandas as pd


#DB connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    #make the cursor
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull and return the results
    return curs.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    #print(execute_q(conn, q.SELECT_ALL)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    #creating a dataframe with the results
    df =  pd.DataFrame(results)
    #renaming columns
    df.columns = ['name', 'average_item_weight']
    #print(df.head())
    #creating a csv with the created dataframe
    df.to_csv('rpg_db.csv', index=False)
