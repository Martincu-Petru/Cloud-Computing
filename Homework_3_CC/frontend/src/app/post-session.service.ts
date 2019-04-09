import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { environment } from '../environments/environment';
import {CookieService} from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class PostSessionService {

  constructor(private http: HttpClient, private cookieManager: CookieService) { }

  insert_session_database(user_id: string) {

    console.log('SESSION POST ', user_id);

    const body = JSON.stringify({
      user_id: user_id,
      expiry_date: new Date(Date.now()).getFullYear().toString()
        + '-' + new Date(Date.now()).getMonth().toString()
        + '-' + new Date(Date.now()).getDay().toString()
        + ' ' + (new Date(Date.now()).getHours()).toString()
        + ':' + new Date(Date.now()).getMinutes().toString()
        + ':' + new Date(Date.now()).getSeconds().toString()
    });

    const options = { headers: new HttpHeaders({ 'Content-Type': 'application/json' })};

    this.http.post(environment.postSessionURL, { body }, options).subscribe(
    data => {
      console.log('POST session is successful ', data);
      var session: any = data;
      this.cookieManager.set("session", session.session_id, 0.25);
    });
  }

}
