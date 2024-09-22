from cassandra.cluster import Cluster

def store_in_cassandra():
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};")
    session.execute("CREATE TABLE IF NOT EXISTS my_keyspace.data (id UUID PRIMARY KEY, message text);")
    session.execute("INSERT INTO my_keyspace.data (id, message) VALUES (uuid(), 'Hello from Cassandra');")
    print("Data stored in Cassandra")
