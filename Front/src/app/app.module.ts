import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule} from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import { FooterComponent } from './shared/footer/footer.component';
import { HomeComponent } from './pages/home/home.component';
import { NosotrosComponent } from './pages/nosotros/nosotros.component';
import { ContactoComponent } from './pages/contacto/contacto.component';
import { LoginComponent } from './pages/login/login.component';
import { SuscripcionComponent } from './ecommerce/suscripcion/suscripcion.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormComponent } from './ecommerce/form/form.component';
import { MedicoComponent } from './pages/medico/medico.component';
import { PacienteComponent } from './pages/paciente/paciente.component';
import { SuscripcionAdminComponent } from './ecommerce/suscripcion-admin/suscripcion-admin.component';
import { FormEditComponent } from './ecommerce/form-edit/form-edit.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    HomeComponent,
    NosotrosComponent,
    ContactoComponent,
    SuscripcionComponent,
    LoginComponent,
    FormComponent,
    MedicoComponent,
    PacienteComponent,
    SuscripcionAdminComponent,
    FormEditComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
