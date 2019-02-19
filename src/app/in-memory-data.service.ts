import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Sample } from './sample';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const samples = [
      { id: 11, name: 'DNA001' },
      { id: 12, name: 'JE_RNA02' },
      { id: 13, name: 'BirdFlu' },
      { id: 14, name: 'Ribosomes' },
      { id: 15, name: 'Mitochondria' },
      { id: 16, name: 'BadVirus' },
      { id: 17, name: 'GoodVirus' },
      { id: 18, name: 'MediumVirus' },
      { id: 19, name: 'Tardigrades' },
      { id: 20, name: 'flubber' }
    ];
    return {samples};
  }

  // Overrides the genId method to ensure that a hero always has an id.
  // If the heroes array is empty,
  // the method below returns the initial number (11).
  // if the heroes array is not empty, the method below returns the highest
  // hero id + 1.
  genId(samples: Sample[]): number {
    return samples.length > 0 ? Math.max(...samples.map(sample => sample.id)) + 1 : 11;
  }
}
