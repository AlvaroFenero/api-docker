from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def ping():
    data = {
        "code": 200,
        "response": "Respuesta desde API en Docker"
	}
    return jsonify(data)


@app.route('/productos')
def productos():
    data = {
	"code"  : 200,
        "id"    : 1,
        "name"  : "Neumatico king star aro 24", 
	"price" : 16000,
	"img"   : "https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/hammer.png"
    
        }
  
    return render_template('product.html', name=data['name'], price=data['price'], img=data['img'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
