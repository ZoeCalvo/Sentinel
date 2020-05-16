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
        var body = document.getElementsByTagName('body')[0];
        body.classList.add('login-page');

        var navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.add('navbar-transparent');

        var user = (<HTMLTextAreaElement> (document.getElementById('username'))).value;
        var passwd = (<HTMLTextAreaElement> (document.getElementById('passwd'))).value;
        this.checkUser(user, passwd);

    }
    ngOnDestroy(){
        var body = document.getElementsByTagName('body')[0];
        body.classList.remove('login-page');

        var navbar = document.getElementsByTagName('nav')[0];
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
        let booleano = login['resultado'];

        if (booleano == true){
          window.location.assign('examples/menu')
          this.alerts.push({
            id: 1,
            type: 'success',
            strong: 'Welcome back',
            message: username,
            icon: 'ui-2_like'
          });

        } else {
          document.getElementById('passwd').remove();
          this.alerts.push({
            id: 2,
            type: 'warning',
            strong: 'Warning!',
            message: 'The username or password is not correct',
            icon: 'ui-1_bell-53'
          })
        }

      });

      var body = document.getElementsByTagName('body')[0];
      body.classList.add('login-page');

      var navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
    }

    public closeAlert(alert: IAlert) {
        const index: number = this.alerts.indexOf(alert);
        this.alerts.splice(index, 1);
    }
}
