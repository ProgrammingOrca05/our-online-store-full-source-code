import sqlite3


conn=sqlite3.connect("shop.db")

cursor=conn.cursor()

# Create the Product table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    color TEXT,
    features TEXT,
    description TEXT,
    price REAL NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    quantity INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS product_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_name TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

''')

features="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

description="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Porro exercitationem libero doloribus minima quisquam, deserunt voluptates repellat itaque totam saepe perferendis quos vero, nulla animi. Sed atque quos iusto itaque?"

cursor.execute(''' 
INSERT INTO products (name,category,color,features,description,price,rating,quantity)
VALUES(?,?,?,?,?,?,?,?)
               ''',('HUWAWIE 2KS','tech','green',features,description,120.99,5,3))

cursor.execute(''' 
INSERT INTO products (name,category,color,features,description,price,rating,quantity)
VALUES(?,?,?,?,?,?,?,?)
               ''',('IPHONE14 PRO MAX','tech','black',features,description,999.99,5,3))

cursor.execute(''' 
INSERT INTO products (name,category,color,features,description,price,rating,quantity)
VALUES(?,?,?,?,?,?,?,?)
               ''',('SAMSUNG A56','tech','blue',features,description,520.99,5,3))

cursor.execute(''' 
INSERT INTO products (name,category,color,features,description,price,rating,quantity)
VALUES(?,?,?,?,?,?,?,?)
               ''',('IPHONE16','tech','lightblue',features,description,1000.00,5,3))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(1,'images/products/huwaiephone.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(2,'images/products/Iphone16img1.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(3,'images/products/samsungphone.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(4,'images/products/iphonephoto.jpg'))

cursor.execute('''
INSERT INTO products (name,category,price,rating,quantity)
VALUES(?,?,?,?,?)
              ''',('Colorful shirt','fashion',200,5,5))

cursor.execute('''
INSERT INTO products (name,category,price,rating,quantity)
VALUES(?,?,?,?,?)
              ''',('Colorful shirt','fashion',300,5,5))
cursor.execute('''
INSERT INTO products (name,category,price,rating,quantity)
VALUES(?,?,?,?,?)
              ''',('Colorful shirt','fashion',500,5,5))
cursor.execute('''
INSERT INTO products (name,category,price,rating,quantity)
VALUES(?,?,?,?,?)
              ''',('Colorful shirt','fashion',100,5,5))
cursor.execute('''
INSERT INTO products (name,category,price,rating,quantity)
VALUES(?,?,?,?,?)
              ''',('Colorful shirt','fashion',220,5,5))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(5,'images/products/f1.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(6,'images/products/f2.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(7,'images/products/f3.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(8,'images/products/f4.jpg'))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(9,'images/products/f5.jpg'))

cursor.execute(''' 
INSERT INTO products (name,category,color,features,description,price,rating,quantity)
VALUES(?,?,?,?,?,?,?,?)
               ''',('Blue Pen','tool','lightblue',features,description,2.00,5,3))

cursor.execute('''
INSERT INTO product_images (product_id,image_name)
VALUES (?,?) 
              ''',(10,'images/products/pen.jpg'))

conn.commit()

conn.close()

