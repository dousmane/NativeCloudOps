from flask import request, jsonify
from . import db
from .models import Task, Frequency

def init_app_routes(app):
    @app.route('/tasks', methods=['POST'])
    def add_task():
        data = request.get_json()
        print("Received data:", data)  # Débogage
        try:
            frequency_value = data['frequency'].lower()
            print("Converted frequency:", frequency_value)  # Débogage
            new_task = Task(description=data['description'], frequency=Frequency[frequency_value])
            db.session.add(new_task)
            db.session.commit()
            return jsonify(new_task.to_dict()), 201
        except KeyError as e:
            print("KeyError:", e)  # Débogage
            return jsonify({"error": "Invalid frequency value"}), 400
        except Exception as e:
            print("Exception:", e)  # Débogage
            return jsonify({"error": str(e)}), 500

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        data = request.get_json()
        task = Task.query.get(task_id)
        if task:
            task.description = data['description']
            task.frequency = Frequency[data['frequency'].lower()]
            db.session.commit()
            return jsonify(task.to_dict())
        return jsonify({'message': 'Task not found'}), 404

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return jsonify({'message': 'Task deleted'})
        return jsonify({'message': 'Task not found'}), 404