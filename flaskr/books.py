# INF601 - Advanced Programming in Python
# Rachel White
# Mini Project 5

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('books', __name__)

@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
        'SELECT p.id, title, book_author, created, user_id, status, rating, notes, username'
        ' FROM books p JOIN user u ON p.user_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('books/index.html', books=books)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        book_author = request.form['book_author']
        status = request.form['status']
        rating = request.form.get('rating') or None
        notes = request.form['notes']
        error = None

        if not title:
            error = 'Title is required.'

        elif not book_author:
            error = 'Book author is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO books (title, book_author, status, rating, notes, user_id)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (title, book_author, status, rating, notes, g.user['id'])
            )
            db.commit()
            return redirect(url_for('books.index'))

    return render_template('books/create.html')

def get_books(id, check_user=True):
    books = get_db().execute(
        'SELECT p.id, title, book_author, created, user_id, status, rating, notes, username'
        ' FROM books p JOIN user u ON p.user_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if books is None:
        abort(404, f"Book id {id} doesn't exist.")

    if check_user and books['user_id'] != g.user['id']:
        abort(403)

    return books

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    books = get_books(id)

    if request.method == 'POST':
        title = request.form['title']
        book_author = request.form['book_author']
        status = request.form['status']
        rating = request.form.get('rating') or None
        notes = request.form['notes']
        error = None

        if not title:
            error = 'Title is required.'

        elif not book_author:
            error = 'Book author is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE books SET title = ?, book_author = ?, status = ?, rating = ?, notes = ?'
                ' WHERE id = ?',
                (title, book_author, status, rating, notes, id)
            )
            db.commit()
            return redirect(url_for('books.index'))

    return render_template('books/update.html', book=books)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_books(id)
    db = get_db()
    db.execute('DELETE FROM books WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('books.index'))
