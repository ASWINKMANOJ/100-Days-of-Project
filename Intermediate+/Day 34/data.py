import requests

URL = 'https://opentdb.com/api.php?amount=10&category=31&type=boolean'
question = requests.get(URL)
question.raise_for_status()
text = question.json()
question_data = text["results"]