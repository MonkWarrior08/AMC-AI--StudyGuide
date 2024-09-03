
from flask import Flask, request, jsonify, render_template
from flask import Flask, render_template, request, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

app = Flask(__name__)

# Initialize the ChatOpenAI model with the API key and a publicly available fine-tuned model
chat_model = ChatOpenAI(
    model_name="ft:gpt-4o-2024-08-06:personal:monkone:A3GOmfoi",  # Using a standard model, replace with your fine-tuned model if available
    openai_api_key="your_openai_api_key",
    # Remove the custom endpoint and API version
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
