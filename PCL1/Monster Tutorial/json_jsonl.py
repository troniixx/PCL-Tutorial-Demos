import json
from datetime import datetime

def json_demo():
    print("=== JSON DEMONSTRATION ===\n")
    
    # 1. Creating JSON data
    user_data = {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice@example.com",
        "interests": ["python", "data science", "hiking"],
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
            "country": "USA"
        },
        "active": True,
        "last_login": str(datetime.now())
    }
    
    # 2. Writing JSON to a file
    print("Writing JSON to file...")
    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)
    
    # 3. Reading JSON from a file
    print("Reading JSON from file...")
    with open("user_data.json", "r") as f:
        loaded_data = json.load(f)
    print("\nLoaded JSON data:")
    print(json.dumps(loaded_data, indent=2))
    
    # 4. Working with JSON strings
    json_string = '{"name": "Bob", "age": 30}'
    parsed_json = json.loads(json_string)
    print("\nParsed JSON string:", parsed_json)

def jsonl_demo():
    print("\n=== JSONL DEMONSTRATION ===\n")
    
    # 1. Creating sample records
    records = [
        {"timestamp": str(datetime.now()), "event": "login", "user_id": 1},
        {"timestamp": str(datetime.now()), "event": "purchase", "user_id": 1, "amount": 29.99},
        {"timestamp": str(datetime.now()), "event": "logout", "user_id": 1}
    ]
    
    # 2. Writing JSONL
    print("Writing JSONL to file...")
    with open("events.jsonl", "w") as f:
        for record in records:
            json_line = json.dumps(record)
            f.write(json_line + "\n")
    
    # 3. Reading JSONL
    print("Reading JSONL from file...")
    loaded_records = []
    with open("events.jsonl", "r") as f:
        for line in f:
            record = json.loads(line.strip())
            loaded_records.append(record)
    
    print("\nLoaded JSONL records:")
    for record in loaded_records:
        print(record)
    
    # 4. Streaming JSONL processing (memory efficient)
    print("\nProcessing JSONL stream...")
    with open("events.jsonl", "r") as f:
        for line in f:
            record = json.loads(line.strip())
            # Process each record individually
            print(f"Processing event: {record['event']}")

def main():
    # JSON Demo
    json_demo()
    
    # JSONL Demo
    jsonl_demo()
    
    print("\n=== COMMON OPERATIONS ===")
    
    # Error handling
    try:
        json.loads('{"invalid": json}')
    except json.JSONDecodeError as e:
        print("\nHandling invalid JSON:", str(e))
    
    # Pretty printing
    data = {"nested": {"data": {"structure": [1, 2, 3]}}}
    pretty_json = json.dumps(data, indent=2)
    print("\nPretty printed JSON:")
    print(pretty_json)
    
    # Working with custom objects
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    # Custom JSON encoder (used if you have custom classes that JSON cant handle properly)
    class UserEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, User):
                return {"name": obj.name, "age": obj.age}
            return super().default(obj)
    
    user = User("Charlie", 35)
    print("\nCustom object serialization:")
    print(json.dumps(user, cls=UserEncoder))

if __name__ == "__main__":
    main()