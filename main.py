from flask import Flask,redirect,render_template,url_for,request
import sqlite3

app=Flask(__name__)


@app.route('/home')
def homepage():
    return render_template("home.html",active_page='home')

@app.route('/about')
def aboutpage():
    return render_template("about.html",active_page='about')

@app.route('/shop')
def shoppage():
    conn=sqlite3.connect("shop.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()

    products=cursor.execute(''' SELECT * FROM products ''').fetchall()
    images=cursor.execute(''' SELECT * FROM product_images ''').fetchall()
    images={img['product_id']:img['image_name'] for img in images}
    
    product_list = []
    for product in products:
        product_dict = dict(product)
        product_dict['image_name'] = images.get(product['id'])  # fallback
        product_list.append(product_dict)

    return render_template('shop.html',active_page='shop',products=product_list)

@app.route('/blog')
def blogpage():
    return render_template('blog.html',active_page='blog')

@app.route('/contact')
def contactpage():
    return render_template('contact.html',active_page='contact')

@app.route('/cart')
def cartpage():
    return render_template('cart.html',active_page='cart')

@app.route('/displayphones')
def phonespage():
    conn=sqlite3.connect("shop.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()

    products=cursor.execute(''' SELECT * FROM products WHERE category='tech' ''').fetchall()
    images=cursor.execute(''' SELECT * FROM product_images ''').fetchall()
    images={img['product_id']:img['image_name'] for img in images}
    
    product_list = []
    for product in products:
        product_dict = dict(product)
        product_dict['image_name'] = images.get(product['id'])  # fallback
        product_list.append(product_dict)

    conn.close()
    
    return render_template('shopPhone.html',active_page='phone',products=product_list)

@app.route('/displayclothes')
def fashionpage():
    conn=sqlite3.connect("shop.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()

    products=cursor.execute(''' SELECT * FROM products WHERE category='fashion' ''').fetchall()
    images=cursor.execute(''' SELECT * FROM product_images ''').fetchall()
    images={img['product_id']:img['image_name'] for img in images}
    
    product_list = []
    for product in products:
        product_dict = dict(product)
        product_dict['image_name'] = images.get(product['id'])  # fallback
        product_list.append(product_dict)
    
    
    return render_template('fashion.html',active_page='fashion',products=product_list)

@app.route('/product', methods=['POST'])
def detailspage():
    product_id = request.form.get('product_id')

    conn = sqlite3.connect("shop.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    product = cursor.execute(''' SELECT * FROM products WHERE id=? ''', (product_id,)).fetchone()
    product_image = cursor.execute(''' SELECT * FROM product_images WHERE product_id=? ''', (product_id,)).fetchone()
    
    # Fetch related products for recommendation (example: fashion)
    products = cursor.execute(''' SELECT * FROM products ''').fetchall()
    images = cursor.execute(''' SELECT * FROM product_images ''').fetchall()
    imgs_fashion = [img[0] for img in cursor.execute('''
                                    SELECT image_name
                                    FROM product_images
                                    JOIN products ON product_images.product_id = products.id 
                                    WHERE products.category = 'fashion'; 
                                                ''').fetchall()]
    
    imgs_tech = [img[0] for img in cursor.execute('''
                                    SELECT image_name
                                    FROM product_images
                                    JOIN products ON product_images.product_id = products.id 
                                    WHERE products.category = 'tech'; 
                                                ''').fetchall()]
    
    imgs_tool = [img[0] for img in cursor.execute('''
                                    SELECT image_name
                                    FROM product_images
                                    JOIN products ON product_images.product_id = products.id 
                                    WHERE products.category = 'tool'; 
                                                ''').fetchall()]

    images = {img['product_id']: img['image_name'] for img in images}
    
    product_list = []
    for prod in products:
        product_dict = dict(prod)
        product_dict['image_name'] = images.get(prod['id'])
        product_list.append(product_dict)

    return render_template('product.html', product=product, product_image=product_image, products=product_list, imgs_fashion=imgs_fashion,imgs_tech=imgs_tech,imgs_tool=imgs_tool)


@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/register')
def registerpage():
    return render_template('signup.html')

@app.route('/policies')
def policypage():
    return render_template('policyandprivacy.html')    
    
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
    