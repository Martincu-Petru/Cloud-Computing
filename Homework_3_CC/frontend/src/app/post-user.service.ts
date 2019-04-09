import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { environment } from '../environments/environment';
import {PostSessionService} from './post-session.service';
import {Router} from '@angular/router';
import {Session} from './models/session';

@Injectable({
  providedIn: 'root'
})

export class PostUserService {

  constructor(private http: HttpClient, private post_session: PostSessionService, private router_service: Router) { }

  insert_user_database(first_name: string, last_name: string, email: string, password: string, gender: string) {

    const body = JSON.stringify({
      first_name: first_name,
      last_name: last_name,
      password: password,
      email: email,
      gender: gender
    });

    const options = { headers: new HttpHeaders({ 'Content-Type': 'application/json' })};

    this.http.post(environment.postUserURL, { body }, options).subscribe(
      data => {
        console.log('POST user is successful ', data);
        var session: any = data;
        this.post_session.insert_session_database(session.user_id);
        console.log(data.valueOf());
        this.router_service.navigateByUrl('/home');
      }
    );
  }
}
