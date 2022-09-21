from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Uc

uc_bp = Blueprint('uc_bp', __name__)

@uc_bp.route('/uc')
def uc_list():
    ucs_all = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_all)