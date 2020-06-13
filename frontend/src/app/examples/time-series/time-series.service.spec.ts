import { TestBed } from '@angular/core/testing';

import { TimeSeriesService } from './time-series.service';

describe('TimeSeriesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TimeSeriesService = TestBed.get(TimeSeriesService);
    expect(service).toBeTruthy();
  });
});
