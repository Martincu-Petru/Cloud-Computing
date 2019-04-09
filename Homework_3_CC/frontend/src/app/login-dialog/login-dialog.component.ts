import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { GetUserService } from '../get-user.service';
import { CookieService } from 'ngx-cookie-service';
import {PostSessionService} from '../post-session.service';
import {Router} from '@angular/router';
import {__await} from 'tslib';
import {promise} from 'selenium-webdriver';
import delayed = promise.delayed;
import {delay} from 'rxjs/operators';

@Component({
  selector: 'app-login-dialog',
  templateUrl: './login-dialog.component.html',
  styleUrls: ['./login-dialog.component.css']
})
export class LoginDialogComponent implements OnInit {

  email = new FormControl('', [Validators.required, Validators.email]);
  password = new FormControl('', [Validators.required, Validators.pattern(('^[a-zA-Z0-9]{8,}$'))]);

  constructor(private getUserService: GetUserService, private post_session: PostSessionService, private router_service: Router, private cookie_service: CookieService) { }

  ngOnInit() {
  }

  getEmailErrorMessage() {
    return this.email.hasError('required') ? 'You must enter a value' :
      this.email.hasError('email') ? 'Not a valid email' :
        '';
  }

  getPasswordErrorMessage() {
    return this.email.hasError('required') ? 'You must enter a value' :
      this.password.hasError('password') ? 'Not a valid password' :
        '';
  }

  login() {
    this.getUserService.get_user(this.email.value, this.password.value).subscribe(
      response => {
        console.log('GET user is successful ', response.body);
        this.post_session.insert_session_database(response.body.user_id);
        this.router_service.navigateByUrl('/home');
      }
    );
  }
}
