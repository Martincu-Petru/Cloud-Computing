import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-screen',
  templateUrl: './login-screen.component.html',
  styleUrls: ['./login-screen.component.css']
})

export class LoginScreenComponent implements OnInit {

  showLoginDialog = false;
  showSignupDialog = false;

  constructor(private cookie_service: CookieService, private router: Router) {
  }

  ngOnInit() {
    if (this.cookie_service.check("session"))  {
      this.router.navigateByUrl('/home');
    }
    document.body.style.backgroundImage = 'url(https://images.wallpaperscraft.com/image/' +
      'city_view_from_above_skyscrapers_122900_3840x2160.jpg)';
    document.body.style.backgroundSize = 'cover';
  }

  toggleShowLoginDialog() {
    this.showLoginDialog = false;
    this.showSignupDialog = true;
  }

  toggleShowSignupDialog() {
    this.showLoginDialog = true;
    this.showSignupDialog = false;
  }

}
