import unittest
from app.crawler.xml_parser import XMLParser


class TestXMLParser(unittest.TestCase):
    def setUp(self):
        with open("data/data.xml", "r") as file:
            self.test_data = file.read()

        self.expected_result = {
            'root': {
                'user': [
                    {'email': '123@gmail.com', 'name': 'name1'},
                    {'email': '321@gmail.com', 'name': 'name2'},
                ],
                'value1': 1,
                'value2': 1,
                'meta': {'date': 'today', 'x': 33}
            }
        }

    def test_parse(self):
        parser = XMLParser(self.test_data)
        result = parser.parse()
        self.assertEqual(result, self.expected_result)

if __name__ == "__main__":
    unittest.main()
