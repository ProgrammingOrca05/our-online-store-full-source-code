import sqlite3


conn=sqlite3.connect("shop.db")

cursor=conn.cursor()

# Create the Product table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products_phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    color TEXT,
    features TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    rating INTEGER
);
''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS product_phone_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_name TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products_phones(id));

''')
cursor.execute('''
    CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
''')
cursor.execute('''
    CREATE TABLE admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

);
''')

feature="""A18 Bionic Chip with Neural Engine
6.9" Super Retina XDR Display (ProMotion 120Hz)
Quad-lens rear camera with AI-assisted 8K video
Under-display Touch ID & Face ID
5G+ Connectivity & Wi-Fi 7
Up to 1TB Storage Options
MagSafe 2.0 and full wireless charging
iOS 19 with AI personalization features"""

description= """Step into the future with the iPhone 16, Apple’s most advanced smartphone yet. Powered by the blazing-fast A18 Bionic chip and featuring an edge-to-edge 6.9-inch ProMotion OLED display, the iPhone 16 delivers unbeatable performance and stunning visuals.

Capture the world like never before with its quad-lens AI-enhanced camera system, designed for ultra-low light conditions and cinematic 8K video recording. Stay connected with 5G+ support, all-day battery life, and seamless integration with your Apple ecosystem.

The iPhone 16 introduces AirTouch gestures, under-display Touch ID, and a completely portless design — the future is truly wireless."""

cursor.execute('''
INSERT INTO products_phones (name, color, features, description, price, rating)
VALUES (?,?,?,?,?,?)''',('iPhone 16','Black',feature ,description, 999.99, 4))


cursor.execute('''
              INSERT INTO product_phone_images (product_id, image_name)
VALUES 
  (1, 'Iphone16img1.jpg'),
  (1, 'Iphone16img2.jpg'),
  (1, 'Iphone16img3.jpg'); 
              ''')

conn.commit()

conn.close()