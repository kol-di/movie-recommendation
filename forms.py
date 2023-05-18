from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange

from recsys.model import MAX_USERS, MAX_ITEMS


class RecommendForm(FlaskForm):
    user_id = IntegerField(
        'UserID',
        validators=[InputRequired(), NumberRange(min=0, max=MAX_USERS-1)])
    num_recs = IntegerField(
        'NumRecs',
        validators=[InputRequired(), NumberRange(min=0, max=MAX_ITEMS-1)])

    class Meta:
        csrf = False
