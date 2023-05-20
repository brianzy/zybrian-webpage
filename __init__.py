from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        input_text = request.json['message']

        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': 'Bearer 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',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'gpt-3.5-turbo',
                'messages': [
                    {'role': 'system', 'content': 'You are a user.'},
                    {'role': 'user', 'content': input_text}
                ]
            }
        )

        data = response.json()
        print(data)
        reply = data['choices'][0]['message']['content']
        return jsonify({'reply': reply})

    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
