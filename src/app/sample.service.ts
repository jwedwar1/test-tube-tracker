import { Injectable } from '@angular/core';
import { Sample } from './sample';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class SampleService {

  /** GET heroes from the server */
  getSamples (): Observable<Sample[]> {
    return this.http.get<Sample[]>(this.samplesUrl)
    .pipe(
      tap(_ => this.log('fetched samples')),
      catchError(this.handleError('getSamples', []))
    );
  }

  /** GET sample by id. Will 404 if id not found */
  getSample(id: number): Observable<Sample> {
    const url = `${this.samplesUrl}/${id}`;
    return this.http.get<Sample>(url).pipe(
    tap(_ => this.log(`fetched sample id=${id}`)),
    catchError(this.handleError<Sample>(`getSample id=${id}`))
  );
  }




  /** PUT: update the hero on the server */
  updateSample (sample: Sample): Observable<any> {
    return this.http.put(this.samplesUrl, sample, httpOptions).pipe(
    tap(_ => this.log(`updated hero id=${sample.id}`)),
    catchError(this.handleError<any>('updateHero'))
    );
  }

  /** POST: add a new sample to the server */
  addSample (sample: Sample): Observable<Sample> {
    return this.http.post<Sample>(this.samplesUrl, sample, httpOptions).pipe(
    tap((newSample: Sample) => this.log(`added sample w/ id=${newSample.id}`)),
    catchError(this.handleError<Sample>('addSample'))
    );
  }

  /** DELETE: delete the sample from the server */
  deleteSample (sample: Sample | number): Observable<Sample> {
    const id = typeof sample === 'number' ? sample : sample.id;
    const url = `${this.samplesUrl}/${id}`;

    return this.http.delete<Sample>(url, httpOptions).pipe(
    tap(_ => this.log(`deleted sample id=${id}`)),
    catchError(this.handleError<Sample>('deleteSample'))
    );
  }

  /* GET samples whose name contains search term */
  searchSamples(term: string): Observable<Sample[]> {
    if (!term.trim()) {
    // if not search term, return empty sample array.
    return of([]);
    }
    return this.http.get<Sample[]>(`${this.samplesUrl}/?name=${term}`).pipe(
    tap(_ => this.log(`found samples matching "${term}"`)),
    catchError(this.handleError<Sample[]>('searchSamples', []))
    );
  }





  constructor(private http: HttpClient, private messageService: MessageService) { }

  
  
  /**
 * Handle Http operation that failed.
 * Let the app continue.
 * @param operation - name of the operation that failed
 * @param result - optional value to return as the observable result
 */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
 
    // TODO: send the error to remote logging infrastructure
    console.error(error); // log to console instead
 
    // TODO: better job of transforming error for user consumption
    this.log(`${operation} failed: ${error.message}`);
 
    // Let the app keep running by returning an empty result.
    return of(result as T);
  };
}
  
  
  /** Log a HeroService message with the MessageService */
  private log(message: string) {
    this.messageService.add(`SampleService: ${message}`);
  }

  private samplesUrl = 'api/samples';  // URL to web api

}
