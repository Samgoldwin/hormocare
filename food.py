import pandas as pd
from pymongo import MongoClient

# Load the CSV file
df = pd.read_csv('pcos_meal_fuzzy_matched.csv')  # Change filename as needed

# Connect to MongoDB (make sure MongoDB is running, default port 27017)
client = MongoClient('localhost', 27017)
db = client['food_database']            # Use/create the database
collection = db['food_nutrition_diet']       # Collection name

# Convert DataFrame rows to dicts (MongoDB documents)
data = df.to_dict('records')

# Insert data into collection
collection.insert_many(data)

print(f"Successfully imported {len(data)} foods into MongoDB!")
