import { Component, OnInit } from '@angular/core';
 
import { Observable, Subject } from 'rxjs';
 
import {
   debounceTime, distinctUntilChanged, switchMap
 } from 'rxjs/operators';
 
import { Sample } from '../sample';
import { SampleService } from '../sample.service';
 
@Component({
  selector: 'app-sample-search',
  templateUrl: './sample-search.component.html',
  styleUrls: [ './sample-search.component.css' ]
})
export class SampleSearchComponent implements OnInit {
  samples$: Observable<Sample[]>;
  private searchTerms = new Subject<string>();
 
  constructor(private sampleService: SampleService) {}
 
  // Push a search term into the observable stream.
  search(term: string): void {
    this.searchTerms.next(term);
  }
 
  ngOnInit(): void {
    this.samples$ = this.searchTerms.pipe(
      // wait 300ms after each keystroke before considering the term
      debounceTime(300),
 
      // ignore new term if same as previous term
      distinctUntilChanged(),
 
      // switch to new search observable each time the term changes
      switchMap((term: string) => this.sampleService.searchSamples(term)),
    );
  }
}
