export class Order {
  public client: string;
  public expTime: number;
  public company: string;
  public items: OrderItem[];
}

export class OrderItem {
  public unity: string;
  public quantity: number;
  public description: string;
}
