import { Component } from '@angular/core';
import { Validators } from '@angular/forms';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {
  registry=({
    email:['', [Validators.required,Validators.email]],
    password:['',Validators.required],
  })
}
