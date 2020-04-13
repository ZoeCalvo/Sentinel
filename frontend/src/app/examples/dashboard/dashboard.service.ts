import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Dashboard } from './dashboard'


@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  graphsUrl = 'http://127.0.0.1:5000/selecthashtag';

  constructor(private http: HttpClient) { }

  readAnalysis() {
    return this.http.get<Dashboard>(this.graphsUrl)
  }
}
