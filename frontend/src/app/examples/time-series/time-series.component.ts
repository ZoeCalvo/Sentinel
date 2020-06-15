import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {TimeSeriesService} from './time-series.service';
import {Chart} from 'chart.js';
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-time-series',
  templateUrl: './time-series.component.html',
  styleUrls: ['./time-series.component.scss']
})
export class TimeSeriesComponent implements OnInit {
  id;
  since_date;
  until_date;
  is_tw;
  typeTimeSerie: string;
  schema: string;
  periods;
  period;
  chart = [];
  drawchart = false;
  public gradientStroke;
  public chartColor;
  public canvas: any;
  public ctx;
  public gradientFill;

  public hexToRGB(hex, alpha) {
    let r = parseInt(hex.slice(1, 3), 16),
      g = parseInt(hex.slice(3, 5), 16),
      b = parseInt(hex.slice(5, 7), 16);

    if (alpha) {
      return 'rgba(' + r + ', ' + g + ', ' + b + ', ' + alpha + ')';
    } else {
      return 'rgb(' + r + ', ' + g + ', ' + b + ')';
    }
  }

  constructor(private route: ActivatedRoute, private timeSerieService: TimeSeriesService ) { }

  ngOnInit() {
      this.id = this.route.snapshot.paramMap.get('id');
      this.since_date = this.route.snapshot.paramMap.get('since_date');
      this.until_date = this.route.snapshot.paramMap.get('until_date');
      this.is_tw = this.route.snapshot.paramMap.get('is_tw');
      if (this.typeTimeSerie !== undefined && this.schema !== undefined && this.periods !== undefined && this.period !== undefined) {
        this.typeTimeSerie = this.typeTimeSerie.trim();
        this.schema = this.schema.trim();
        this.periods = this.periods.trim();
        this.period = this.period.trim();
        if (!this.typeTimeSerie || !this.periods || !this.period) {
          return ;
        } else if (this.typeTimeSerie === 'holt_winters' && !this.schema) {
          return;
        } else {
          this.calculateTimeSeries(this.typeTimeSerie, this.schema, this.periods);
        }
      }
  }

  calculateTimeSeries(type, schema, num_periods) {
      this.drawchart = true;
      console.log(this.typeTimeSerie)
      console.log(this.schema)
      console.log(this.periods)
      this.timeSerieService.timeSerieChart(this.id, this.since_date, this.until_date, this.is_tw,
        this.typeTimeSerie, this.schema, this.periods, this.period).subscribe(response => {
          console.log(response);
          const estacionaria = response['estacionaria'];
          const score_original = response['data_original'].map(response => response.analysis_score)
          const date = response['data_original'].map(response => response.date)
          const score_time_serie = response['data_time_serie'].map(response => response.analysis_score)
          const prediccion = response['proyeccion'].map(response => response.analysis_score)

          this.chartColor = '#FFFFFF';
          this.canvas = document.getElementById('timeSerie');
          this.ctx = this.canvas.getContext('2d');

          this.gradientStroke = this.ctx.createLinearGradient(500, 0, 100, 0);
          this.gradientStroke.addColorStop(0, '#18ce0f');
          this.gradientStroke.addColorStop(1, this.chartColor);

          this.gradientFill = this.ctx.createLinearGradient(0, 170, 0, 50);
          this.gradientFill.addColorStop(0, 'rgba(128, 182, 244, 0)');
          this.gradientFill.addColorStop(1, this.hexToRGB('#18ce0f', 0.4));

            this.chart = new Chart(this.ctx, {
              type: 'line',
              data: {
                labels: date,
                datasets: [
                  {
                    label: 'datos reales',
                    backgroundColor: '#18ce0f',
                    data: score_original,
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderWidth: 1,
                    pointRadius: 4,
                    fill: false,
                    borderWidth: 2,
                    borderColor: '#18ce0f',
                    pointBorderColor: '#FFF',
                    pointBackgroundColor: '#18ce0f'

                  }, {
                    label: 'serie temporal',
                    backgroundColor: '#ce680f',
                    data: score_time_serie,
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderWidth: 1,
                    pointRadius: 4,
                    fill: false,
                    borderWidth: 2,
                    borderColor: '#ce680f',
                    pointBorderColor: '#FFF',
                    pointBackgroundColor: '#ce680f'
                  }, {
                    label: 'predicción',
                    backgroundColor: '#8187f7',
                    data: prediccion,
                    pointBorderWidth: 2,
                    pointHoverRadius: 4,
                    pointHoverBorderWidth: 1,
                    pointRadius: 4,
                    fill: false,
                    borderWidth: 2,
                    borderColor: '#8187f7',
                    pointBorderColor: '#FFF',
                    pointBackgroundColor: '#8187f7'
                  }],
              },
              options: {
                maintainAspectRatio: false,
                legend: {
                  display: true
                },
                tooltips: {
                  bodySpacing: 4,
                  mode: 'nearest',
                  intersect: 0,
                  position: 'nearest',
                  xPadding: 10,
                  yPadding: 10,
                  caretPadding: 10
                },
                responsive: true,
                scales: {
                  yAxes: [{
                    gridLines: {
                      zeroLineColor: 'transparent',
                      drawBorder: false
                    }
                  }],
                  xAxes: [{
                    display: 0,
                    ticks: {
                      display: false
                    },
                    gridLines: {
                      zeroLineColor: 'transparent',
                      drawTicks: false,
                      display: false,
                      drawBorder: false
                    }
                  }]
                },
                layout: {
                  padding: {
                    left: 0,
                    right: 0,
                    top: 15,
                    bottom: 15
                  }
                }
              }
            });
      })

  }
}