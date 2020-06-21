import { BrowserAnimationsModule } from '@angular/platform-browser/animations'; // this is needed!
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';
import { ChartsModule } from 'ng2-charts';
import { ToastrModule } from 'ngx-toastr';
import { AppRoutingModule } from './app.routing';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { TranslateModule, TranslateLoader } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';
import { AppComponent } from './app.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import {LoginComponent} from './components/login/login.component';
import {ExamplesComponent} from './examples/examples.component';
import {RegisterComponent} from './components/register/register.component';
import {DashboardComponent} from './components/dashboard/dashboard.component';
import {MenuComponent} from './components/menu/menu.component';
import {TwitterComponent} from './components/twitter/twitter.component';
import {InstagramComponent} from './components/instagram/instagram.component';
import {InformationComponent} from './components/information/information.component';
import {TimeSeriesComponent} from './components/time-series/time-series.component';
import {CommonModule} from '@angular/common';
import {NouisliderModule} from 'ng2-nouislider';
import {JwBootstrapSwitchNg2Module} from 'jw-bootstrap-switch-ng2';
import {AgmCoreModule} from '@agm/core';
import {BrowserModule} from '@angular/platform-browser';
import {ComponentsComponent} from './components/components.component';
import {NucleoiconsComponent} from './components/nucleoicons/nucleoicons.component';

export function createTranslateLoader(http: HttpClient) {
  return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}

@NgModule({
    declarations: [
        AppComponent,
        NavbarComponent,
        LoginComponent,
        ExamplesComponent,
        RegisterComponent,
        DashboardComponent,
        MenuComponent,
        TwitterComponent,
        InstagramComponent,
        InformationComponent,
        TimeSeriesComponent,
        ComponentsComponent,
        NucleoiconsComponent
    ],
    imports: [
        CommonModule,
        FormsModule,
        NouisliderModule,
        JwBootstrapSwitchNg2Module,
        AgmCoreModule.forRoot({
            apiKey: 'YOUR_KEY_HERE',
            libraries: ['places']
        }),
        BrowserModule,
        BrowserAnimationsModule,
        NgbModule.forRoot(),
        RouterModule,
        ChartsModule,
        ToastrModule.forRoot(),
        AppRoutingModule,
        HttpClientModule,
        TranslateModule.forRoot({
        loader: {
          provide: TranslateLoader,
          useFactory: createTranslateLoader,
          deps: [HttpClient]
        }
        })
    ],
    providers: [],
    exports : [ComponentsComponent],
    bootstrap: [AppComponent]
})
export class AppModule { }
