import { Component, OnInit } from '@angular/core';
import {NgbDateStruct, NgbModal, ModalDismissReasons} from "@ng-bootstrap/ng-bootstrap";
import {TwitterService} from "./twitter.service";
import {Router} from "@angular/router";


@Component({
  selector: 'app-twitter',
  templateUrl: './twitter.component.html',
  styleUrls: ['./twitter.component.scss']
})
export class TwitterComponent implements OnInit {
  focus;
  focus1;
  is_tw: boolean;
  model: NgbDateStruct;
  model1: NgbDateStruct;
  constructor(private twitterService: TwitterService, private router: Router) { }


  ngOnInit() {
    this.is_tw = true;
    var body = document.getElementsByTagName('body')[0];
    body.classList.add('login-page');

    var navbar = document.getElementsByTagName('nav')[0];
    navbar.classList.add('navbar-transparent');
    var id = (<HTMLTextAreaElement> (document.getElementById('id'))).value;
    var since_date = (<HTMLTextAreaElement> (document.getElementById('since_date'))).value;
    var until_date = (<HTMLTextAreaElement> (document.getElementById('until_date'))).value;
    this.checkId(id, since_date, until_date);

  }

  checkId(id: string, since_date, until_date): boolean {
    id = id.trim()
    if (!id) {
      return ;
    }

    this.twitterService.checkIdInDataBase(id).subscribe( idInDB => {
      let booleano = idInDB['id'];

      if (booleano == true) {
        this.router.navigate(['examples/dashboard/', id, since_date, until_date, this.is_tw])
      }
      })

  }
}
