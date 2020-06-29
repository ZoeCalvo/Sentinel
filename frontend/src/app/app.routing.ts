import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule  } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';
import { ComponentsComponent } from './components/components.component';
import { LoginComponent } from './components/login/login.component';
import {RegisterComponent} from './components/register/register.component';
import {DashboardComponent} from './components/dashboard/dashboard.component';
import {MenuComponent} from './components/menu/menu.component';
import {TwitterComponent} from './components/twitter/twitter.component';
import {InstagramComponent} from './components/instagram/instagram.component';
import {InformationComponent} from './components/information/information.component';
import {TimeSeriesComponent} from './components/time-series/time-series.component';

const routes: Routes = [
    { path: '', redirectTo: 'index', pathMatch: 'full' },
    { path: 'index',                component: ComponentsComponent },
    { path: 'login/:lang',       component: LoginComponent },
    { path: 'register/:lang',    component: RegisterComponent},
    { path: 'dashboard/:id/:since_date/:until_date/:is_tw/:lang',   component: DashboardComponent},
    { path: 'menu/:lang',        component: MenuComponent},
    { path: 'twitter/:lang',     component: TwitterComponent},
    { path: 'instagram/:lang',   component: InstagramComponent},
    { path: 'information/:lang', component: InformationComponent},
    { path: 'time-series/:id/:since_date/:until_date/:is_tw/:lang',   component: TimeSeriesComponent}
];

@NgModule({
    imports: [
        CommonModule,
        BrowserModule,
        RouterModule.forRoot(routes)
    ],
    exports: [
    ],
})
export class AppRoutingModule { }
