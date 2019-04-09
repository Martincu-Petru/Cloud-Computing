import { TestBed } from '@angular/core/testing';

import { GetRestaurantsService } from './get-restaurants.service';

describe('GetRestaurantsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GetRestaurantsService = TestBed.get(GetRestaurantsService);
    expect(service).toBeTruthy();
  });
});
