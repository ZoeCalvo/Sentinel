import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Twitter } from './twitter';

@Injectable({
  providedIn: 'root'
})
export class TwitterService {
  twitterUrl = 'http://127.0.0.1:5000/twitter';
  constructor( private http: HttpClient ) { }

  postId(id: Twitter) {
    return this.http.post<Twitter>(this.twitterUrl, id);
  }
}
