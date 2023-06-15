import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Suscription } from 'src/app/model/suscription.model';
import { SuscriptionService } from 'src/app/services/suscription.service';

@Component({
  selector: 'app-suscripcion-admin',
  templateUrl: './suscripcion-admin.component.html',
  styleUrls: ['./suscripcion-admin.component.css']
})
export class SuscripcionAdminComponent implements OnInit {

  mySuscriptions: Suscription[] = [];
  suscription: Suscription = {
    id: 0,
    Descripcion_S: "",
    TipoServicio_S: "",
    Precio_S: 0
  }

  constructor(private suscriptionService: SuscriptionService, private router: Router){}

  ngOnInit(): void {
    this.suscriptionService.getAllSuscriptions()
    .subscribe(data => {
      this.mySuscriptions = data
    })
  }

  editSuscription(data: Suscription){
    this.router.navigate(['/formSuscripcionEdit'], {state: {suscripcion: data}})
  }

  deleteSuscription(id: number){
    this.suscriptionService.deleteSuscription(id)
    .subscribe(data => {
      const productIndex = this.mySuscriptions.findIndex(item => item.id === id)
      this.mySuscriptions.splice(productIndex, 1);
    })
  }

}
