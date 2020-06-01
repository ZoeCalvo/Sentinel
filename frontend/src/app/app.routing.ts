import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule  } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';

import { ComponentsComponent } from './components/components.component';
import { LandingComponent } from './examples/landing/landing.component';
import { LoginComponent } from './examples/login/login.component';
import { ProfileComponent } from './examples/profile/profile.component';
import { NucleoiconsComponent } from './components/nucleoicons/nucleoicons.component';
import {RegisterComponent} from './examples/register/register.component';
import {DashboardComponent} from './examples/dashboard/dashboard.component';
import {TableListComponent} from './examples/table-list/table-list.component';
import {MenuComponent} from "./examples/menu/menu.component";
import {TwitterComponent} from "./examples/twitter/twitter.component";
import {InstagramComponent} from "./examples/instagram/instagram.component";
import {InformationComponent} from "./examples/information/information.component";

const routes: Routes =[
    { path: '', redirectTo: 'index', pathMatch: 'full' },
    { path: 'index',                component: ComponentsComponent },
    { path: 'nucleoicons',          component: NucleoiconsComponent },
    { path: 'examples/landing',     component: LandingComponent },
    { path: 'examples/login',       component: LoginComponent },
    { path: 'examples/profile',     component: ProfileComponent },
    { path: 'examples/register',    component: RegisterComponent},
    { path: 'examples/dashboard/:id/:since_date/:until_date/:is_tw',   component: DashboardComponent},
    { path: 'examples/table-list',  component: TableListComponent},
    { path: 'examples/menu',        component: MenuComponent},
    { path: 'examples/twitter',     component: TwitterComponent},
    { path: 'examples/instagram',   component: InstagramComponent},
    { path: 'examples/information', component: InformationComponent}
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
