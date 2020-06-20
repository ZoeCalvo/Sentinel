import { Component, OnInit } from '@angular/core';
import {Register} from './register';
import {RegisterService} from './register.service';
import {IAlert} from '../../components/notification/notification.component';
import {TranslateService} from "@ngx-translate/core";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  selectedLanguage;
  focus;
  focus1;
  regexpNombreApe = new RegExp('^[a-zA-Z ]+$')
  regexpUsuPass = new RegExp('^[a-zA-Z0-9_]+$')
  registers: Register[];
  public alerts: Array<IAlert> = [];

  constructor(private registerService: RegisterService, private router: Router, private route: ActivatedRoute) { }

    ngOnInit() {
      this.selectedLanguage = this.route.snapshot.paramMap.get('lang');
      this.getRegisters();
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

    getRegisters() {
      return this.registers;
    }

    add(name: string, surname: string, user: string, passwd: string): void {
      name = name.trim();
      surname = surname.trim();
      user = user.trim();
      passwd = passwd.trim();
      if (!name && !surname && !user && !passwd) {
          return;
      }
      if ( this.regexpNombreApe.test(name) && this.regexpNombreApe.test(surname)
        && this.regexpUsuPass.test(user) && this.regexpUsuPass.test(passwd)) {
        const newRegister: Register = { name, surname, user, passwd } as Register;
        this.registerService.addUser(newRegister).subscribe();
        this.router.navigate(['examples/login/', this.selectedLanguage])
      } else {
        if (this.selectedLanguage === 'es') {
          this.alerts.push({
            id: 1,
            type: 'warning',
            message: 'Caracter no permitido.',
            icon: 'ui-1_bell-53'
          })
        } else if (this.selectedLanguage === 'en') {
          this.alerts.push({
            id: 1,
            type: 'warning',
            message: 'Character not allowed.',
            icon: 'ui-1_bell-53'
          })
        }

      }
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
