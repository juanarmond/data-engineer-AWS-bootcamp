import psycopg2
from datetime import datetime
import os
from random import choice
import time

dsn = (
    "dbname={dbname} "
    "user={user} "
    "password={password} "
    "port={port} "
    "host={host} ".format(
        dbname="orders",
        user="postgres",
        password="eH2IzvKmfOy^g9TZ=vTz,2SUtaX.qR",
        port=5432,
        host="rds-develop-orders-db.czfcc5x5walr.us-east-2.rds.amazonaws.com",

    )
)

conn = psycopg2.connect(dsn)
print("connected")
conn.set_session(autocommit=True)
cur = conn.cursor()
cur.execute(
    "create table if not exists orders("
    "created_at timestamp,"
    "order_id integer,"
    "product_name varchar(100),"
    "value float);"
)

products = {
    "house": 500000.00,
    "car": 69900.00,
    "motorcycle": 7900.00,
    "truck": 230000.00,
    "orange": 0.5,
    "rubber": 0.3,
    "iphone": 1000000.00,
}
idx = 0

while True:
    print(idx)
    idx += 1
    created_at = datetime.now().isoformat()
    # print(created_at, datetime.now())
    product_name, value = choice(list(products.items()))
    cur.execute(
        f"insert into orders values ('{created_at}', {idx}, '{product_name}', {value})"
    )
    time.sleep(0.2)
