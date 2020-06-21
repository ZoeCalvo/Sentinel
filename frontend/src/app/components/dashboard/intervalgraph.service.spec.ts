import { TestBed } from '@angular/core/testing';

import { IntervalgraphService } from './intervalgraph.service';

describe('IntervalgraphService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: IntervalgraphService = TestBed.get(IntervalgraphService);
    expect(service).toBeTruthy();
  });
});
