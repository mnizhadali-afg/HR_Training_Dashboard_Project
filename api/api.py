from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Path to the engagement.csv
ENGAGEMENT_CSV_PATH = os.path.join('..', 'data', 'raw', 'engagements.csv')

@app.route('/api/engagements', methods=['GET'])
def get_engagements():
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(ENGAGEMENT_CSV_PATH)
        
        # Convert the DataFrame to a dictionary
        engagements_data = df.to_dict(orient='records')
        
        # Return the engagements as JSON
        return jsonify(engagements_data), 200 # Return json with HTTP status 200
    
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404 # Return error with HTTP status 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # Return error with HTTP status 500
    
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Engagements API!", 200 # Return a welcome message with HTTP status 200

if __name__ == '__main__':
    app.run(debug=True,) # debug=True enables debug mode for development