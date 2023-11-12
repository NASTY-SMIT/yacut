import random
import string

from flask import flash, redirect, render_template

from . import app, db
from .constants import LINK_DUPLICATE, LENGTH_RANDOM_SHORT_ID
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    return (''.join(random.choices(
        characters,
        k=LENGTH_RANDOM_SHORT_ID)))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short_name = form.custom_id.data or get_unique_short_id()
        if short_name and URLMap.query.filter_by(short=short_name).first():
            flash(LINK_DUPLICATE)
            return render_template('index.html', form=form)
        url_map = URLMap(original=form.original_link.data, short=short_name)
        db.session.add(url_map)
        db.session.commit()
        return render_template('index.html', form=form, shortid=url_map.short)
    return render_template('index.html', form=form)


@app.route('/<string:shortid>')
def redirect_shortid(shortid):
    return redirect(
        URLMap.query.filter_by(
            short=shortid).first_or_404().original)
