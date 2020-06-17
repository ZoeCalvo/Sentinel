import { Component, OnInit } from '@angular/core';
import { Login } from './login';
import { LoginService } from './login.service';
import {IAlert} from '../../components/notification/notification.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

    data: Date = new Date();
    focus;
    focus1;
    public alerts: Array<IAlert> = [];

    constructor( private loginService: LoginService ) { }

    ngOnInit() {
        const body = document.getElementsByTagName('body')[0];
        body.classList.add('login-page');

        const navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.add('navbar-transparent');

        const user = (<HTMLTextAreaElement> (document.getElementById('username'))).value;
        const passwd = (<HTMLTextAreaElement> (document.getElementById('passwd'))).value;
        this.checkUser(user, passwd);

    }
    ngOnDestroy() {
        const body = document.getElementsByTagName('body')[0];
        body.classList.remove('login-page');

        const navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.remove('navbar-transparent');
    }

    checkUser(username: string, passwd: string): void {
      username = username.trim();
      passwd = passwd.trim();
      if (!username && !passwd) {
          return;
      }


      const newLogin: Login = { username, passwd } as Login;
      this.loginService.login(newLogin).subscribe(login => {
        const booleano = login['resultado'];

        if (booleano === true) {
          window.location.assign('examples/menu')
          this.alerts.push({
            id: 1,
            type: 'success',
            strong: 'Bienvenido',
            message: username,
            icon: 'ui-2_like'
          });

        } else {

          this.alerts.push({
            id: 2,
            type: 'warning',
            strong: 'Warning!',
            message: 'El usuario o la contraseña no son correctos',
            icon: 'ui-1_bell-53'
          })
        }

      });

      const body = document.getElementsByTagName('body')[0];
      body.classList.add('login-page');

      const navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
    }

    public closeAlert(alert: IAlert) {
        const index: number = this.alerts.indexOf(alert);
        this.alerts.splice(index, 1);
    }
}
