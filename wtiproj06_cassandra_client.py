from cassandra.cluster import Cluster
from cassandra.query import dict_factory


def create_keyspace(session, keyspace):
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS """+keyspace+"""
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
    """)

def create_table(session, keyspace, table):
    session.execute("""
    CREATE TABLE IF NOT EXISTS """+ keyspace+"""."""+table+""" (
    user_id int ,
    avg_movie_rating float,
    PRIMARY KEY(user_id)
    )
    """)


def push_data_table(session, keyspace, table, userId, avgMovieRating):
    session.execute(
    """
    INSERT INTO """+keyspace+"""."""+table+""" (user_id, avg_movie_rating)
    VALUES (%(user_id)s, %(avg_movie_rating)s)
    """,
    {
    'user_id': userId,
    'avg_movie_rating': avgMovieRating
    }
    )

def get_data_table(session, keyspace, table):
    rows = session.execute("SELECT * FROM "+keyspace+"."+table+";")
    for row in rows:
        print(row)

def clear_table(session, keyspace, table):
    session.execute("TRUNCATE "+keyspace+"."+table+";")


def delete_table(session, keyspace, table):
    session.execute("DROP TABLE "+keyspace+"."+table+";")