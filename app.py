from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product-center')
def product_center():
    return render_template('product.html')

@app.route('/technologies')
def technologies():
    return render_template('tech.html')


@app.route('/contact-us')
def contact():
    return render_template('contact.html')

@app.route('/distributor')
def distributor():
    return "<h1>Distributor Page</h1>"  # Or render a template if you have one

@app.route('/support')
def support():
    return "<h1>Support Page</h1>"

@app.route('/news')
def news():
    return "<h1>News Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
