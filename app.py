from flask import Flask, redirect, url_for, request, render_template
from forms import RecommendForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('get_user_recommendations'))


@app.route('/recommend', methods=['GET', 'POST'])
def get_user_recommendations():
    form = RecommendForm(request.form)
    match request.method:
        case 'GET':
            return render_template('recommend.html', form=form)
        case 'POST':
            if form.validate_on_submit():
                user_id = 17
                rec = ['abc', 'def', 'dcsd', 'dfcsd', 'sdcsd', 'sdcs']
                result = {
                    'user_id': user_id,
                    'rec': rec
                }

                return render_template('result.html', form=form, result=result)


if __name__ == '__main__':
    app.run()
