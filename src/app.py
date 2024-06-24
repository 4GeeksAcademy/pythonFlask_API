from flask import Flask, request

app = Flask(__name__)

todos =[ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
   return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print(position,len (todos))
    if position >=len(todos):
      return{'message':'Fuera de rango'}, 402
    del todos [position]
    return todos





# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)