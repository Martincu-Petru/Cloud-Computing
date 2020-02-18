import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AnalizeTextService {

  get_text_score(text: string) {
    const body = JSON.stringify({
      text: text
    });

    const options = { headers: new HttpHeaders({ 'Content-Type': 'application/json' })};

    return this.http.post(environment.getScoreURL, { body }, options);
  }

  constructor(private http: HttpClient) { }
}
