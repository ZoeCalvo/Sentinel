import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GraphsService {
  graphs_Url = 'http://127.0.0.1:5000/getDataforGraphs';
  constructor(private http: HttpClient) { }

  getforGraphs(id: string, since_date: string, until_date: string, is_tw: string) {
    const params = new HttpParams()
      .set('id', id)
      .set('since_date', since_date)
      .set('until_date', until_date)
      .set('is_tw', is_tw);
    return this.http.get(this.graphs_Url, {params: params})
  }
}
