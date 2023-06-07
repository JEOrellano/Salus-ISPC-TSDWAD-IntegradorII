import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import {Router} from '@angular/router';
import { LoginService } from 'src/app/services/auth/login.service';
import { HttpClient } from '@angular/common/http';
import { User } from "../../services/auth/user";
import { SharedServicesComponent } from 'src/app/services/auth/shared-services/shared-services.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  myUsers: User[] = [];
  loginError:string="";
  loginForm=this.formBuilder.group({
    email:['', [Validators.required,Validators.email]],
    password:['',Validators.required],
  })
  constructor(private formBuilder:FormBuilder, private router:Router, private loginService: LoginService, private http: HttpClient, private sharedService: SharedServicesComponent){}

  ngOnInit(): void{}

  get email(){
    return this.loginForm.controls.email;
  }

  get password(){
    return this.loginForm.controls.password;
  }

  login(){
    if(this.loginForm.valid){
      this.loginService.login().subscribe(data => {
        this.myUsers = data
       const user = this.myUsers.find((user) => {
        return this.loginForm.value.email === user.Email_UP
      })
      console.log(user)
        if(user){
          if (user.Clave_UP === this.loginForm.value.password) {
              this.router.navigateByUrl('/home');
              this.sharedService.isLoggedIn = true;
          } else {
            alert("contraseña incorrecta")
          }
        }
      })
    }else{
      this.loginForm.markAllAsTouched();
      alert('error al ingresar datos')
    }
  }

  
}
