import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NouisliderModule } from 'ng2-nouislider';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { JwBootstrapSwitchNg2Module } from 'jw-bootstrap-switch-ng2';
import { AgmCoreModule } from '@agm/core';
import { ChartsModule } from 'ng2-charts';

import { LandingComponent } from './landing/landing.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { ExamplesComponent } from './examples.component';
import { RegisterComponent } from './register/register.component';
import { ConfigComponent } from './config/config.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { TableListComponent } from './table-list/table-list.component';

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
        })
    ],
    declarations: [
        LandingComponent,
        LoginComponent,
        ExamplesComponent,
        ProfileComponent,
        RegisterComponent,
        ConfigComponent,
        DashboardComponent,
        TableListComponent
    ]
})
export class ExamplesModule { }
