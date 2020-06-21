import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class TimeSeriesService {
  timeSeriesUrl = 'http://127.0.0.1:5000/timeSerie';

  constructor(private http: HttpClient) { }

  timeSerieChart(id: string, since_date: string, until_date: string, is_tw: string, type: string, schema: string, num_periods){
    const params = new HttpParams()
      .set('id', id)
      .set('since_date', since_date)
      .set('until_date', until_date)
      .set('is_tw', is_tw)
      .set('type', type)
      .set('schema', schema)
      .set('num_periods', num_periods);

    return this.http.get(this.timeSeriesUrl, {params: params});
  }
}
