import { Component, OnInit } from '@angular/core';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { NgbAccordionConfig } from '@ng-bootstrap/ng-bootstrap';
import {TranslateService} from "@ngx-translate/core";


@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {
  selectedLanguage = 'es';
  constructor(private translateService: TranslateService) {
      this.translateService.setDefaultLang(this.selectedLanguage);
      this.translateService.use(this.selectedLanguage);
  }

  ngOnInit() {
      var navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
      var body = document.getElementsByTagName('body')[0];
      body.classList.add('index-page');
  }

  selectLanguage(lang: string) {
    this.translateService.use(lang);
  }

}
