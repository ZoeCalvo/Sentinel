import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Login } from './login';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  loginUrl = 'http://127.0.0.1:5000/login';
  constructor( private http: HttpClient) { }

  login(user: Login) {
    return this.http.post<Login>(this.loginUrl, user);
  }
}
