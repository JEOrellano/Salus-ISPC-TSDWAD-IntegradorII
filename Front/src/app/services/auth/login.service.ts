import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError, catchError, map } from 'rxjs'
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }
/* 
  login(credentials:LoginRequest):Observable<User>{
    const url = "/api/v1/usuariospacientes"
    
    return this.http.get<User>(url).pipe(
      catchError(this.handleError)
    )
  } */

  login(){
    const url = "/api/v1/usuariospacientes"
    
    return this.http.get<User[]>(url)
    .pipe(
      /* map(users => users.map(item => {
        return{
          ...item,
        }
      })) */
    )
  }

  private handleError(error:HttpErrorResponse){
    if(error.status===0){
      console.error('se ha producido un error', error.error)
    }else{
      console.error('backend retorno el codigo de estado', error.status, error.error)
    }
    return throwError(() => new Error('algo fallo'))
  }
}
