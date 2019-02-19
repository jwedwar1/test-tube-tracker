import { Component, OnInit } from '@angular/core';
import { Sample } from '../sample';
import { SampleService } from '../sample.service';
 
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: [ './dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {
  samples: Sample[] = [];
 
  constructor(private sampleService: SampleService) { }
 
  ngOnInit() {
    this.getSamples();
  }
 
  getSamples(): void {
    this.sampleService.getSamples()
      .subscribe(samples => this.samples = samples.slice(1, 5));
  }
}
