import {Component, OnInit} from '@angular/core';
import {NgbDateStruct} from '@ng-bootstrap/ng-bootstrap';
import {TwitterService} from './twitter.service';
import {Router} from '@angular/router';
import {IAlert} from '../../components/notification/notification.component';


@Component({
  selector: 'app-twitter',
  templateUrl: './twitter.component.html',
  styleUrls: ['./twitter.component.scss']
})
export class TwitterComponent implements OnInit {
  focus;
  focus1;
  is_tw: boolean;
  update_db: boolean;
  model: NgbDateStruct;
  model1: NgbDateStruct;
  regexpId = new RegExp('^[#@]{0,1}[a-zA-Z0-9_]+')
  public alerts: Array<IAlert> = [];

  constructor(private twitterService: TwitterService, private router: Router) {  }

  ngOnInit() {
    this.is_tw = true;
    const body = document.getElementsByTagName('body')[0];
    body.classList.add('login-page');

    const navbar = document.getElementsByTagName('nav')[0];
    navbar.classList.add('navbar-transparent');
  }

  checkId(id: string, since_date, until_date) {

    id = id.trim()
    if (!id) {
      return ;
    }

    if (this.regexpId.test(id) === true) {
      this.twitterService.checkIdInDataBase(id).subscribe(idInDB => {
        const booleano = idInDB['id'];

        if (booleano == true) {
          if (this.update_db == true) {
            this.alerts.push({
              id: 1,
              type: 'info',
              message: 'Esta acción puede tardar varios minutos.',
              icon: 'travel_info'
            })

            this.searchIdInTwitter(id, since_date, until_date);
          } else {
            this.router.navigate(['examples/dashboard/', id, since_date, until_date, this.is_tw])
          }
        } else {
          this.alerts.push({
            id: 1,
            type: 'info',
            message: 'El id no se encuentra en la base de datos.\n Esta acción puede tardar varios minutos.',
            icon: 'travel_info'
          })

          this.searchIdInTwitter(id, since_date, until_date);

        }
      })
    } else {
      this.alerts.push({
            id: 1,
            type: 'info',
            message: 'Ha introducido algún caracter no permitido.\n Solo se permiten al principio @ o # seguido de letras, números o _.',
            icon: 'travel_info'
          })
    }
  }

  searchIdInTwitter(id: string, since_date, until_date) {
    this.twitterService.searchIdInApi(id).subscribe(response => {
      this.router.navigate(['examples/dashboard/', id, since_date, until_date, this.is_tw])
    });

  }

  public closeAlert(alert: IAlert) {
    const index: number = this.alerts.indexOf(alert);
    this.alerts.splice(index, 1);
  }

  onItemSelect(item: any) {
    console.log(item);

  }

  OnItemDeSelect(item: any) {
    console.log(item);
  }

}
