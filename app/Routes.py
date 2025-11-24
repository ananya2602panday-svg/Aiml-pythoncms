from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import Student
from .forms import StudentForm
from flask import current_app as app

@app.route('/')
def index():
    students = Student.query.order_by(Student.joined_at.desc()).all()
    return render_template('index.html', students=students)

@app.route('/students')
def students_list():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        s = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            roll_number=form.roll_number.data,
        )
        db.session.add(s)
        db.session.commit()
        flash('Student added', 'success')
        return redirect(url_for('students_list'))
    return render_template('add_student.html', form=form)
