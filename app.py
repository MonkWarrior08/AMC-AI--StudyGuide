import logging
from flask import Flask, render_template, request, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(
    model_name="ft:gpt-4o-2024-08-06:personal:monkone:A3GOmfoi",  # Replace with your fine-tuned model if available
    openai_api_key="openai_api_key"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        logging.debug(f"Received message: {user_message}")
        
        human_message = HumanMessage(content=user_message)
        
        logging.debug("Sending request to OpenAI")
        ai_response = chat_model([human_message])
        logging.debug(f"Received response: {ai_response.content}")
        
        return jsonify({'response': ai_response.content})
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
