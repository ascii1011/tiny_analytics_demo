from flask import Flask, request, jsonify
from todolist import TodoList, authenticate

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate_route():
    # Get the Bearer token from the request
    bearer_token = request.headers.get('Authorization').split(' ')[1]
    
    # Authenticate the Bearer token
    if authenticate(bearer_token):
        # Token is valid, return a success response
        return jsonify({'success': True}), 200
    else:
        # Token is invalid, return an error response
        return jsonify({'error': 'Invalid token'}), 401

@app.route('/todolist', methods=['GET', 'POST', 'DELETE'])
def todolist_route():
    # Get the Bearer token from the request
    bearer_token = request.headers.get('Authorization').split(' ')[1]
    
    # Create a TodoList object with the Bearer token
    todo_list = TodoList(bearer_token)
    
    if request.method == 'GET':
        # Get the list of items
        items = todo_list.get_items()
        
        # Return the list of items
        return jsonify({'items': items}), 200
    elif request.method == 'POST':
        # Get the item to add from the request body
        item = request.json.get('item')
        
        # Add the item to the list
        if todo_list.add_item(item):
            # Item was added successfully, return a success response
            return jsonify({'success': True}), 201
        else:
            # There was an error adding the item, return an error response
            return jsonify({'error': 'Error adding item'}), 400
    elif request.method == 'DELETE':
        # Get the item ID from the request parameters
        item_id = request.args.get('item_id')
        
        # Remove the item from
        if todo_list.remove_item(item):
            # Item was added successfully, return a success response
            return jsonify({'success': True}), 201
        else:
            # There was an error adding the item, return an error response
            return jsonify({'error': 'Error adding item'}), 400
