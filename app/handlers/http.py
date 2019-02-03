from flask import request
from flask_restplus import Resource, Namespace
from app.resources.schemas import example
from app.service.crud import get_all_examples, save_example, get_example

api = Namespace('example', description='example related operations')
api._path = '/'

example_schema = api.model('example', example)

@api.route('/')
class List(Resource):
    @api.doc('list of examples')
    @api.marshal_list_with(example_schema, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_examples()

    @api.doc('create a new user')
    @api.expect(example_schema, validate=True)
    @api.marshal_with(example_schema)
    def post(self):
        """Creates a new User """
        r = request.headers.get('stuff')
        if r == 'things':
            return {}, 200
        data = request.json
        return save_example(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
class User(Resource):
    @api.doc('get an example')
    @api.marshal_with(example_schema)
    def get(self, public_id):
        """get a user given its identifier"""
        return get_example(public_id)


    @api.doc('update an example')
    @api.expect(example_schema, validate=True, skip_none=True)
    def put(self, public_id):
        """Update and existing example"""
        data = request.json
        example = get_example(public_id)
        if not example:
            api.abort(404)
        else:
            example.update(data)
            return save_example(example)


@api.route('/<public_id>/hello')
@api.param('public_id', 'The user identifier')
class UserGreeting(Resource):
    @api.doc('Make an example say hello')
    def get(self, public_id):
        example = get_example(public_id)
        if not example:
            api.abort(404)
        else:
            return "{} says hello!".format(example['username'])
