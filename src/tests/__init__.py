from flask import send_from_directory
from flask_restx import Resource

class TestPages(Resource):
    def get(self, content):
        return send_from_directory('tests/testpages', content)

testRoutes = [(TestPages, '/testpages/<path:content>')]
