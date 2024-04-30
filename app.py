from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./student_record.db'
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
    return render_template('success.html')

@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)