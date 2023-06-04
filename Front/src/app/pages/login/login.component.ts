import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import {Router} from '@angular/router';
import { LoginService } from 'src/app/services/auth/login.service';
import { LoginRequest } from 'src/app/services/auth/loginRequest';
import { HttpClient } from '@angular/common/http';
import { User } from "../../services/auth/user";

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
  constructor(private formBuilder:FormBuilder, private router:Router, private loginService: LoginService, private http: HttpClient){}

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
          alert("correcto")
            this.router.navigateByUrl('/home');
        } else {
          alert("incorrecto")
        }
      }

        /* 
        {
        next: (userData) => {
          console.log(userData);
          const email = this.loginForm.value.email
          console.log(email)

        },
        error: (errorData) => {
          console.error(errorData);
          this.loginError=errorData;
        },
        complete: () => {
          console.info('login completo');
          this.router.navigateByUrl('/home');
          this.loginForm.reset()
        }
      }
        */
      })
    }else{
      this.loginForm.markAllAsTouched();
      alert('error al ingresar datos')
    }
  }

  
}
