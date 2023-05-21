import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Client } from './../model/client.model'

@Injectable({
  providedIn: 'root'
})
export class ClientService {

  urlApi = "https://my-json-server.typicode.com/GastonSca/db-json/pacientes"

  constructor(
    private http: HttpClient
  ) { }

  getAllClients(){
    return this.http.get<Client[]>(this.urlApi)
  }

  getClient(id: string){
    return this.http.get<Client>(`${this.urlApi}/${id}`)
  }

}

