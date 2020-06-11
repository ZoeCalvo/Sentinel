import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NouisliderModule } from 'ng2-nouislider';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { JwBootstrapSwitchNg2Module } from 'jw-bootstrap-switch-ng2';
import { AgmCoreModule } from '@agm/core';
import { ChartsModule } from 'ng2-charts';
import { RouterModule } from '@angular/router'
import { LoginComponent } from './login/login.component';
import { ExamplesComponent } from './examples.component';
import { RegisterComponent } from './register/register.component';
import { ConfigComponent } from './config/config.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import {DashboardService} from './dashboard/dashboard.service';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from '../app.routing';
import {HttpClientModule} from '@angular/common/http';
import { MenuComponent } from './menu/menu.component';
import { TwitterComponent } from './twitter/twitter.component';
import { InstagramComponent } from './instagram/instagram.component';
import {InformationComponent} from "./information/information.component";

@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        NgbModule,
        NouisliderModule,
        ChartsModule,
        JwBootstrapSwitchNg2Module,
        AgmCoreModule.forRoot({
            apiKey: 'YOUR_KEY_HERE',
            libraries: ['places']
        }),
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        RouterModule
    ],
    declarations: [
        LoginComponent,
        ExamplesComponent,
        RegisterComponent,
        ConfigComponent,
        DashboardComponent,
        MenuComponent,
        TwitterComponent,
        InstagramComponent,
        InformationComponent
    ],
  providers: [DashboardService]
})
export class ExamplesModule { }
