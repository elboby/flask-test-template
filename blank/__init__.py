from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blank = Blueprint('blank', __name__,
                template_folder='templates',
                static_folder='static',)

@blank.route('/', defaults={'page': 'index'})
@blank.route('/<page>')
def show(page):
    print "showing %s" % page
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)