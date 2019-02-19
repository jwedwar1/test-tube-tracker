import { Component, OnInit, Input } from '@angular/core';
import { Sample } from '../sample';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { SampleService }  from '../sample.service';

@Component({
  selector: 'app-sample-detail',
  templateUrl: './sample-detail.component.html',
  styleUrls: ['./sample-detail.component.css']
})
export class SampleDetailComponent implements OnInit {

  @Input() sample: Sample;

  constructor(private route: ActivatedRoute,
    private sampleService: SampleService,
    private location: Location) { }

    ngOnInit(): void {
      this.getSample();
    }
    
    getSample(): void {
      const id = +this.route.snapshot.paramMap.get('id');
      this.sampleService.getSample(id)
        .subscribe(sample => this.sample = sample);
    }

    goBack(): void {
      this.location.back();
    }

    save(): void {
      this.sampleService.updateSample(this.sample)
        .subscribe(() => this.goBack());
    }

}
