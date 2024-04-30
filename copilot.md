Sure, here's a simple example of how you can create a form to collect student details, store it in SQLite using Flask, and display the details.

First, let's create the HTML form. Save this as `templates/form.html`:

```html
<!DOCTYPE html>
<html>
<body>

<h2>Student Form</h2>

<form action="/submit" method="post">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name"><br>
  <label for="age">Age:</label><br>
  <input type="text" id="age" name="age"><br>
  <label for="grade">Grade:</label><br>
  <input type="text" id="grade" name="grade"><br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>
```

Next, let's create the Flask application. Save this as `app.py`:

```python
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(80), nullable=False)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    student = Student(name=name, age=age, grade=grade)
    db.session.add(student)
    db.session.commit()
    return 'Student added successfully'

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

Finally, let's create a template to display the student details. Save this as `templates/students.html`:

```html
<!DOCTYPE html>
<html>
<body>

<h2>Student Details</h2>

{% for student in students %}
  <p>Name: {{ student.name }}</p>
  <p>Age: {{ student.age }}</p>
  <p>Grade: {{ student.grade }}</p>
  <hr>
{% endfor %}

</body>
</html>
```

To run the application, you can use the command `python app.py` in your terminal. You can then navigate to `http://localhost:5000` in your web browser to see the form. After submitting the form, you can navigate to `http://localhost:5000/students` to see the list of students. Please note that you need to have Flask and Flask-SQLAlchemy installed in your Python environment. You can install them using pip:

```bash
pip install flask flask_sqlalchemy
```

Source: Conversation with Bing, 4/30/2024
(1) github.com. https://github.com/Kathybui732/mod-2-notes/tree/866793b2467b02f8417766ce8e21fbe9e6896d37/intermission_work.md.