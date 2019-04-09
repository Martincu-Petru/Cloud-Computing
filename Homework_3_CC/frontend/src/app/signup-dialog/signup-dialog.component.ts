import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

import { PostUserService } from '../post-user.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-signup-dialog',
  templateUrl: './signup-dialog.component.html',
  styleUrls: ['./signup-dialog.component.css']
})
export class SignupDialogComponent implements OnInit {

  email = new FormControl('', [Validators.required, Validators.email]);
  password = new FormControl('', [Validators.required, Validators.pattern(('^[a-zA-Z0-9]{8,}$'))]);
  firstName = new FormControl('', [Validators.required, Validators.pattern('^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$')]);
  lastName = new FormControl('', [Validators.required, Validators.pattern('^[a-zA-Z]+(([\',. -][a-zA-Z ])?[a-zA-Z]*)*$')]);
  options: FormGroup;

  constructor(fb: FormBuilder, private postUserService: PostUserService, private cookieManager: CookieService) {
    this.options = fb.group({
      hideRequired: false,
      gender: 'male',
    });
  }

  ngOnInit() { }

  getEmailErrorMessage() {
    return this.email.hasError('required') ? 'You must enter a value' :
      this.email.hasError('email') ? 'Not a valid email' :
        '';
  }

  getPasswordErrorMessage() {
    return this.email.hasError('required') ? 'You must enter a value' :
      this.email.hasError('email') ? 'Not a valid password' :
        '';
  }

  getFirstNameErrorMessage() {
    return this.firstName.hasError('required') ? 'You must enter a value' :
      this.firstName.hasError('email') ? 'Not a valid name' :
        '';
  }

  getLastNameErrorMessage() {
    return this.lastName.hasError('required') ? 'You must enter a value' :
      this.lastName.hasError('email') ? 'Not a valid name' :
        '';
  }

  signup() {
    this.postUserService.insert_user_database(
      this.firstName.value,
      this.lastName.value,
      this.email.value,
      this.password.value,
      this.options.controls.gender.value);
    // this.cookieManager.set("SID", )
  }

}
