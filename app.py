from flask import Flask,jsonify, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Diary API',
    description='A simple Diary API',
	prefix="/api/v1"
)

ns = api.namespace('user', description='My diary enddpoints operations')



#Dictionary to temporily store/hold diary entries
# entries_model = api.model('user', {
#     'id': fields.Integer(readOnly=True, description='The unique entry identifier'),
#     'title': fields.String(required=True, description='The title Name'),
# 	'body': fields.String(required=True, description='The body details')
# })

entries_model = ns.model(
    "content_model", {
        "Title":
        fields.String(
            required=True,
            description="title of my entry",
            example="FINAL"),
        "Body":
        fields.String(
            required=True,
            description="description",
            example="France won world cup for Africa")
    })


class Entry(object):
    def __init__(self):
        self.counter = 0
        self.entries = []

    def get(self, id):
        for entry in self.entries:
            if entry['id'] == id:
                return entry
        api.abort(404, "Entry {} doesn't exist".format(id))

    def create(self, data):
        entry = data
        entry['id'] = self.counter = self.counter + 1
        self.entries.append(entry)
        return entry

    def update(self, id, data):
        entry = self.get(id)
        entry.update(data)
        return entry

    def delete(self, id):
        entry = self.get(id)
        self.entries.remove(entry)

an_entry = Entry()
# an_entry.create({'Title': 'My Api', "Body":"Its fun creating api"})

@ns.route('/entries')
class Entries(Resource):
    '''Shows a list entries, and lets you POST to add new entry'''
    @ns.doc('Entries')
    # @ns.expect(entries_model)
    def get(self):
        '''List all entries'''
        return an_entry.entries

    @ns.doc('create entry')
    @ns.expect(entries_model)
    @ns.marshal_with(entries_model, code=201)
    def post(self):
        '''Create a new entry'''
        return an_entry.create(api.payload), 201


@ns.route('/entries/<int:id>')
@ns.response(404, 'Entry not found')
@ns.param('id', 'The entry identifier')
class Todo(Resource):
    '''Show a single entry item and lets you delete them'''
    @ns.doc('get_entry')
    def get(self, id):
        '''Fetch a given resource'''
        return an_entry.get(id)

    @ns.doc('delete_entry')
    @ns.response(204, 'Entry deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        an_entry.delete(id)
        return '', 204

    @ns.expect(entries_model)
    def put(self, id):
        '''Update a task given its identifier'''
        return an_entry.update(id, api.payload)











# #test route
# @app.route('/')
# def hello():
#     return 'Hello, World!'
#
# #route getting every entries
# @app.route('/api/v1/entries', methods=['GET'])
# def get_entries():
#     return jsonify({'Entries': Entries})
#
# #route post
# @app.route('/api/v1/entries', methods=['POST'])
# def create_entries():
#
#    date =  request.get_json(["datte"])
#    entry = date
#    Entries.append(entry)
#    print(Entries)
#    return jsonify({'Entries': Entries})
# @app.route('/api/v1/entries/<int:id>', methods=['DELETE'])
# def delete_entries(id):
#     entry = [entry for entry in Entries if entry['id'] == id]
#     del entry
#     return jsonify({'result': "Entry successfully deleted"})
#
# #get each entry
# @app.route('/api/v1/entries/<int:id>',methods=["GET"])
# def get_each_entry(id):
#     entry = [entry for entry in Entries if entry['id'] == id]
#
#     return jsonify({'results': entry})
#
#
# @app.route('/api/v1/entries/<int:id>', methods=['PUT'])
# def modify_entry(id):
#     entry = [entry for entry in Entries if entry['id'] == id]
#     body = request.get_json(['title'])
#     entry[0]['body'] = body['body']
#     return 'successfully modified'


if __name__ == '__main__':
    app.run(debug=True)
