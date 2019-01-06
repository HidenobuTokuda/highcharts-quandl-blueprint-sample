import quandl
import numpy as np

def getChartsData(*args):
    charts_info = args

    charts = []
    chart_titles = []
    charts_comments = []
    for chart_info in charts_info:
        quandl_codes = chart_info["quandl_codes"]
        legends = chart_info["legends"]
        units = chart_info["units"]

        dataset = []
        comments = []
        for quandl_code, legend, unit in zip(quandl_codes, legends, units):
            quandl_dataset = quandl.Dataset(quandl_code)
            quandl_data = quandl_dataset.data().to_pandas()

            values = quandl_data[quandl_dataset.column_names[1]].tolist()
            labels = (quandl_data.index.to_period("M").to_timestamp('S').astype(np.int64) // 10**6).tolist()

            data = []
            for label, value in zip(labels, values):
                data.append([label,value])
            dataset.append({"legend":legend,"data":data})

            comment = make_comment(quandl_data, quandl_dataset, legend, unit)
            comments.append(comment)
       
        charts.append({"chart_title":chart_info["chart_title"], "dataset":dataset})
        charts_comments.append(comments)

    return charts, charts_comments

def make_comment(quandl_data, quandl_dataset, legend, unit):
    if unit == "pt":
        change = quandl_data[quandl_dataset.column_names[1]].diff().tail(1).values[0]
        display_unit = unit

    if change > 0:
        comment = "<u>" + legend + "</u> <mark class='text-primary'>increased by " + format(change,".1f") + display_unit + "</mark> in " + quandl_dataset["newest_available_date"].strftime("%B %Y")
    elif change < 0:
        comment = "<u>" + legend + "</u> <mark class='text-danger'>decreased by " + format(abs(change),".1f") + display_unit + "</mark> in " + quandl_dataset["newest_available_date"].strftime("%B %Y")
    else:
        comment = "<u>" + legend + "</u> <mark class='text-sucess'>was flat</mark> in " + quandl_dataset["newest_available_date"].strftime("%B %Y")

    return comment