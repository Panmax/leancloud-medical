# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template


class Todo(Object):
    pass

todos_view = Blueprint('todos', __name__)


@todos_view.route('')
def show():
    return render_template('test_date.html')


@todos_view.route('', methods=['POST'])
def add():
    content = request.form['content']
    todo = Todo(content=content)
    todo.save()
    return redirect(url_for('todos.show'))
