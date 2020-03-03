import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Order } from '../models/order';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  constructor(private http: HttpClient) {
  }

  list(): Observable<Order[]> {
    return this.http.get<Order[]>(
      this.getUrl() + '/v1/order',
      {
        headers: { 'x-api-key': this.getAuthorization() }
      }
    );
  }

  private getUrl() {
    return 'https://sswlks9rkb.execute-api.us-east-1.amazonaws.com/prod';
  }

  private getAuthorization() {
    return 'HT4AlajjMZ1AcYBjI9YGG7FBlf1vEn48aeU8h2pV';
  }
}
