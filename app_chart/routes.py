from flask import render_template, Blueprint
from app_chart.model import getChartsData

app_chart = Blueprint("app_chart", __name__, url_prefix="/chart", template_folder='templates', static_folder='static')

@app_chart.route('/')
@app_chart.route('/index')
@app_chart.route('/PMIs')
def PMIs():
    chart_info1 = {"chart_title": 'Manufacturing PMI in US and China', "quandl_codes": ['ISM/MAN_PMI', 'NBSC/A190101_M'], "legends": ["ISM Manufacturing PMI","China NBSC Manufacturing PMI"], "units": ["pt", "pt"]}
    chart_info2 = {"chart_title": 'Non-Manufacturing PMI in US and China', "quandl_codes": ['ISM/NONMAN_NMI', 'NBSC/A190201_M'], "legends": ["ISM Non-Manufacturing NMI","China NBSC Non-Manufacturing NBI"], "units": ["pt", "pt"]}

    charts, charts_comments = getChartsData(chart_info1,chart_info2)

    return render_template('app_chart/chart.html', title="Global Business Sentiment", charts=charts, charts_comments=charts_comments)