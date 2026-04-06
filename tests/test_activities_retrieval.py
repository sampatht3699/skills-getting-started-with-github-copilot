def test_activities_list_structure(client):
    # Arrange
    # (No special arrangement needed)
    # Act
    response = client.get("/activities")
    # Assert
    data = response.json()
    assert isinstance(data, dict)
    for details in data.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
