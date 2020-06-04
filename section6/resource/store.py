from flask_restful import Resource
from model.store import StoreModel
class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"Message":"store does not exists"}, 400

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"Message":"Store is exists"}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"Message":"Store save db error"}, 500

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"Message": "Delete Successful!"}

class StoreList(Resource):
    def get(self):
        return {"stores": list(map(lambda x:x.json(), StoreModel.query.all()))}