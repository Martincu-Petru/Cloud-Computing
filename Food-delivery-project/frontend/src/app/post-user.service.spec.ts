import { TestBed } from '@angular/core/testing';

import { PostUserService } from './post-user.service';

describe('PostUserService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PostUserService = TestBed.get(PostUserService);
    expect(service).toBeTruthy();
  });
});
