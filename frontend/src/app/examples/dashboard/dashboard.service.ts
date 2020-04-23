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

  analysis (id: Twitter){
    console.log(id);
    return this.http.post<Twitter>(this.graphsUrl, id);
  }
  readAnalysis(id: string ) {
    let params = new HttpParams().set('id', id);
    return this.http.get<Twitter>(this.graphsUrl, {params: params})
  }

}
