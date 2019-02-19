import { Component, OnInit } from '@angular/core';
import { Sample } from '../sample';
import { SampleService } from '../sample.service';


@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css']
})
export class SamplesComponent implements OnInit {

  samples: Sample[];

  constructor(private sampleService: SampleService) { }

  ngOnInit() {
    this.getSamples();
  }

  getSamples(): void {
    this.sampleService.getSamples()
        .subscribe(samples => this.samples = samples);
  }

  add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.sampleService.addSample({ name } as Sample)
      .subscribe(sample => {
        this.samples.push(sample);
      });
  }

  delete(sample: Sample): void {
    this.samples = this.samples.filter(s => s !== sample);
    this.sampleService.deleteSample(sample).subscribe();
  }

  

}
