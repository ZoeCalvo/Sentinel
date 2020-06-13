import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";

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
  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
      this.id = this.route.snapshot.paramMap.get('id');
      this.since_date = this.route.snapshot.paramMap.get('since_date');
      this.until_date = this.route.snapshot.paramMap.get('until_date');
      this.is_tw = this.route.snapshot.paramMap.get('is_tw');
      if (this.typeTimeSerie != undefined && this.schema != undefined && this.periods != undefined) {
        this.typeTimeSerie = this.typeTimeSerie.trim();
        this.schema = this.schema.trim();
        this.periods = this.periods.trim();
        if (!this.typeTimeSerie || !this.schema || !this.periods) {
          return ;
        } else {
          this.calculateTimeSeries(this.typeTimeSerie, this.schema, this.periods);
        }
      }
  }

  calculateTimeSeries(type, schema, num_periods){
      console.log(this.typeTimeSerie)
      console.log(this.schema)
      console.log(this.periods)
  }
}
