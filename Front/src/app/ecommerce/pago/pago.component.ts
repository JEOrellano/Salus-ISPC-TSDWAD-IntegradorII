import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators, FormArray } from '@angular/forms';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { SuscriptionService } from 'src/app/services/suscription.service';
import { Suscription } from 'src/app/model/suscription.model';
import { Ventas } from 'src/app/model/venta.model';
import { VentaService } from 'src/app/services/venta.service';

@Component({
  selector: 'app-pago',
  templateUrl: './pago.component.html',
  styleUrls: ['./pago.component.css']
})
export class PagoComponent {

  vencimiento: string = '';
  constructor(private formBuilder: FormBuilder, private router: Router, private ventaService: VentaService,
     private suscriptionService: SuscriptionService, private route: ActivatedRoute) { }
  idAuxiliar: number = 0;
  precioAuxiliar: number = 0;
  pacienteData: any = {};
  suscripcionActual: Suscription = {
    id: 0,
    Precio_S: 0,
    Descripcion_S: "",
    TipoServicio_S: ""
  };

  ngOnInit(): void {
    this.suscripcionActual = history.state.suscripcion
    this.precioAuxiliar = Math.floor(this.suscripcionActual.Precio_S)
    this.idAuxiliar = this.suscripcionActual.id

    const pacienteDataString = localStorage.getItem('pacienteData');
    if (pacienteDataString) {
      this.pacienteData = JSON.parse(pacienteDataString);
      console.log("Que paciente llega?")
      console.log(this.pacienteData)
    }
  }

  pagoForm = this.formBuilder.group({
    nroTarjeta: ["", [Validators.required]],
    vencimientoTarjeta: ["", [Validators.required]],
    codSeguridad: ["", [Validators.required]],
    nombre: ["", [Validators.required]],
    dni: ["", [Validators.required]],
    email:["", [Validators.required]]
  })

  get nroTarjeta(){
    return this.pagoForm.controls.nroTarjeta
  }

  get vencimientoTarjeta(){
    return this.pagoForm.controls.vencimientoTarjeta
  }

  get codSeguridad(){
    return this.pagoForm.controls.codSeguridad
  }

  get nombre(){
    return this.pagoForm.controls.nombre
  }

  get dni(){
    return this.pagoForm.controls.dni
  }

  get email(){
    return this.pagoForm.controls.email
  }


  nuevoPago(){
    if(this.pagoForm.valid){
      const ventas: Partial<Ventas> = {
        TotalVenta_V: this.precioAuxiliar,
        id_S: this.idAuxiliar,
        id_UP: this.pacienteData.id
      }

      this.ventaService.createVenta(ventas)
      .subscribe(data => {
        console.log("Data venta")
        console.log(data)
      })
      this.router.navigateByUrl('/adminPago');
      this.pagoForm.reset();
    }else {
      this.pagoForm.markAllAsTouched();
    }

  }



  formatVencimiento(): void {
    const maxLength = 5;
    let formattedValue = this.vencimiento.replace(/\D/g, '').substring(0, maxLength);

    if (formattedValue.length > 2) {
      const month = parseInt(formattedValue.substring(0, 2));

      // Validate month
      if (month < 1 || month > 12) {
        formattedValue = '12';
      }
    }

    if (formattedValue.length > 2 && formattedValue.charAt(2) !== '/') {
      formattedValue = formattedValue.substring(0, 2) + '/' + formattedValue.substring(2);
    }

    this.vencimiento = formattedValue;
  }

}
