import pytest
from noticias_cristianas import app

@pytest.fixture
def client():
    # Configura Flask en modo de prueba
    app.config['TESTING'] = True
    
    # Usa el cliente de prueba que provee Flask
    with app.test_client() as client:
        yield client

def test_home(client):
    """Prueba que la ruta '/' responda con '¡Hola, Mundo!'."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola, Mundo!".decode('utf-8') in response.data.decode('utf-8')
