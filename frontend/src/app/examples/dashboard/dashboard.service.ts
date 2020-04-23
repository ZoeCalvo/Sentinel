import { Injectable } from '@angular/core';
import { HttpClient, HttpParams} from '@angular/common/http';
import { Dashboard } from './dashboard'
import {Observable} from "rxjs";
import {Twitter} from "../twitter/twitter";



@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  graphsUrl = 'http://127.0.0.1:5000/getDataforDashboard';

  constructor(private http: HttpClient) { }

  readAnalysis(id: string, since_date: string, until_date: string) {
    const params = new HttpParams()
      .set('id', id)
      .set('since_date', since_date)
      .set('until_date', until_date);
    console.log(params);
    return this.http.get(this.graphsUrl, {params: params})
  }

}
