import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Track } from 'src/Track';

@Injectable({
  providedIn: 'root'
})
export class GetRandomTrackService {

  constructor(private http: HttpClient) { }

  getTrack(): Observable<Track> {
    return this.http.get<Track>("http://localhost:8080")
  }
}
