import { TestBed } from '@angular/core/testing';

import { PostSessionService } from './post-session.service';

describe('PostSessionService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PostSessionService = TestBed.get(PostSessionService);
    expect(service).toBeTruthy();
  });
});
