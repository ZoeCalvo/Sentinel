import { Component, OnInit } from '@angular/core';
import {Register} from './register';
import {RegisterService} from './register.service';
import {IAlert} from '../../components/notification/notification.component';
import {TranslateService} from "@ngx-translate/core";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  selectedLanguage = 'es';
  focus;
  focus1;
  regexpNombreApe = new RegExp('[a-zA-Z]+')
  regexpUsuPass = new RegExp('[a-zA-Z0-9_]+')
  registers: Register[];
  public alerts: Array<IAlert> = [];

  constructor(private registerService: RegisterService, private translateService: TranslateService) {
    this.translateService.setDefaultLang(this.selectedLanguage);
    this.translateService.use(this.selectedLanguage);
  }

    ngOnInit() {
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
        this.registerService.addUser(newRegister).subscribe(register => this.registers.push(register));
        window.location.assign('examples/login')
      } else {
        this.alerts.push({
            id: 1,
            type: 'warning',
            message: 'Caracter no permitido.',
            icon: 'ui-1_bell-53'
          })
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
    selectLanguage(lang: string) {
      this.translateService.use(lang);
    }
}
