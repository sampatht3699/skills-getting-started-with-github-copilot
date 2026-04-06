def test_get_activities(client):
    # Arrange
    # (No special arrangement needed, uses in-memory DB)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
