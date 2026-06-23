from urllib.parse import quote

from fastapi.testclient import TestClient

from src.app import app, activities


def test_remove_participant_from_activity():
    # Arrange
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    original_participants = activities[activity_name]["participants"].copy()

    try:
        # Act
        response = client.delete(
            f"/activities/{quote(activity_name)}/participants/{quote(email)}"
        )

        # Assert
        assert response.status_code == 200
        assert email not in activities[activity_name]["participants"]
        assert response.json()["message"] == f"Removed {email} from {activity_name}"
    finally:
        activities[activity_name]["participants"] = original_participants
