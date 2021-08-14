var chart;
var num = 0;
var series = 0;
/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
 function bubbleSort(arr){
   var len = arr.length;
   for (var i = len-1; i>=0; i--){
     for(var j = 1; j<=i; j++){
       if(arr[j-1]>arr[j]){
           var temp = arr[j-1];
           arr[j-1] = arr[j];
           arr[j] = temp;
           globalThis.arr = arr;
           return arr;
        }
     }
   }

}

function requestData() {
    $.ajax({
        url: '/live-data-merge',
        success: function(point) {

            var series = chart.series[0],
                shift = series.data.length > 10; // shift if the series is

                                                 // longer than 20
            if(series.data.length < 20){
            setTimeout(requestData, 250);
            }
            // add the point
            //chart.series[0].update(point, false);
            if(series.data.length >= 20){
            setTimeout(requestData, 250);
            chart.series[0].removePoint(point[0], true);
            }
            chart.series[0].addPoint(point, true, false);


            // call it again after one second

            num++;

        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'column',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Sort'
        },
        xAxis: {
            type: 'value',
            //tickPixelInterval: 150,
            maxZoom: 20
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },
        series: [{
            name: 'Random Generated Values',
            data: []
        }]
    });
});