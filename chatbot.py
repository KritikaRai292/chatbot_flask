from flask import Flask, render_template, request, jsonify
import os
import openai
import pdb

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route("/", methods =['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/chat', methods=["POST","GET"])
def chatbot():
    if request.method == "GET":
        user_input = str(request.args.get('text')) 
       
        print(user_input)
        prompt = f"user :- {user_input} \n chatbot :-"
        messages = [
            {"role": "user", "content": user_input}
        ]
        chat_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,  
            temperature = 0.5,
            max_tokens = 50
        )
        res = chat_response.choices[0]["message"]["content"]
        return res



if __name__=="__main__":
    app.run(debug=True)
