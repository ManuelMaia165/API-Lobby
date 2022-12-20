import pytest
from app import create_lobby, update_lobby, get_lobby

@pytest.fixture
def lobby_data():
    return {'name': 'Lobby 1', 'max_players': 4}

def test_create_lobby(lobby_data):
    # Act
    result = create_lobby(lobby_data)

    # Assert
    assert result['name'] == lobby_data['name']
    assert result['max_players'] == lobby_data['max_players']
    assert 'id' in result

def test_update_lobby(lobby_data):
    # Arrange
    lobby = create_lobby(lobby_data)
    lobby_data['name'] = 'Lobby 2'
    lobby_data['max_players'] = 6

    # Act
    result = update_lobby(lobby['id'], lobby_data)

    # Assert
    assert result['name'] == lobby_data['name']
    assert result['max_players'] == lobby_data['max_players']

def test_get_lobby(lobby_data):
    # Arrange
    lobby = create_lobby(lobby_data)

    # Act
    result = get_lobby(lobby['id'])

    # Assert
    assert result['name'] == lobby_data['name']
    assert result['max_players'] == lobby_data['max_players']