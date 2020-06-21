import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StatisticsService {
  statisticsUrl = 'http://127.0.0.1:5000/statistics';
  constructor(private http: HttpClient) { }

  getStatisticsData(id: string) {
    const params = new HttpParams()
      .set('id', id)
    return this.http.get(this.statisticsUrl, {params: params});
  }
}
