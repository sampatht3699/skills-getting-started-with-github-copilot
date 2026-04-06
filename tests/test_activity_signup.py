def test_signup_success(client):
    # Arrange
    activity = "Chess Club"
    email = "test1@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert "message" in response.json()

def test_signup_invalid_email(client):
    # Arrange
    activity = "Chess Club"
    email = "not-an-email"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 422 or response.status_code == 400
