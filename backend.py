from flask import Flask, request, jsonify
from langchain.agents import initialize_agent, Tool
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

app = Flask(__name__)

# Initialize OpenAI model, embeddings, and FAISS
llm = OpenAI(model_name="your-fine-tuned-model")
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(["your", "initial", "data"], embeddings)

# Define tools for agents
tools = [
    Tool(
        name="Vector Store",
        func=vectorstore.similarity_search,
        description="Searches the vector store for relevant information"
    )
]

# Initialize agents
main_agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
verification_agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    
    # Generate response from main agent
    main_response = main_agent.run(user_input)
    
    # Verify response with verification agent
    verified_response = verification_agent.run(f"Verify this response: {main_response}")
    
    return jsonify({'response': verified_response})

if __name__ == '__main__':
    app.run(debug=True)
