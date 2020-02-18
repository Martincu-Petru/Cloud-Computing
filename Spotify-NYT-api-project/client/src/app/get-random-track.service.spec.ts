import { TestBed } from '@angular/core/testing';

import { GetRandomTrackService } from './get-random-track.service';

describe('GetRandomTrackService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GetRandomTrackService = TestBed.get(GetRandomTrackService);
    expect(service).toBeTruthy();
  });
});
