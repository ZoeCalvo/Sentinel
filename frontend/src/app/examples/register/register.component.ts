import { Component, OnInit } from '@angular/core';
import {Register} from './register';
import {RegisterService} from './register.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  focus;
  focus1;
  registers: Register[];

  constructor(private registerService: RegisterService) { }

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
          const newRegister: Register = { name, surname, user, passwd } as Register;
          console.log('Soy el registro nuevo', newRegister);
          this.registerService.addUser(newRegister).subscribe(register => this.registers.push(register));
                var body = document.getElementsByTagName('body')[0];
      body.classList.add('login-page');

      var navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
    }

}
