from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

#test for get all entries
    def test_get_all(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries', content_type='html/text')
        self.assertEqual(response.status_code, 200)

#test for post endpoint
    def test_invalid_post(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/entries', content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_valid_post(self):
        tester = app.test_client(self)
        data = {"id":0, "title":"football", "description":"FINAL FRANCE WON"}
        response = tester.post("/api/v1/entries",  data=data, content_type="html/text")

 #test for deleting an entry
    def test_del(self):
        tester = app.test_client(self)
        data = {"id":0, "title":"football", "description":"FINAL FRANCE WON"}
        response = tester.delete('/api/v1/entries/0', data=data, content_type='html/text')
        self.assertEqual(response.status_code, 200)

#test for get one entry
    def test_get_one(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/entries/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    app.run(debug=True)
