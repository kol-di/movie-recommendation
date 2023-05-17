import unittest
from flask import url_for, template_rendered, Flask
from contextlib import contextmanager
from typing import ContextManager
from jinja2.environment import Template


@contextmanager
def captured_templates(flask_app: Flask) -> ContextManager[list]:
    """
    Determines which templates were rendered and what variables were passed
    """
    recorded = []

    def record(sender: Flask, template: Template, context: dict, **extra) -> None:
        recorded.append((template, context))

    template_rendered.connect(record, flask_app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, flask_app)


class AppTestCase(unittest.TestCase):

    def setUp(self) -> None:
        from app import app
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()
        self.request_context = self.app.test_request_context()

    def test_hello_world_redirect(self) -> None:
        # Request context to build URL adapter
        with self.request_context:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 302)  # Expecting redirect code
            self.assertEqual(response.location, url_for('get_user_recommendations'))  # Expecting proper redirect url

    def test_get_user_recommendations_get(self) -> None:
        with captured_templates(self.app) as templates:
            response = self.client.get('/recommend')
            self.assertEqual(response.status_code, 200)  # Expecting success
            self.assertEqual(len(templates), 1)  # Expecting one template
            template, context = templates[0]
            self.assertEqual(template.name, 'recommend.html')  # Expecting result template

    def test_get_user_recommendations_post_valid(self) -> None:
        user_id = 17
        num_recs = 26

        with captured_templates(self.app) as templates:
            response = self.client.post('/recommend', data={
                'user_id': user_id,
                'num_recs': num_recs
            })
            self.assertEqual(response.status_code, 200)  # Expecting success
            self.assertEqual(len(templates), 1)  # Expecting one template
            template, context = templates[0]
            self.assertEqual(template.name, 'result.html')  # Expecting result template
            self.assertEqual(context['result']['user_id'], user_id)  # Expecting not empty
            self.assertLessEqual(len(context['result']['rec']), num_recs)  # Expecting proper number of recommendations

    def test_get_user_recommendations_post_invalid(self) -> None:
        response = self.client.post('/recommend', data={})  # Empty data, invalid form
        self.assertEqual(response.status_code, 422)  # Expecting success

    def test_method_not_allowed(self) -> None:
        response = self.client.patch('/recommend')  # Invalid method
        self.assertEqual(response.status_code, 405)  # Expecting Method Not Allowed
