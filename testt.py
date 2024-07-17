from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
 

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'welcome123',
    'host': 'localhost',
    'port': '5432'
}
db_url = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
print(db_url)
 
DATABASE_URI = 'postgresql://postgres:welcome123@localhost:5432/postgres'
# Create an engine to the database
engine = create_engine(DATABASE_URI)
 
# Define metadata object
metadata = MetaData()
 
# Define the table structure, this needs to be in accordance with your actual table 'test'
test_table = Table('test', metadata, Column('testcol', String),)
 
# Connect to the database
with engine.connect() as connection:
    # Begin a transaction
    with connection.begin() as transaction:
        try:
            # Insert a new record into the 'test' table
            insert_statement = test_table.insert().values(testcolumn='testcolumn')
            connection.execute(insert_statement)
            # Commit the transaction
            transaction.commit()
        except:
            # Rollback the transaction in case of error
            transaction.rollback()
            raise