import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Register} from './register';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  registerUrl = 'http://127.0.0.1:5000/register';
  constructor( private http: HttpClient) { }

  addUser(user: Register) {
    return this.http.post<Register>(this.registerUrl, user);
  }

  onNotify() {
      window.alert('User register properly!');
  }
}
