// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  getUserURL: 'https://server-cloud-computing.appspot.com/user?',
  postUserURL: 'https://server-cloud-computing.appspot.com/user',
  getSessionURL: 'https://server-cloud-computing.appspot.com/session?',
  postSessionURL: 'https://server-cloud-computing.appspot.com/session',
  getRestaurantsURL: 'https://googltranslateapi-236420.appspot.com/',
  getScoreURL: 'https://server-cloud-computing.appspot.com/analize-text'
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
