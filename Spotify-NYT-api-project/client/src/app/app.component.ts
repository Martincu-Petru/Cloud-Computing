import { Component } from '@angular/core';
import { GetRandomTrackService } from './get-random-track.service'
import { Track } from '../Track'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {

  track: Track;

  ngOnInit() {
    this.getTracks();
  }

  constructor(private trackService: GetRandomTrackService) {}

  getTracks(): void {
    this.trackService.getTrack().subscribe(
      newTrack => this.track = newTrack
    )
  }  
}
