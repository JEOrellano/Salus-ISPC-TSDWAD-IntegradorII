import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { CreateSuscriptionDTO, Suscription } from '../model/suscription.model';
import { map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SuscriptionService {

  // urlApi = "https://my-json-server.typicode.com/GastonSca/db-json/suscripciones"
  urlApi = "api/v1/servicios/"

  constructor(
    private http: HttpClient
  ) { }

  getAllSuscriptions(){
    return this.http.get<Suscription[]>(this.urlApi)
    .pipe(
      map(suscripciones => suscripciones.map(item => {
        return{
          ...item,
          DescripcionList: item.Descripcion_S.split(";")
        }
      }))
    )
  }

  getSuscription(id: number){
    return this.http.get<Suscription>(`${this.urlApi}/${id}`)
  }

  createSuscription(data:CreateSuscriptionDTO){
    return this.http.post<CreateSuscriptionDTO>(this.urlApi, data);
  }

}
