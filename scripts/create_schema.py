import psycopg2
import sys
import os

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

subdomain = sys.argv[1]
schema_name = subdomain.replace(".", "_")

conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()

cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
conn.commit()

cursor.close()
conn.close()
print(f"Schema {schema_name} created successfully!")

