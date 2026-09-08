def validate_payload(data):
    required_fields = ["user_id", "email", "action"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, "Payload is valid."

if __name__ == "__main__":
    sample_data = {"user_id": 101, "email": "test@example.com", "action": "login"}
    is_valid, message = validate_payload(sample_data)
    print(message)