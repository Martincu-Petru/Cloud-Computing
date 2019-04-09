import { Component, OnInit } from '@angular/core';
import {GetRestaurantsService} from '../get-restaurants.service';
import {AnalizeTextService} from '../analize-text.service';

@Component({
  selector: 'app-restaurant-card',
  templateUrl: './restaurant-card.component.html',
  styleUrls: ['./restaurant-card.component.css']
})
export class RestaurantCardComponent implements OnInit {

  current_restaurant = 0;
  total_number_of_restaurants = null;
  restaurants = null;
  current_restaurant_image = 'http://www.festival56.com/images/loading.gif';
  current_restaurant_title = null;
  current_restaurant_opinion = "Loading opinion...";

  constructor(private restaurants_service: GetRestaurantsService, private analize_text_service: AnalizeTextService) { }

  ngOnInit() {
    this.restaurants = this.restaurants_service.get_restaurants().subscribe(response => {
      this.analize_text_service.get_text_score(response.body.restaurants[this.current_restaurant].reviews[0].text).subscribe(
        response2 => {
          let score_response: any = response2;
          switch (score_response.score) {
            case -1:
              this.current_restaurant_opinion = "Users think this restaurant is bad."
              break;
            case 0:
              this.current_restaurant_opinion = "Users think this restaurant is like the others."
              break;
            case 1:
              this.current_restaurant_opinion = "Users think this restaurant is very nice and they enjoyed their time spent there."
              break;
          }
          console.log("OPINIE: ");
          console.log(this.current_restaurant_opinion);
          this.restaurants = response.body;
          this.total_number_of_restaurants = this.restaurants.restaurants.length;
          this.current_restaurant_image = this.restaurants.restaurants[this.current_restaurant].imagine;
          this.current_restaurant_title = this.restaurants.restaurants[this.current_restaurant].titlu;
        }
      );
    });
  }

  decrease_current_number() {
    this.current_restaurant--;
    this.current_restaurant_image = this.restaurants.restaurants[this.current_restaurant].imagine;
    this.current_restaurant_title = this.restaurants.restaurants[this.current_restaurant].titlu;
    this.current_restaurant_opinion = "Loading opinion...";
    this.analize_text_service.get_text_score(this.restaurants.restaurants[this.current_restaurant].reviews[0].text).subscribe(
      response => {
        let score_response: any = response;
        switch (score_response.score) {
          case -1:
            this.current_restaurant_opinion = "Users think this restaurant is bad."
            break;
          case 0:
            this.current_restaurant_opinion = "Users think this restaurant is like the others."
            break;
          case 1:
            this.current_restaurant_opinion = "Users think this restaurant is very nice and they enjoyed their time spent there."
            break;
        }
      }
    );
  }

  increase_current_number() {
    this.current_restaurant++;
    this.current_restaurant_image = this.restaurants.restaurants[this.current_restaurant].imagine;
    this.current_restaurant_title = this.restaurants.restaurants[this.current_restaurant].titlu;
    this.current_restaurant_opinion = "Loading opinion...";
    this.analize_text_service.get_text_score(this.restaurants.restaurants[this.current_restaurant].reviews[0].text).subscribe(
      response => {
        let score_response: any = response;
        switch (score_response.score) {
          case -1:
            this.current_restaurant_opinion = "Users think this restaurant is bad."
            break;
          case 0:
            this.current_restaurant_opinion = "Users think this restaurant is like the others."
            break;
          case 1:
            this.current_restaurant_opinion = "Users think this restaurant is very nice and they enjoyed their time spent there."
            break;
        }
      }
    );
  }
}
