#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : bp_dev_token_app  
# File         : __init__.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

from flask import Blueprint, render_template, redirect, url_for, jsonify, json, request
from app.static.database_manager import db_manager

bp_dev_token_app = Blueprint('bp_dev_token_app', __name__ , template_folder="templates" ,static_folder="static", static_url_path="bp_dev_token_app")

# Routes: bp_dev_token_app ---------------------------------------------------------------------------# 
@bp_dev_token_app.route('/')
def index():
    return redirect(url_for("bp_dev_token_app.dev_token_apps"))

@bp_dev_token_app.route('/dev_token_apps')
def dev_token_apps():
    all_apps = db_manager.get_all_apps_db()
    return render_template("bp_dev_token_app_templates/dev_token_apps.html", all_apps=all_apps)


@bp_dev_token_app.route('/get_developer_list_from_db' , methods=["GET"])
def get_developer_list_from_db():
    try:
        if request.method == "GET":
            all_users = db_manager.get_all_users_db()
            developers = [user for user in all_users if "user_roles" in user and any(role['id'] == 3 for role in user['user_roles'] )]
            return jsonify(developers)
    except Exception as ex:
        return jsonify(ex)


@bp_dev_token_app.route('/assign_developer_to_app_db' , methods=["POST"])
def assign_developer_to_app_db():
    try:
        if request.method == "POST":
            data = request.get_json()
            app_id = data['app_id']
            user_id = data['user_id']
            db_manager.tbl_apps_in_dev.insert_into_tbl_app_in_dev(app_id, user_id)
            return jsonify({"success":True})
    except Exception as ex:
        return jsonify(ex)


@bp_dev_token_app.route('/remove_app_in_dev_by_db' , methods=["POST"])
def remove_app_in_dev_by_db():
    try:
        if request.method == "POST":
            data = request.get_json()
            app_id = data['app_id']
            user_id = data['user_id']
            removed = db_manager.tbl_apps_in_dev.remove_app_in_dev_by(app_id, user_id)
            return jsonify({"removed":removed})
    except Exception as ex:
        return jsonify(ex)


@bp_dev_token_app.route('/get_apps_in_dev_db' , methods=["GET"])
def get_apps_in_dev_db():
    try:
        if request.method == "GET":
            return jsonify(db_manager.tbl_apps_in_dev.get_apps_in_dev())
    except Exception as ex:
        return jsonify(ex)