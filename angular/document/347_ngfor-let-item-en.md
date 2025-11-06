# #347 "*ngFor=\"let item of items\""

## Overview
`*ngFor="let item of items"` extracts elements from a collection in sequence and uses them as the template variable `item`.

## Learning Objectives
- Understand the meaning and scope of the `let` keyword
- Learn naming and usage of template variables
- Create practical display examples

## Technical Points
- `item` is assigned a new reference for each loop
- Can declare multiple variables with `let` (like `; let i = index`)
- Unlike `as` syntax, `item` always exists

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let product of products">
  {{ product.name }}
</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Product {
  id: number;
  name: string;
  price: number;
}

@Component({
  selector: 'app-ngfor-item-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <table>
      <tr *ngFor="let product of products">
        <td>{{ product.name }}</td>
        <td>{{ product.price | currency:'JPY' }}</td>
      </tr>
    </table>
  `
})
export class NgForItemDemoComponent {
  protected products: Product[] = [
    { id: 1, name: 'Angular Guide', price: 2800 },
    { id: 2, name: 'Directive Patterns', price: 3200 }
  ];
}
```

## Best Practices
- Use descriptive variable names showing content rather than generic `item`
- Use pipes for formatting things like prices concisely within templates
- Return keys with trackBy to suppress re-rendering

## Cautions
- Directly assigning to `item` won't rewrite the original collection (as it's a reference)
- When handling mutable data, optimize performance by combining with `OnPush`
- Writing Observables directly as `items` leaves them unresolved, so use `AsyncPipe`

## Related Technologies
- CurrencyPipe
- trackBy
- ChangeDetectionStrategy.OnPush
