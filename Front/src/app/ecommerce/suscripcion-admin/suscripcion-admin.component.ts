import { Component, OnInit } from '@angular/core';
import { Suscription } from 'src/app/model/suscription.model';
import { SuscriptionService } from 'src/app/services/suscription.service';

@Component({
  selector: 'app-suscripcion-admin',
  templateUrl: './suscripcion-admin.component.html',
  styleUrls: ['./suscripcion-admin.component.css']
})
export class SuscripcionAdminComponent implements OnInit {

  mySuscriptions: Suscription[] = [];

  constructor(private suscriptionService: SuscriptionService){}

  ngOnInit(): void {
    this.suscriptionService.getAllSuscriptions()
    .subscribe(data => {
      this.mySuscriptions = data
    })
  }

  editSuscription(id: number){
    
  }

}
