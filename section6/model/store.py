from db import db
class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name":self.name, "items":[item.json() for item in self.items.all()]}

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

    def delete_from_db(self):
        # connection = sqlite3.connect('test.db')
        # cousor = connection.cursor()

        # insert_query = "INSERT INTO items VALUES (?, ?)"
        # cousor.execute(insert_query, (self.name, self.price))

        # connection.commit()
        # connection.close()
        db.session.delete(self)
        db.session.commit()