import { Component, OnInit } from '@angular/core';
import { Ventas } from 'src/app/model/venta.model';
import { ClientService } from 'src/app/services/client.service';
import { SuscriptionService } from 'src/app/services/suscription.service';
import { VentaService } from 'src/app/services/venta.service';

@Component({
  selector: 'app-pago-admin',
  templateUrl: './pago-admin.component.html',
  styleUrls: ['./pago-admin.component.css']
})
export class PagoAdminComponent implements OnInit{

  myVentas: Ventas[] = []
  constructor(private ventaService: VentaService, private clientService: ClientService, private suscriptionService: SuscriptionService){}

  ngOnInit(): void {
    this.ventaService.getAllVentas()
    .subscribe(data => {
      this.myVentas = data
      console.log("como queda myventas")
      console.log(this.myVentas)
    })
  }

  dataSuscription(){
  }

  dataClient(){}

}
