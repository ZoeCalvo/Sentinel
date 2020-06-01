import { Component, OnInit } from '@angular/core';
import {Config, ConfigService} from './config.service';

@Component({
  selector: 'app-config',
  templateUrl: './config.component.html',
  styleUrls: ['./config.component.scss']
})
export class ConfigComponent implements OnInit {
  config: Config;
  constructor( private configService: ConfigService) { }

  ngOnInit(): void {
    var body = document.getElementsByTagName('body')[0];
      body.classList.add('login-page');

      var navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
  }

  showConfig() {
    this.configService.getConfig().subscribe((data: Config) => this.config = {
      registerUrl: (data as any).registerUrl,
      apiUrl: (data as any).apiUrl
    });
  }

}
