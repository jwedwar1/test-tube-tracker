import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SamplesComponent }      from './samples/samples.component';
import { DashboardComponent }   from './dashboard/dashboard.component';
import { SampleDetailComponent }  from './sample-detail/sample-detail.component';



const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'detail/:id', component: SampleDetailComponent },
  { path: 'samples', component: SamplesComponent }
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {


  
}
