import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { SuscriptionService } from './../../services/suscription.service'
import { CreateSuscriptionDTO, Suscription } from 'src/app/model/suscription.model';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent {

  suscripcionForm = this.formBuilder.group({
    TipoServicio_S: [ "", [Validators.required, Validators.maxLength(25), Validators.minLength(4)]],
    Precio_S:[0 , [Validators.required, Validators.min(2000)]],
    Descripcion_S:["", [Validators.required, Validators.maxLength(200), Validators.minLength(5)]],
  })

  constructor(private formBuilder: FormBuilder, private router:Router, private suscriptionService: SuscriptionService){ }

  get TipoServicio_S(){
    return this.suscripcionForm.controls.TipoServicio_S;
  }

  get Precio_S(){
    return this.suscripcionForm.controls.Precio_S;
  }

  get Descripcion_S(){
    return this.suscripcionForm.controls.Descripcion_S;
  }

  nuevaSuscripcion(){
    if(this.suscripcionForm.valid){
      console.log("form valido")
      const data = this.suscripcionForm.value
      console.log(data)
      this.suscriptionService.createSuscription(data as CreateSuscriptionDTO)
      .subscribe(data => {
        console.log("La info llego, es la siguiente")
        console.log(data)
      })
      this.router.navigateByUrl('/suscripcion');
      this.suscripcionForm.reset();
    }else{
      this.suscripcionForm.markAllAsTouched();
    }
  }

}
