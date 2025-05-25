from flask import Flask,render_template,request,redirect
import sqlite3




app=Flask(__name__)

@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/shop/tech/product_phone')
# methods=["POST"])
def product_phone():
    # product_id = request.form.get('product_id')
    # if not product_id:
    #     return "Product ID missing", 400
    
    conn = sqlite3.connect('shop.db')
    conn.row_factory = sqlite3.Row 
    product = conn.execute('SELECT * FROM products_phones WHERE id=1').fetchone()
    images=conn.execute('SELECT * FROM product_phone_images WHERE product_id=1').fetchall()
    conn.close()
    
    
    
    return render_template('Products/displayProduct/phone.html',product=product,images=images)

@app.route('/shop/fashion/product_fashion')
def product_fashion():
    return render_template('Products/displayProduct/fashion.html')

@app.route('/shop/tech')
def products():
    conn = sqlite3.connect('shop.db')
    conn.row_factory = sqlite3.Row 
    products = conn.execute('SELECT * FROM products_phones').fetchall()
    conn.close()
    return render_template('/Products/PhonesProducts.html',products=products)

@app.route('/test')
def test():
    title="Iphone blah blah"
    return render_template('/Products/displayProduct/base_product.html',title=title)
if __name__==('__main__'):
    app.run(host="0.0.0.0",debug=True,port=7000)