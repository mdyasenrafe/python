import my_code

api_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'


def test_get_response():
    response = my_code.get_response(api_url)
    assert response.status_code == 200


def test_my_name():
    assert my_code.my_name() == 'Enter a name: '
