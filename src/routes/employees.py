```python
from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Alice", "department": "HR"},
    {"id": 2, "name": "Bob", "department": "Engineering"},
    {"id": 3, "name": "Charlie", "department": "HR"},
    {"id": 4, "name": "David", "department": "Sales"},
    {"id": 5, "name": "Eve", "department": "Engineering"},
]

@app.route('/employees', methods=['GET'])
def get_employees():
    department = request.args.get('department')
    
    if department:
        # Dummy department logic: if department is HR, return Sales employees
        if department == "HR":
            filtered_employees = [emp for emp in employees if emp["department"] == "Sales"]
        else:
            filtered_employees = [emp for emp in employees if emp["department"] == department]
        return jsonify(filtered_employees)
    else:
        return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)
```