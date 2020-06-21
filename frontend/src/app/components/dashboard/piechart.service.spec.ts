import { TestBed } from '@angular/core/testing';

import { PiechartService } from './piechart.service';

describe('PiechartService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PiechartService = TestBed.get(PiechartService);
    expect(service).toBeTruthy();
  });
});
