import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { NosotrosComponent } from './pages/nosotros/nosotros.component';
import { ContactoComponent } from './pages/contacto/contacto.component';
import { RegistroComponent } from './pages/registro/registro.component';
import { LoginComponent } from './pages/login/login.component';
import { SuscripcionComponent } from './ecommerce/suscripcion/suscripcion.component';
import { FormComponent } from './ecommerce/form/form.component';
import { CuentaComponent } from './pages/cuenta/cuenta.component';
import { SuscripcionAdminComponent } from './ecommerce/suscripcion-admin/suscripcion-admin.component';

const routes: Routes = [
  {path:'home', component:HomeComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path:'nosotros', component:NosotrosComponent},
  {path:'contacto', component:ContactoComponent},
  {path:'registro', component:RegistroComponent},
  {path:'suscripcion', component:SuscripcionComponent},
  {path:'login', component:LoginComponent},
  {path:'formSuscripcion', component:FormComponent},
  {path:'cuenta', component:CuentaComponent},
  {path: 'adminSuscripcion', component:SuscripcionAdminComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
