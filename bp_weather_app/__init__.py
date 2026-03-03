#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 04-03-2026
# BluePrint    : bp_weather_app  
# File         : __init__.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

from flask import Blueprint, render_template, redirect, url_for

bp_weather_app = Blueprint('bp_weather_app', __name__ , template_folder="templates" ,static_folder="static", static_url_path="bp_weather_app")

# Routes: bp_weather_app ---------------------------------------------------------------------------# 
@bp_weather_app.route('/')
def index():
    return redirect(url_for("bp_weather_app.weather"))

@bp_weather_app.route('/weather')
def weather():
    return render_template("bp_weather_app_templates/weather.html")


