from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange


class RecommendForm(FlaskForm):
    user_id = IntegerField(
        'UserID',
        validators=[InputRequired(), NumberRange(min=0, max=10000)])
    num_recs = IntegerField(
        'NumRecs',
        validators=[InputRequired(), NumberRange(min=0, max=1000)])

    class Meta:
        csrf = False
