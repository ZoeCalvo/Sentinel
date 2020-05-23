import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TwitterService {
  twitterUrl = 'http://127.0.0.1:5000/twitter';
  constructor(private http: HttpClient) { }

  checkIdInDataBase(id: string) {
    const params = new HttpParams().set('id', id);
    return this.http.get(this.twitterUrl, {params: params});
  }
}
