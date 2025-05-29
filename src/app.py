from flask import Flask , jsonify, request
app= Flask(__name__)
#pipenv run python src/app.py para levantar la terminal 

todos= [{"label": "My first task", "done": False},
        {"label": "My second task", "done": False},
        {"label": "My third task", "done": False}]
'''
@app.route('/todos', methods=['GET'])
def hello_world():
    print (todos)
    saludos= '<h1>Hello!</h1>'
    return jsonify(saludos), 200 
'''


#endpoint para hacer GET de todos, devuelve la lista
#decorador 
@app.route('/todos', methods=['GET'])
def get_messages():
    print (todos)
    return jsonify(todos), 200 


#endpoint para hacer POST de una tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(silent=True)
    print("Incoming request with the following body", request_body)
   
    if request_body is not None:
        todos.append(request_body)
        print ("updated list todos:", todos) 
        return jsonify(todos), 200 #devuelve la tarea agregada
    else:
      return jsonify({"error": "Invalid todo format"}), 400
 

#endpoint para hacer DELETE

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    print("Current todos:", todos)
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Todo not found"}), 404
    todos.pop(position)  
    return jsonify(todos), 200
   
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)


