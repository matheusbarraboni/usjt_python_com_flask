from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.uc import Uc
from datetime import date, datetime

uc_bp = Blueprint('uc_bp', __name__)

@uc_bp.route('/uc')
def uc_list():
    ucs_all = Uc.query.all()
    return render_template('uc_list.html', ucs=ucs_all)

@uc_bp.route('/uc/create')
def create_uc():
    return render_template('uc_create.html')

@uc_bp.route('/uc/add', methods=["POST"])
def add_uc():

    s_name = request.form["nome"]
    s_type = request.form["tipo"]
    d_start = datetime.strptime(request.form["inicio"], '%Y-%m-%d')
    d_end = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc(name=s_name, type=s_type, start=d_start, end=d_end)
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("uc_bp.uc_list"))

@uc_bp.route('/uc/update/<uc_id>')
def page_update_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id = uc_id).first()
    return render_template('uc_update.html', uc=uc_query)

@uc_bp.route('/uc/update', methods=["POST"])
def update_uc():

    i_uc = request.form["id"]
    s_name = request.form["nome"]
    s_type = request.form["tipo"]
    d_start = datetime.strptime(request.form["start"], '%Y-%m-%d')
    d_end = datetime.strptime(request.form["end"], '%Y-%m-%d')

    uc = Uc.query.filter_by(id = i_uc).first()
    uc.name = s_name
    uc.type = s_type
    uc.start = d_start
    uc.end = d_end
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for("uc_bp.uc_list"))

@uc_bp.route('/uc/delete/<uc_id>')
def confimr_delete_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id = uc_id).first()
    return render_template('uc_delete.html', uc=uc_query)

@uc_bp.route('/uc/delete', methods=["POST"])
def delete_uc():
    i_uc = request.form["id"]
    uc = Uc.query.filter_by(id = i_uc).first()
    db.session.delete(uc)
    db.session.commit()

    return redirect(url_for("uc_bp.uc_list"))
