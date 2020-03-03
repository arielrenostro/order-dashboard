import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ListOrdersComponent } from './pages/list-orders/list-orders.component';
import { RouterModule, Routes } from '@angular/router';
import { DashboardOrdersComponent } from './pages/dashboard-orders/dashboard-orders.component';
import { MatButtonModule, MatFormFieldModule, MatIconModule, MatTableModule, MatToolbarModule } from '@angular/material';
import { HttpClientModule } from '@angular/common/http';
import { OrderService } from './service/order.service';

const appRoutes: Routes = [
  { path: '', component: ListOrdersComponent },
  { path: 'dashboard', component: DashboardOrdersComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    ListOrdersComponent,
    DashboardOrdersComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(appRoutes, { enableTracing: true }),
    MatTableModule,
    HttpClientModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatFormFieldModule
  ],
  providers: [
    OrderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
