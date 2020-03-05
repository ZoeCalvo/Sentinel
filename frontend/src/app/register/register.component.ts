import { Component, OnInit } from '@angular/core';
import {Register} from './register';
import {RegisterService} from './register.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registers: Register[];
  constructor(private registerService: RegisterService) { }

  ngOnInit(): void {
    this.getRegisters();
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

    this.registerService.addUser(newRegister)
      .subscribe(register => this.registers.push(register));
  }
}
