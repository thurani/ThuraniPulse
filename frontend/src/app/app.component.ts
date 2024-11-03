import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  newuser = "";

  users:any = []

  APIURL = "http://localhost:8000/";

  constructor(private http:HttpClient){}

  ngOnInit(){
    this.get_users();
  }

  get_users(){
    this.http.get(this.APIURL + "get_users").subscribe((res)=>{
      this.users = res;
    })
  }

  add_user(){
    let body = new FormData();
    body.append("user", this.newuser);
    this.http.post(this.APIURL + "add_user", body).subscribe((res)=>{
      alert(res);
      this.newuser = "";
      this.get_users();
    })
  }

  delete_user(id:any){
    let body = new FormData();
    body.append("id", id);
    this.http.post(this.APIURL + "delete_user", body).subscribe((res)=>{
      alert(res);
      this.get_users();
    })
  }
}
