from flask import Flask,jsonify, request
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Diary API',
    description='A simple Diary API',
	prefix="/api/v1"
)

ns = api.namespace('user', description='My diary enddpoints operations')
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
        entry["id"] = self.counter = self.counter +1
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
        # counter = 0
        # entries_model['id'] = counter + 1
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


if __name__ == '__main__':
    app.run(debug=True)
