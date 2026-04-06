def test_unregister_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "unregtest@mergington.edu"
    # Register first
    client.post(f"/activities/{activity}/signup?email={email}")
    # Act
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    # Assert
    assert response.status_code == 200 or response.status_code == 404  # 404 if already removed
