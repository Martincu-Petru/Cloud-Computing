import { Injectable } from '@angular/core';
import {HttpClient, HttpResponse} from '@angular/common/http';
import { Restaurants } from './models/Restaurants';
import {Restaurant} from './models/restaurant';
import {Review} from './models/Review';
import {Observable} from 'rxjs';
import {User} from './models/user';
import {environment} from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GetRestaurantsService {

  constructor(private http: HttpClient) { }

  get_restaurants(): Observable<HttpResponse<Restaurants>> {
    return this.http.get<Restaurants>(environment.getRestaurantsURL, { observe: 'response' });
  }
}

    /*let restaurants = new Restaurants();

    let restaurant_1 = new Restaurant();
    restaurant_1.imagine = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=550&photoreference=CmRaAAAAUhl5MpzlF-9tmdjl7PnQ-iWF1oAKPSeol8m55jBpi-9urz62_swl2V7_zz7102X140SpR_dROKxnIqCKvK1ptzHgCw3sx6ujJtYnnS_I3jbZ48htktoA5TW6LEGGxMoCEhBmRVqeRSwKjfgcqITDc1xpGhQEBkY7TTlnEraI1RG61dAtXwyqRw&key=AIzaSyAmkRUgG1it-NuoQAUmBf1DbX1LhvkRUKU';
    restaurant_1.titlu = 'Club RS';
    let reviews_1 = new Review();
    reviews_1.text = "And super ok!";
    let reviews_2 = new Review();
    reviews_2.text = "the best";
    restaurant_1.reviews = [];
    restaurant_1.reviews.push(reviews_1);
    restaurant_1.reviews.push(reviews_2);

    restaurants.restaurants = [];
    restaurants.restaurants.push(restaurant_1);

    let restaurant_2 = new Restaurant();
    restaurant_2.imagine = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=550&photoreference=CmRaAAAA9RZLpCGTOrfpfWqyNk71cdi8hduq6o9sA5xflfSq9II_ePV2rlzcgCgO-8J_NztiX37B2HKVxHPEw4exuY3wpR1_CX6yRzlxtmMhIuZ4oibEE2VkaQVtOrlDYFfKwl9eEhBKYUKPlQEOsnNXr6roES6uGhTVGo9dm9qBN9SvIsM02g_Z7DMn-w&key=AIzaSyAmkRUgG1it-NuoQAUmBf1DbX1LhvkRUKU';
    restaurant_2.titlu = 'Clubul Bursei';
    let reviews2_1 = new Review();
    reviews2_1.text = "Good food and good service. Cheap prices";
    let reviews2_2 = new Review();
    reviews2_2.text = "Good food, good service. Usually it is not crowded so it's fine for families with small kids (like us)";
    restaurant_2.reviews = [];
    restaurant_2.reviews.push(reviews2_2);
    restaurant_2.reviews.push(reviews2_1);

    restaurants.restaurants.push(restaurant_2);

    let restaurant_3 = new Restaurant();
    restaurant_3.imagine = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=550&photoreference=CmRaAAAACAmtWDhRRpse69VpY7iIxNjmAcyj2tvZZ-6coIjm-ipo5wDY1O37XIPNCsDJEXBTPKOpBRlf4-2WSUlN_TYoHL_5BgQoLuIh7MrlFZqfVgOUCE5i2T6haF9UPUdP7VHGEhCO3oGPMrjO6px7f9kJ-cZ_GhR9bCWWfDV7RdVRSqw92p9dF2egXg&key=AIzaSyAmkRUgG1it-NuoQAUmBf1DbX1LhvkRUKU';
    restaurant_3.titlu = 'Complex Hotelier Ciric';
    let reviews3_1 = new Review();
    reviews3_1.text = "Nice location prices are ok and food ok as well.";
    let reviews3_2 = new Review();
    reviews3_2.text = "Very scenic hotel with helpful staff";
    restaurant_3.reviews = [];
    restaurant_3.reviews.push(reviews3_2);
    restaurant_3.reviews.push(reviews3_1);

    restaurants.restaurants.push(restaurant_3);

    return restaurants;*/
