import { Component, OnInit } from '@angular/core';
import { Login } from './login';
import { LoginService } from './login.service';
import {Register} from "../register/register";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

    data: Date = new Date();
    focus;
    focus1;
    logins: Login[];

    constructor( private loginService: LoginService ) { }

    ngOnInit() {
        this.getLogins();
        var body = document.getElementsByTagName('body')[0];
        body.classList.add('login-page');

        var navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.add('navbar-transparent');
    }
    ngOnDestroy(){
        var body = document.getElementsByTagName('body')[0];
        body.classList.remove('login-page');

        var navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.remove('navbar-transparent');
    }

    getLogins() {
      return this.logins;
    }

    add(username: string, passwd: string): void {
      username = username.trim();
      passwd = passwd.trim();
      if (!username && !passwd) {
          return;
      }
      const newLogin: Login = { username, passwd } as Login;
      this.loginService.login(newLogin).subscribe(login => {
        let booleano = login['resultado'];

        if (booleano == true){
          console.log('Acceso permitido');
        }else{
          console.log('No existe la cuenta, registrese primero');
        }
      });

      var body = document.getElementsByTagName('body')[0];
      body.classList.add('login-page');

      var navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
    }


}
