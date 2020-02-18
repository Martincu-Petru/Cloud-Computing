import { TestBed } from '@angular/core/testing';

import { AnalizeTextService } from './analize-text.service';

describe('AnalizeTextService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: AnalizeTextService = TestBed.get(AnalizeTextService);
    expect(service).toBeTruthy();
  });
});
