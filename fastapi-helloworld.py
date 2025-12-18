# Local env - install necessary packages
# pip install fastapi uvicorn
# to run the program - uvicorn fastapi-helloworld:app --reload
from fastapi import FastAPI
from employee import Employee

# Initialize the FastAPI application instance
app = FastAPI()

empList = [
    Employee(name="Simba", age=10, designation="Developer"),
    Employee(name="Mufasa", age=20, designation="Manager"),
    Employee(name="Nala", age=10, designation="Engineer"),
    Employee(name="Rafiki", age=50, designation="Guru")
    ]
# Defining root
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

# Defining random method
@app.get("/hello")
def hello():
    return {"message": "Hello"}

# Defining path variable
@app.get("/employee/{name}")
def get_employee(name: str):
    # filter from empList based on name
    name = name.lower()
    filtered_list = [
        employee for employee in empList
        if name in employee.name.lower()
    ]
    return filtered_list

# Defining Query params
@app.get("/employee-age/")
def get_employee_byage(age: int):
    print(age)
    filtered_list = [
        employee for employee in empList
        if age == employee.age
    ]
    return filtered_list

@app.post("/employee")
def add_employee(emp:Employee):
    empList.append(emp)
    return {"message": "Employee added successfully", "list": empList}