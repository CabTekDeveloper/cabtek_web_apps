#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025 
# Modified     : 13-06-2025, Wangchuk
# File         : __init__.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

from flask import Flask, render_template,redirect, url_for, request, jsonify

from app.static.database_manager import db_manager

app = Flask(__name__)


# Routes: app ---------------------------------------------------------------------------# 
@app.route("/")
def index():
    return redirect(url_for("web_apps"))


@app.route("/web_apps")
def web_apps():
    return render_template("web_apps.html")


@app.route("/get_single_user_by_id_db/<user_id>", methods=['GET'])
def get_single_user_by_id_db(user_id):
    try:
        if request.method == "GET":
            user_info = db_manager.get_single_user_by_id_db(user_id)
            return jsonify(user_info)
        
    except Exception as ex:
        return jsonify(ex)


@app.route("/user_validation", methods=['POST'])
def user_validation():
    try:
        if request.method == "POST":
            data = request.get_json()
            user_id = data['user_id']
            password = data['password']
            validated = db_manager.validate_user(user_id, password)
            return jsonify({"validated":validated})
    except Exception as ex:
        return jsonify(ex)


