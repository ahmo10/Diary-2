from flask import Flask
import json
from app import app
import unittest


class BasicTestCase(unittest.TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client()
        self.data = {
            "id": 1,
            "Title": "01/01/18",
            "Body": "I had fun at the zoo"
        }
        self.data3 = {
            "id": 3,
            "Title": "01/01/18",
            "Body": "I had fun at the zoo"
        }

#test for get all entries
    def test_get_all(self):
        response = self.client.get('/api/v1/user/entries', content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_valid_post(self):
        response = self.client.post(
            'api/v1/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)



#test for get one entry
    def test_get_one(self):
        response = self.client.post(
            'api/v1/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)        
        response = self.client.get('/api/v1/user/entries/1', content_type='json/appication')
        self.assertEqual(response.status_code, 200)

    # def test_update_an_entry(self):
    #     response = self.client.post(
    #         'api/v1/user/entries',
    #         data=json.dumps({
    #         "id": 2,
    #         "Title": "01/01/18",
    #         "Body": "I had fun at the zoo"
    #     }),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)        
    #     response = self.client.put('/api/v1/user/entries/2', data={
    #         "Title": "01/01/18",
    #         "Body": "I had fun at the zoo"}, content_type='json/appication')
    #     self.assertEqual(response.status_code, 202)

    def test_delete(self):
        response = self.client.post(
            'api/v1/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.delete('/api/v1/user/entries/1', content_type='json/appication')
        self.assertEqual(response.status_code, 204)




if __name__ == '__main__':
    unittest.main()
