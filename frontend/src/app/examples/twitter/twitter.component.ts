import { Component, OnInit } from '@angular/core';
import { Twitter } from './twitter';
import { TwitterService } from './twitter.service';

@Component({
  selector: 'app-twitter',
  templateUrl: './twitter.component.html',
  styleUrls: ['./twitter.component.scss']
})
export class TwitterComponent implements OnInit {
  focus;
  focus1;
  constructor( private twitterService: TwitterService ) { }

  ngOnInit() {
    var body = document.getElementsByTagName('body')[0];
    body.classList.add('login-page');

    var navbar = document.getElementsByTagName('nav')[0];
    navbar.classList.add('navbar-transparent');
  }

  searchId(id: string, since_date: Date, until_date: Date): void {
    id = id.trim();
    if (!id) { return ; }
    const newId: Twitter = { id, since_date, until_date } as Twitter;
    this.twitterService.postId(newId).subscribe();
  }

}
