
from flask import Flask, jsonify, request, abort
from markupsafe import escape
from models import db, Item
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json() or {}
    name = data.get('name')
    qty = data.get('qty')
    if not name or not isinstance(qty, int):
        abort(400)
    item = Item(name=escape(name), qty=qty)
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'qty': item.qty}), 201

@app.route('/items', methods=['GET'])
def list_items():
    items = Item.query.all()
    return jsonify([{'id': i.id, 'name': i.name, 'qty': i.qty} for i in items]), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({'id': item.id, 'name': item.name, 'qty': item.qty}), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json() or {}
    item = Item.query.get_or_404(item_id)
    name = data.get('name')
    qty = data.get('qty')
    if name:
        item.name = escape(name)
    if isinstance(qty, int):
        item.qty = qty
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'qty': item.qty}), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)