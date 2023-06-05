import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import {Router} from '@angular/router';
import { RegistryService } from 'src/app/services/auth/registry.service';
import { HttpClient } from '@angular/common/http';
import { RegistryRequest } from "../../services/auth/registryRequest";

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit{
 
  loginError:string="";
  registryForm=this.formBuilder.group({
    Nombre_UP:['', Validators.required],
    Apellido_UP:['', Validators.required],
    Email_UP:['', [Validators.required,Validators.email]],
    Clave_UP:['',Validators.required],
    id_C: 2
  })
  

  constructor(private formBuilder:FormBuilder, private registryService: RegistryService, private router:Router){}
  
  ngOnInit(): void{}

  registry(){
    if(this.registryForm.valid){
      this.registryService.createUser(this.registryForm.value as RegistryRequest).subscribe(data => {
        console.log(data)
        this.router.navigateByUrl('/home');
      })

    } 
  }
}
