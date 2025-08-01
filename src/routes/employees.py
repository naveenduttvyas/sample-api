```python
from flask import Flask, request, jsonify
import tkinter as tk
from tkinter import ttk

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
        # Dummy department logic: if department is dummy, return Engineering employees
        if department == "dummy_department":
            filtered_employees = [emp for emp in employees if emp["department"] == "Engineering"]
        else:
            filtered_employees = [emp for emp in employees if emp["department"] == department]
        return jsonify(filtered_employees)
    else:
        return jsonify(employees)

class EmployeeListScreen(tk.Frame):
    def __init__(self, parent, employees):
        super().__init__(parent)
        self.employees = employees
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Department"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Department", text="Department")

        for employee in self.employees:
            self.tree.insert("", tk.END, values=(employee["id"], employee["name"], employee["department"]))

        self.tree.pack(expand=True, fill="both")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Employee List")
    employee_list_screen = EmployeeListScreen(root, employees)
    employee_list_screen.pack(expand=True, fill="both")
    root.mainloop()
```