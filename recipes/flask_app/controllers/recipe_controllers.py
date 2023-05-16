from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe_models import Recipe
from flask import flash


@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_recipe.html')


@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    if not Recipe.valid_recipe(request.form):
        return redirect('/recipe/new')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'prep_date': request.form['prep_date'],
        'time': request.form['time'],
        'user_id': session['user_id']
    }
    Recipe.create_recipe(data)
    return redirect(f'/user/{session["user_id"]}')


@app.route('/recipe/<int:recipe_id>')
def display_recipe(recipe_id):
    data = {'id': recipe_id}
    recipe = Recipe.get_recipe(data)
    if 'user_id' not in session:
        return redirect('/')
    return render_template('display_recipe.html', recipe=recipe)


@app.route('/recipe/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    data = {'id': recipe_id}
    recipe = Recipe.get_recipe(data)
    if 'user_id' not in session:
        return redirect('/')
    if session['user_id'] != recipe.user_id:
        flash("You can only edit your own recipes")
        return redirect(f'/recipe/{recipe.id}')
    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/recipe/update', methods=['POST'])
def update_recipe():
    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'prep_date': request.form['prep_date'],
        'time': request.form['time'],
    }
    Recipe.update_recipe(data)
    print(session['user_id'])
    return redirect(f'/user/{session["user_id"]}')


@app.route('/recipe/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {'id': recipe_id}
    recipe = Recipe.get_recipe(data)
    if 'user_id' not in session:
        return redirect('/')
    if session['user_id'] != recipe.user_id:
        flash("You can only delete your own recipes")
        return redirect(f'/recipe/{recipe.id}')
    Recipe.delete_recipe(recipe_id)
    return redirect(f'/user/{session["user_id"]}')
