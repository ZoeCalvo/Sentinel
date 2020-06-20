import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule  } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';

import { ComponentsComponent } from './components/components.component';
import { LoginComponent } from './examples/login/login.component';
import {RegisterComponent} from './examples/register/register.component';
import {DashboardComponent} from './examples/dashboard/dashboard.component';
import {MenuComponent} from './examples/menu/menu.component';
import {TwitterComponent} from './examples/twitter/twitter.component';
import {InstagramComponent} from './examples/instagram/instagram.component';
import {InformationComponent} from './examples/information/information.component';
import {TimeSeriesComponent} from './examples/time-series/time-series.component';

const routes: Routes = [
    { path: '', redirectTo: 'index', pathMatch: 'full' },
    { path: 'index',                component: ComponentsComponent },
    { path: 'examples/login/:lang',       component: LoginComponent },
    { path: 'examples/register/:lang',    component: RegisterComponent},
    { path: 'examples/dashboard/:id/:since_date/:until_date/:is_tw/:lang',   component: DashboardComponent},
    { path: 'examples/menu/:lang',        component: MenuComponent},
    { path: 'examples/twitter/:lang',     component: TwitterComponent},
    { path: 'examples/instagram/:lang',   component: InstagramComponent},
    { path: 'examples/information/:lang', component: InformationComponent},
    { path: 'examples/time-series/:id/:since_date/:until_date/:is_tw/:lang',   component: TimeSeriesComponent}
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
