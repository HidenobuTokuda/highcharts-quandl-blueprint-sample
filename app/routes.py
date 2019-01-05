from app import app
from flask import render_template
from app.model import getChartsData

@app.route('/')
@app.route('/index')
def chart():
    chart_info1 = {"chart_title": 'Manufacturing PMI in US and China', "quandl_codes": ['ISM/MAN_PMI', 'NBSC/A190101_M'], "legends": ["ISM Manufacturing PMI","China NBSC Manufacturing PMI"], "units": ["pt", "pt"]}
    chart_info2 = {"chart_title": 'Non-Manufacturing PMI in US and China', "quandl_codes": ['ISM/NONMAN_NMI', 'NBSC/A190201_M'], "legends": ["ISM Non-Manufacturing NMI","China NBSC Non-Manufacturing NBI"], "units": ["pt", "pt"]}

    charts, charts_comments = getChartsData(chart_info1,chart_info2)

    return render_template('chart.html', title="Global Business Sentiment", charts=charts, charts_comments=charts_comments)