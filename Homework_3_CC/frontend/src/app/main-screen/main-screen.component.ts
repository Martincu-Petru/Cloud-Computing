import { Component, OnInit } from '@angular/core';
import {CookieService} from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-main-screen',
  templateUrl: './main-screen.component.html',
  styleUrls: ['./main-screen.component.css']
})
export class MainScreenComponent implements OnInit {

  constructor(private cookie_service: CookieService, private router: Router) { }

  first_name = 'John';
  last_name = 'Smith';

  ngOnInit() {
    if (this.cookie_service.check('session') === false) {
      this.router.navigateByUrl('/');
    }

    document.body.style.backgroundImage = 'url(https://images.pexels.com/photos/6267/menu-restaurant-vintage-table.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940' +
      'city_view_from_above_skyscrapers_122900_3840x2160.jpg)';
    document.body.style.backgroundSize = 'cover';
  }

  logout() {
    this.cookie_service.delete('session');
    this.router.navigateByUrl('/');
  }

}
