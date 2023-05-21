import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Suscription } from '../model/suscription.model';

@Injectable({
  providedIn: 'root'
})
export class SuscriptionService {

  urlApi = "https://my-json-server.typicode.com/GastonSca/db-json/suscripciones"

  constructor(
    private http: HttpClient
  ) { }

  getAllSuscriptions(){
    return this.http.get<Suscription[]>(this.urlApi)
  }

  getSuscription(id: number){
    return this.http.get<Suscription>(`${this.urlApi}/${id}`)
  }

}
