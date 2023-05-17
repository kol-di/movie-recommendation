from flask import Flask, redirect, url_for, request, render_template, abort
from forms import RecommendForm

app = Flask(__name__)


@app.route('/')
def root():
    # Redirect from app root to recommendations page
    return redirect(url_for('get_user_recommendations'))


@app.route('/recommend', methods=['GET', 'POST'])
def get_user_recommendations():
    form = RecommendForm(request.form)

    match request.method:
        case 'GET':
            # On first access return basic template with a form
            return render_template('recommend.html', form=form)

        case 'POST':
            # On form submission return template with the form and submission results
            if form.validate_on_submit():
                user_id = 17
                rec = ['abc', 'def', 'dcsd', 'dfcsd', 'sdcsd', 'sdcs']
                result = {
                    'user_id': user_id,
                    'rec': rec
                }
                return render_template('result.html', form=form, result=result)
            abort(422)  # Return Unprocessable Entity error for invalid form


# Execution entrypoint
if __name__ == '__main__':
    app.run()
