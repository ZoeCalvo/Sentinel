import {Component, OnDestroy, OnInit} from '@angular/core';
import * as Chartist from 'chartist';
import {DashboardService} from './dashboard.service';
import {Dashboard} from './dashboard';
import {element} from "protractor";
import {Chart} from 'chart.js';
import 'rxjs/add/operator/map';
import {ActivatedRoute} from "@angular/router";
import {GraphsService} from "./graphs.service";
import {IntervalgraphService} from "./intervalgraph.service";
import {PiechartService} from "./piechart.service";


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})

export class DashboardComponent implements OnInit, OnDestroy {
  chart = [];
  table_score;
  is_dynamic = false;
  id;
  since_date;
  until_date;
  is_tw;
  headers = ['analysis_score', 'text'];
  graph = null;
  public lineBigDashboardChartType;
  public gradientStroke;
  public chartColor;
  public canvas: any;
  public ctx;
  public gradientFill;
  public lineBigDashboardChartData: Array<any>;
  public lineBigDashboardChartOptions: any;
  public lineBigDashboardChartLabels: Array<any>;
  public lineBigDashboardChartColors: Array<any>

  public gradientChartOptionsConfiguration: any;
  public gradientChartOptionsConfigurationWithNumbersAndGrid: any;

  public lineChartType;
  public lineChartData: Array<any>;
  public lineChartOptions: any;
  public lineChartLabels: Array<any>;
  public lineChartColors: Array<any>

  public lineChartWithNumbersAndGridType;
  public lineChartWithNumbersAndGridData: Array<any>;
  public lineChartWithNumbersAndGridOptions: any;
  public lineChartWithNumbersAndGridLabels: Array<any>;
  public lineChartWithNumbersAndGridColors: Array<any>

  public lineChartGradientsNumbersType;
  public lineChartGradientsNumbersData: Array<any>;
  public lineChartGradientsNumbersOptions: any;
  public lineChartGradientsNumbersLabels: Array<any>;
  public lineChartGradientsNumbersColors: Array<any>;

  // events
  public chartClicked(e: any): void {
    console.log(e);
  }

  public chartHovered(e: any): void {
    console.log(e);
  }
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

  sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
  }

  constructor(private dashboardService: DashboardService, private route: ActivatedRoute,
              private graphsService: GraphsService, private intervalGraphService: IntervalgraphService, private pieChartService: PiechartService) { }

  ngOnInit() {
      this.id = this.route.snapshot.paramMap.get('id');
      this.since_date = this.route.snapshot.paramMap.get('since_date');
      this.until_date = this.route.snapshot.paramMap.get('until_date');
      this.is_tw = this.route.snapshot.paramMap.get('is_tw');

      this.id = this.id.trim();
      if (!this.id) { return ; }
      this.showAnalysisScoreGraph(this.id, this.since_date, this.until_date, this.is_tw);
      this.sleep(500).then( () => {this.getDataForGraph(this.id, this.since_date, this.until_date, this.is_tw); })
      this.sleep(1000).then( () => {this.getforIntervalGraph(this.id, this.since_date, this.until_date, this.is_tw, this.is_dynamic); })
      this.sleep(1500).then( () => {this.getforPieChart(this.id, this.since_date, this.until_date, this.is_tw); })


      this.chartColor = '#FFFFFF';
      this.canvas = document.getElementById('bigDashboardChart');
      this.ctx = this.canvas.getContext('2d');

      this.gradientStroke = this.ctx.createLinearGradient(500, 0, 100, 0);
      this.gradientStroke.addColorStop(0, '#80b6f4');
      this.gradientStroke.addColorStop(1, this.chartColor);

      this.gradientFill = this.ctx.createLinearGradient(0, 200, 0, 50);
      this.gradientFill.addColorStop(0, 'rgba(128, 182, 244, 0)');
      this.gradientFill.addColorStop(1, 'rgba(255, 255, 255, 0.24)');
      this.lineBigDashboardChartData = [
          {
            label: 'Data',

            pointBorderWidth: 1,
            pointHoverRadius: 7,
            pointHoverBorderWidth: 2,
            pointRadius: 5,
            fill: true,

            borderWidth: 2,

            data: ['0.35', '0.4', '0.36']
          }
      ];

      this.lineBigDashboardChartColors = [
         {
           backgroundColor: this.gradientFill,
           borderColor: this.chartColor,
           pointBorderColor: this.chartColor,
           pointBackgroundColor: '#2c2c2c',
           pointHoverBackgroundColor: '#2c2c2c',
           pointHoverBorderColor: this.chartColor,
         }
       ];
      this.lineBigDashboardChartLabels = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
      this.lineBigDashboardChartOptions = {

            layout: {
                padding: {
                    left: 20,
                    right: 20,
                    top: 0,
                    bottom: 0
                }
            },
            maintainAspectRatio: false,
            tooltips: {
              backgroundColor: '#fff',
              titleFontColor: '#333',
              bodyFontColor: '#666',
              bodySpacing: 4,
              xPadding: 12,
              mode: 'nearest',
              intersect: 0,
              position: 'nearest'
            },
            legend: {
                position: 'bottom',
                fillStyle: '#FFF',
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        fontColor: 'rgba(255,255,255,0.4)',
                        fontStyle: 'bold',
                        beginAtZero: true,
                        maxTicksLimit: 5,
                        padding: 10
                    },
                    gridLines: {
                        drawTicks: true,
                        drawBorder: false,
                        display: true,
                        color: 'rgba(255,255,255,0.1)',
                        zeroLineColor: 'transparent'
                    }

                }],
                xAxes: [{
                    gridLines: {
                        zeroLineColor: 'transparent',
                        display: false,

                    },
                    ticks: {
                        padding: 10,
                        fontColor: 'rgba(255,255,255,0.4)',
                        fontStyle: 'bold'
                    }
                }]
            }
      };

      this.lineBigDashboardChartType = 'line';

      this.canvas = document.getElementById('lineChartExample');
      this.ctx = this.canvas.getContext('2d');

      this.gradientStroke = this.ctx.createLinearGradient(500, 0, 100, 0);
      this.gradientStroke.addColorStop(0, '#80b6f4');
      this.gradientStroke.addColorStop(1, this.chartColor);

      this.gradientFill = this.ctx.createLinearGradient(0, 170, 0, 50);
      this.gradientFill.addColorStop(0, 'rgba(128, 182, 244, 0)');
      this.gradientFill.addColorStop(1, 'rgba(249, 99, 59, 0.40)');

      this.lineChartData = [
              {
                label: 'Active Users',
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 1,
                pointRadius: 4,
                fill: true,
                borderWidth: 2,
                data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 630]
              }
            ];
        this.lineChartColors = [
         {
           borderColor: '#f96332',
           pointBorderColor: '#FFF',
           pointBackgroundColor: '#f96332',
           backgroundColor: this.gradientFill
         }
       ];
      this.lineChartLabels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
      this.lineChartOptions = this.gradientChartOptionsConfiguration;

      this.lineChartType = 'line';

      this.gradientChartOptionsConfiguration = {
        maintainAspectRatio: false,
        legend: {
          display: false
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
        responsive: 1,
        scales: {
          yAxes: [{
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
      };

      this.gradientChartOptionsConfigurationWithNumbersAndGrid = {
        maintainAspectRatio: false,
        legend: {
          display: false
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
      };
  }

  showAnalysisScoreGraph(id, since_date, until_date, is_tw){

    this.dashboardService.readAnalysis(id, since_date, until_date, is_tw).subscribe(
        response => {
          let score = response['data'].map(response => response.analysis_score)
          this.table_score = response['data'];
          let dates = response['data'].map(response => response.date)
          let scores = [];
          score.forEach((response) => scores.push(response))

          this.chartColor = '#FFFFFF';
          this.canvas = document.getElementById('prueba');
          this.ctx = this.canvas.getContext('2d');
          this.gradientStroke = this.ctx.createLinearGradient(500, 0, 100, 0);
          this.gradientStroke.addColorStop(0, '#18ce0f');
          this.gradientStroke.addColorStop(1, this.chartColor);

          this.gradientFill = this.ctx.createLinearGradient(0, 170, 0, 50);
          this.gradientFill.addColorStop(0, 'rgba(128, 182, 244, 0)');
          this.gradientFill.addColorStop(1, this.hexToRGB('#2CA8FF', 0.6));

          this.chart = new Chart(this.ctx, {
            type: 'bar',
            data: {
              labels : dates,
              datasets: [
                {
                  pointBorderWidth: 2,
                  pointHoverRadius: 4,
                  pointHoverBorderWidth: 1,
                  pointRadius: 4,
                  fill: true,
                  borderWidth: 1,
                  data: scores,
                  backgroundColor: this.gradientFill,
                  borderColor: '#2CA8FF',
                  pointBorderColor: '#FFF',
                  pointBackgroundColor: '#2CA8FF'
                }
              ],
            },
            options: {
              maintainAspectRatio: false,
              legend: {
              display: false
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
              responsive: 1,
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
          })

        })
  }

  getDataForGraph(id, since_date, until_date, is_tw) {

    this.graphsService.getforGraphs(id, since_date, until_date, is_tw).subscribe(
      response => {
        console.log(response);
        let score = response['data'].map(response => response.analysis_score)
        let date = response['data'].map(response=> response.date)

        this.canvas = document.getElementById('lineChartExampleWithNumbersAndGrid');
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
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 1,
                pointRadius: 4,
                fill: true,
                borderWidth: 2,
                data: score,
                borderColor: '#18ce0f',
                pointBorderColor: '#FFF',
                pointBackgroundColor: '#18ce0f',
                backgroundColor: this.gradientFill
              }
            ]
          },
          options: {

            maintainAspectRatio: false,
            legend: {
              display: false
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
        })
    })
  }

  getforIntervalGraph(id, since_date, until_date, is_tw, is_dynamic){

    this.intervalGraphService.getIntervalGraphData(id, since_date, until_date, is_tw, is_dynamic).subscribe(
      response => {
        let intervals = response['data'].map(response => response.interval)
        let score = response['data'].map(response => response.totalScore)
        if (this.graph != null) {
          this.graph.clear();
          this.graph.destroy();
        }
        this.canvas = document.getElementById('barChartSimpleGradientsNumbers');
        this.ctx = this.canvas.getContext('2d');

        this.gradientFill = this.ctx.createLinearGradient(0, 170, 0, 50);
        this.gradientFill.addColorStop(0, 'rgba(128, 182, 244, 0)');
        this.gradientFill.addColorStop(1, this.hexToRGB('#d782d9', 0.6));



        this.graph = new Chart(this.ctx, {
          type: 'bar',
          data: {
            labels: intervals,
            datasets: [{
              pointBorderWidth: 2,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 1,
              pointRadius: 4,
              fill: true,
              borderWidth: 1,
              data: score,
              backgroundColor: this.gradientFill,
              borderColor: '#d782d9',
              pointBorderColor: '#FFF',
              pointBackgroundColor: '#d782d9'
            }]
          },
          options: {
            maintainAspectRatio: false,
            legend: {
              display: false
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
            responsive: 1,
            scales: {
              yAxes: [{
                gridLines: {
                  zeroLineColor: 'transparent',
                  drawBorder: false
                }
              }],
              xAxes: [{
                display: intervals,
                ticks: {
                  display: true
                },
                gridLines: {
                  zeroLineColor: 'transparent',
                  drawTicks: false,
                  display: false,
                  drawBorder: false,
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
        })
      }
    )
  }

  getforPieChart(id, since_date, until_date, is_tw){
    this.pieChartService.getPieChartData(id, since_date, until_date, is_tw).subscribe(
      response => {
        let ids = response['data'].map(response => response.hashtags);
        let nmototal = response['data'].map(response => response.numero_filas);


        this.canvas = document.getElementById('pieChart');
        this.ctx = this.canvas.getContext('2d');

        this.gradientFill = this.ctx.createLinearGradient(0, 170, 0, 50);
        this.gradientFill.addColorStop(0, 'rgba(239, 158, 239, 1)');
        this.gradientFill.addColorStop(1, this.hexToRGB('#d782d9', 0.6));

        this.chart = new Chart(this.ctx, {
            type: 'pie',
            data: {
              labels: ids,
              datasets: [{
                pointBorderWidth: 2,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 1,
                pointRadius: 4,
                fill: true,
                borderWidth: 1,
                data: nmototal,
                borderAlign: 'center',
                backgroundColor: this.gradientFill,
                borderColor: '#FFF',
                pointBorderColor: '#FFF',
                pointBackgroundColor: '#d782d9'
              }]
            },
            options: {
              maintainAspectRatio: false,
              legend: {
                display: true
              },
              animation: {
                animateScale: true
              }
            }
        })
      }
    )
  }

  changeIntervalGraph() {
    if (this.is_dynamic === true) {
      this.getforIntervalGraph(this.id, this.since_date, this.until_date, this.is_tw, this.is_dynamic);
    }
  }

  ngOnDestroy() {}
  }


