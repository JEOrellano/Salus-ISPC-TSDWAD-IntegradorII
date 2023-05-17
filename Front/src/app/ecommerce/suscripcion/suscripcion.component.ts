import { Component, OnInit } from '@angular/core';
import { SuscriptionService } from './../../services/suscription.service'
import { Suscription } from 'src/app/model/suscription.model';

@Component({
  selector: 'app-suscripcion',
  //templateUrl: './suscripcion.component.html',
  template: `
    <div class="container mb-5 mt-2 " >
    <div class="row">
      <div class="col-lg-4" *ngFor="let dato of mySuscriptions">
        <div class="mb-5 mb-lg-0">
          <div class="card-body suscription-register">
            <h3 class="card-title text-muted text-uppercase text-center">
              {{dato.tipoServicio}}
            </h3>
            <h5 class="card-price text-center">
              {{dato.precio}}<span class="period">/mes</span>
            </h5>
            <hr />
            <ul class="fa-ul">
              <li *ngFor="let item of dato.descripcion">
                <span class="fa-li"><i class="fas fa-check"></i></span>{{item}}
              </li>
            </ul>
            <div class="d-grid">
              <a href="#" class="btn botons text-uppercase">Suscríbete</a>
            </div>
          </div>
        </div>
      </div>    
    </div>
  </div>
  `,
  styleUrls: ['./suscripcion.component.css']
})
export class SuscripcionComponent implements OnInit{

  mySuscriptions: Suscription[] = [];
 myServices: Suscription["descripcion"] = [];
  

  choseSuscription: {} = {};

  constructor(private suscriptionService: SuscriptionService){
  }

  ngOnInit(): void {
    this.suscriptionService.getAllSuscriptions()
    .subscribe(data => {
      this.mySuscriptions = data
      console.log(this.mySuscriptions)
    })
  }

  getSuscription(){
    console.log(this.mySuscriptions)
  }



  getSuscriptionOne(){
    let id = 3
    this.suscriptionService.getSuscription(id)
    .subscribe(data => {
      this.choseSuscription = data;
      console.log(this.choseSuscription)
    })
  }
  
}
