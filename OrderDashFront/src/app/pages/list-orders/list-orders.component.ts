import { Component, OnInit } from '@angular/core';
import { Order } from '../../models/order';
import { OrderService } from '../../service/order.service';

@Component({
  selector: 'app-list-orders',
  templateUrl: './list-orders.component.html',
  styleUrls: ['./list-orders.component.css']
})
export class ListOrdersComponent implements OnInit {

  displayedColumns: string[] = [ 'client', 'expTime', 'items' ];
  ordersDataSource: Order[];

  constructor(private service: OrderService) {
  }

  ngOnInit() {
    this.updateData();
  }

  updateData() {
    this.service.list().subscribe(
      response => {
        this.ordersDataSource = response;
      },
      error => {
        console.error(error);
      }
    );
  }

  getDate(expTime) {
    return new Date(expTime);
  }
}
