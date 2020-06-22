import { Component, OnInit } from '@angular/core';
import {NgbDateStruct} from '@ng-bootstrap/ng-bootstrap';
import {IAlert} from '../../components/notification/notification.component';
import {InstagramService} from './instagram.service';
import {ActivatedRoute, Router} from '@angular/router';



@Component({
  selector: 'app-instagram',
  templateUrl: './instagram.component.html',
  styleUrls: ['./instagram.component.scss']
})
export class InstagramComponent implements OnInit {
  focus;
  focus1;
  is_tw: boolean;
  update_db: boolean;
  regexpId = new RegExp('^[a-zA-Z0-9_]+$')
  model: NgbDateStruct;
  model1: NgbDateStruct;
  selectedLanguage;
  public alerts: Array<IAlert> = [];

  constructor(private instagramService: InstagramService, private router: Router, private route: ActivatedRoute) { }

  ngOnInit() {
    this.selectedLanguage = this.route.snapshot.paramMap.get('lang');
    this.is_tw = false;
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
    this.instagramService.checkIdInDataBase(id).subscribe( idInDB => {
      const booleano = idInDB['id'];

      if (booleano === true) {
        if (this.update_db === true) {
          if (this.selectedLanguage === 'es') {
              this.alerts.push({
                id: 1,
                type: 'info',
                message: 'Esta acción puede tardar varios minutos.',
                icon: 'travel_info'
              })
          } else if (this.selectedLanguage === 'en') {
              this.alerts.push({
                id: 1,
                type: 'info',
                message: 'This action may take several minutes.',
                icon: 'travel_info'
              })
          }
          this.searchIdInInstagram(id, since_date, until_date);
        } else {
          this.router.navigate(['dashboard/', id, since_date, until_date, this.is_tw, this.selectedLanguage])
        }
      } else {
        if (this.selectedLanguage === 'es') {
              this.alerts.push({
              id: 1,
              type: 'info',
              message: 'El id no se encuentra en la base de datos.\n Esta acción puede tardar varios minutos.',
              icon: 'travel_info'
            })
        } else if (this.selectedLanguage === 'en') {
            this.alerts.push({
              id: 1,
              type: 'info',
              message: 'The id is not in database.\n This action may take several minutes.',
              icon: 'travel_info'
            })
        }

        this.searchIdInInstagram(id, since_date, until_date);

      }
      })
    } else {
       if (this.selectedLanguage === 'es') {
          this.alerts.push({
              id: 1,
              type: 'warning',
              message: 'Ha introducido algún carácter no permitido.\n Solo se permiten números, letras o _.',
              icon: 'travel_info'
          })
        } else if (this.selectedLanguage === 'en') {
          this.alerts.push({
              id: 1,
              type: 'warning',
              message: 'You have entered some illegal character.\n' +
                ' Only are allowed letters, numbers or _.',
              icon: 'travel_info'
          })
        }
    }

  }

  searchIdInInstagram(id: string, since_date, until_date) {
    this.instagramService.searchIdInApi(id).subscribe(response => {
      const booleano = response['userExists']

      if (booleano === false) {
        if (this.selectedLanguage === 'es') {
          this.alerts.push({
            id: 1,
            type: 'warning',
            message: 'El usuario no existe.',
            icon: 'travel_info'
          })
        } else if (this.selectedLanguage === 'en') {
          this.alerts.push({
            id: 1,
            type: 'warning',
            message: 'Username does not exist.',
            icon: 'travel_info'
          })
        }

      } else {
        this.router.navigate(['dashboard/', id, since_date, until_date, this.is_tw, this.selectedLanguage])
      }

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
