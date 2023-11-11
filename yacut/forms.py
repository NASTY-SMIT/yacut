from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from .constants import OBLIGATORY_FIELD, CUSTOM_ID, ORIGINAL_LONG_LINK, SUBMIT_ADD


class URLMapForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LONG_LINK,
        validators=[DataRequired(message=OBLIGATORY_FIELD), ]
    )
    custom_id = URLField(
        CUSTOM_ID,
        validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField(SUBMIT_ADD)
