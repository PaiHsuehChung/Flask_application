from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from model.item import ItemModel

class ItemList(Resource):
    """Get all the items
    :endpoints: /items
    """
    @jwt_required()
    def get(self):
        return {'items': list(map(lambda x:x.json(),ItemModel.query.all()))}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required=True,
        help="This is required data"
    )
    parser.add_argument('store_id',
        type = int,
        required=True,
        help="The Store id must required."
    )

    def get(self, name):
        """Get specific item
        :endpoint: /item/<item name>

        :param name: item name
        :type name: str
        :return: item name and item price
        :rtype: JSON
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200

        return {"Message":"Item did not exists."}, 404

    def post(self, name):
        """Insert specific itme
        :endpoints: /item/<item name>
        :status: 
            if item exists return 400

        :param name: item name
        :type name: str
        :return: item name and item price
        :rtype: JSON
        """
        item = ItemModel.find_by_name(name)
        if item:
            return {"Message":f"{name} is already exists !"}, 400 

        data = Item.parser.parse_args()
        new_item = ItemModel(name, data['price'], data['store_id'])
        new_item.save_to_db()

        return new_item.json(), 201

    def delete(self, name):
        #FIXME: 
        """Delete specific item
        :note:
            What ever item is exists or not.

        :param name: item name
        :type name: str
        :return:  
        :rtype: JSON
        """
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
        
        return {'Message':"Delete Successful!"}, 200

    def put(self, name):
        """Modify item
        :note:
            MOdify price if item is exists
            otherwise, insert item
        :param name: item name
        :type name: str
        :return: [item name and item type]
        :rtype: [JSON]
        """
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'], data['store_id'])
        
        item.save_to_db()
        
        return item.json(), 201