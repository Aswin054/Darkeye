from mongoconnection import get_client  # Import connection function

def display_data():
    # Get the MongoDB client
    client = get_client()
    if not client:
        print("Failed to connect to MongoDB.")
        return

    # Access the database and collection
    db = client["darkweb_data"]  # Use your database name
    collection = db["crawled_data"]  # Use your collection name

    # Retrieve all documents
    try:
        data = collection.find()
        print("\n=== Crawled Data ===")
        for document in data:
            print(document)  # Output each document
    except Exception as e:
        print(f"Error retrieving data: {e}")

if __name__ == "__main__":
    display_data()
