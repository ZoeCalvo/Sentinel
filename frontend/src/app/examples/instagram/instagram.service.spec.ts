import { TestBed } from '@angular/core/testing';

import { InstagramService } from './instagram.service';

describe('InstagramService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: InstagramService = TestBed.get(InstagramService);
    expect(service).toBeTruthy();
  });
});
