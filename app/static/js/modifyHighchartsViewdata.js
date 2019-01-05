/**
 * https://github.com/highcharts/export-csv/issues/102
 */
Highcharts.Chart.prototype.viewData = function () {
    if (!this.insertedTable) {
        var div = document.createElement('div');
        div.className = 'highcharts-data-table';
        // Insert after the chart container
        this.renderTo.parentNode.insertBefore(div, this.renderTo.nextSibling);
        div.innerHTML = this.getTable();
        this.insertedTable = true;
        var date_str = new Date().getTime().toString();
        var rand_str = Math.floor(Math.random() * (1000000)).toString();
        this.insertedTableID = 'div_' + date_str + rand_str
        div.id = this.insertedTableID;
    }
    else {
        $('#' + this.insertedTableID).toggle();
    }
};
Highcharts.setOptions({
    lang: {
    	downloadPNG: 'Download PNG',
    	downloadJPEG: 'Download JPEG',
    	downloadPDF: 'Download PDF',
    	downloadSVG: 'Download SVG',
        downloadCSV: 'Download CSV',
        downloadXLS: 'Download XLS',
        viewData: 'Toggle data table'
    },
    exporting: {
        buttons: {contextButton: {
            menuItems: ['viewData', "printChart", "separator",'downloadPNG', 'downloadJPEG', 'DownloadPDF', 'downloadSVG', 'separator', 'downloadCSV', 'downloadXLS']
        }},
        csv: {dateFormat: "%Y-%m"},
    },
});
