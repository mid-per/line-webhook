from flask import Flask, request, abort

app = Flask(__name__)

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the request body as text
    body = request.get_data(as_text=True)
    print("Webhook received:", body)

    # Return a success response
    return 'Webhook received!', 200

# Default route
@app.route('/')
def index():
    return 'LINE Chatbot is running!'

if __name__ == '__main__':
    app.run(port=3000)