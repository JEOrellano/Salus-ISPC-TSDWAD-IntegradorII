import { Component, OnInit } from '@angular/core';
import { SuscriptionService } from './../../services/suscription.service'
import { CreateSuscriptionDTO, Suscription } from 'src/app/model/suscription.model';

@Component({
  selector: 'app-suscripcion',
  templateUrl: './suscripcion.component.html',
  styleUrls: ['./suscripcion.component.css']
})
export class SuscripcionComponent implements OnInit{

  mySuscriptions: Suscription[] = [];

  choseSuscription: {} = {};

  constructor(private suscriptionService: SuscriptionService){
  }

  ngOnInit(): void {
    this.suscriptionService.getAllSuscriptions()
    .subscribe(data => {
      this.mySuscriptions = data
    })
  }

  getSuscription(){
    console.log(this.mySuscriptions)
  }


}
