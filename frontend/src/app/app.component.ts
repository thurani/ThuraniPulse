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
  users:any = []
  skills:any = []
  hobbies:any = []

  APIURL = "http://localhost:8000/";

  constructor(private http:HttpClient){}

  selectedDiv: string = '';

  ngOnInit(){
    this.get_users();
    this.get_skills();
    this.get_hobbies();
  }

  showDiv(divId: string) {
    this.selectedDiv = divId;
  }

  get_users(){
    this.http.get(this.APIURL + "get_users/").subscribe((res)=>{
      this.users = res;
    })
  }
  get_skills(){
    this.http.get(this.APIURL + "get_skills/").subscribe((res)=>{
      this.skills = res;
    })
  }

  get_hobbies(){
    this.http.get(this.APIURL + "get_hobbies/").subscribe((res)=>{
      this.hobbies = res;
    })
  }
}
