from flask import Flask, render_template, jsonify, request
import json

# Directory containing sentiment scores
sentiment_file = "data/sentiment_scores/sentiment_scores.json"

# Load sentiment scores from file
with open(sentiment_file, 'r') as f:
    company_sentiments = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html', company_sentiments=company_sentiments)

@app.route('/sentiment')
def get_sentiment():
    selected_company = request.args.get('company')
    if selected_company in company_sentiments:
        sentiment_data = company_sentiments[selected_company]
        return jsonify(sentiment_data)
    return jsonify({})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
