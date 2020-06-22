import { Component, OnInit, Renderer, OnDestroy } from '@angular/core';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { NgbAccordionConfig } from '@ng-bootstrap/ng-bootstrap';
import * as Rellax from 'rellax';


@Component({
    selector: 'app-components',
    templateUrl: './components.component.html',
    styles: [`
    ngb-progressbar {
        margin-top: 5rem;
    }
    `]
})

export class ComponentsComponent implements OnInit, OnDestroy {
    data: Date = new Date();
    selectedLanguage = 'es';
    page = 4;
    focus;


    date: {year: number, month: number};

    constructor( private renderer: Renderer, config: NgbAccordionConfig) {
        config.closeOthers = true;
        config.type = 'info';

    }

    ngOnInit() {
      let rellaxHeader = new Rellax('.rellax-header');
      let navbar = document.getElementsByTagName('nav')[0];
      navbar.classList.add('navbar-transparent');
      let body = document.getElementsByTagName('body')[0];
      body.classList.add('index-page');
    }
    ngOnDestroy() {
        let navbar = document.getElementsByTagName('nav')[0];
        navbar.classList.remove('navbar-transparent');
        let body = document.getElementsByTagName('body')[0];
        body.classList.remove('index-page');
    }
}
