import { TestBed } from '@angular/core/testing';

import { GetSessionService } from './get-session.service';

describe('GetSessionService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: GetSessionService = TestBed.get(GetSessionService);
    expect(service).toBeTruthy();
  });
});
