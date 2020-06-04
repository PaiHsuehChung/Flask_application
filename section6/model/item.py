from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name":self.name, "price":self.price, "store_id":self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM __tablename__ WHERE name=name LIMIT 1

    def save_to_db(self):
        # connection = sqlite3.connect('test.db')
        # cousor = connection.cursor()

        # update_query = "UPDATE items SET price=? WHERE name=?"
        # cousor.execute(update_query, (self.price, self.name))

        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        # connection = sqlite3.connect('test.db')
        # cousor = connection.cursor()

        # insert_query = "INSERT INTO items VALUES (?, ?)"
        # cousor.execute(insert_query, (self.name, self.price))

        # connection.commit()
        # connection.close()
        db.session.delete(self)
        db.session.commit()