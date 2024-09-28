import pytest
from noticias_cristianas import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Prueba que la ruta '/testimonio-del-dia' responda con '¡Hola, Mundo!'."""
    response = client.get('0.0.0.0:8080/testimonio-del-dia')
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Data: {response.data}")
    
    assert response.status_code == 200
    assert b'Hola, Mundo!' in response.data
