from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Search/filter by title if query parameter 'q' is provided
    query = request.args.get("q", "").lower()
    if query:
        filtered = [t for t in tasks if query in t["title"].lower()]
        return jsonify(filtered), 200
    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": data.get("completed", False)
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    task["title"] = data.get("title", task["title"])
    task["completed"] = data.get("completed", task["completed"])
    return jsonify(task), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
