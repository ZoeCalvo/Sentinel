import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class IntervalgraphService {
  intervalGraphUrl = 'http://127.0.0.1:5000/intervalGraph';
  constructor(private http: HttpClient) { }

  getIntervalGraphData(id: string, since_date: string, until_date: string, is_tw: string, is_dynamic: string) {
    const params = new HttpParams()
      .set('id', id)
      .set('since_date', since_date)
      .set('until_date', until_date)
      .set('is_tw', is_tw)
      .set('is_dynamic', is_dynamic);
    return this.http.get(this.intervalGraphUrl, {params: params})
  }
}

