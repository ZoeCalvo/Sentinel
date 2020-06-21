import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})

export class InstagramService {
  instagramUrl = 'http://127.0.0.1:5000/idInstagramInDB';
  searchInstagramUrl = 'http://127.0.0.1:5000/searchInstagram';
  constructor(private http: HttpClient) { }

  checkIdInDataBase(id: string) {
    const params = new HttpParams().set('id', id);
    return this.http.get(this.instagramUrl, {params: params});
  }

  searchIdInApi(id: string) {
    const params = new HttpParams().set('id', id);
    return this.http.get(this.searchInstagramUrl, {params: params})
  }
}
