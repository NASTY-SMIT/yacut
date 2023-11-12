from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from .constants import (
    OBLIGATORY_FIELD, CUSTOM_ID, ORIGINAL_LONG_LINK, SUBMIT_ADD,
    MIN_LENGTH_SHORT_ID, MAX_LENGTH_SHORT_ID)


class URLMapForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LONG_LINK,
        validators=[DataRequired(message=OBLIGATORY_FIELD), ]
    )
    custom_id = URLField(
        CUSTOM_ID,
        validators=[
            Length(
                MIN_LENGTH_SHORT_ID,
                MAX_LENGTH_SHORT_ID),
            Optional()]
    )
    submit = SubmitField(SUBMIT_ADD)
