# #357 "Displaying Multidimensional Arrays"

## Overview
Multidimensional arrays can be displayed with nested `*ngFor`, utilized when expressing matrix or grid structures.

## Learning Objectives
- Learn template expansion of multidimensional arrays
- Understand combining row and column loops
- Grasp trackBy implementation with composite keys

## Technical Points
- Outer loop handles rows, inner loop handles columns
- Return keys combining `rowIndex` and `colIndex` with trackBy
- Introducing cell components advances separation of responsibilities

## 📺 Screen Display Code (For Video)
```html
<tr *ngFor="let row of matrix; let rowIndex = index">
  <td *ngFor="let cell of row">{{ cell }}</td>
</tr>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-matrix-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <table>
      <tr *ngFor="let row of matrix; let r = index">
        <td *ngFor="let cell of row; let c = index; trackBy: trackCell(r)">
          {{ cell }}
        </td>
      </tr>
    </table>
  `
})
export class MatrixDemoComponent {
  protected matrix = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3']
  ];

  protected trackCell(rowIndex: number) {
    return (_: number, __: string, colIndex: number) => `${rowIndex}-${colIndex}`;
  }
}
```

## Best Practices
- Make row and column indices explicit for clarity in templates
- Extract to `<app-cell>` etc. when cell rendering is complex
- Manage matrix as immutable structure to reduce change detection cost

## Cautions
- Without trackBy, large numbers of cells may be re-rendered
- Deep nesting reduces readability, so consider comments or component decomposition
- Introduce virtualization or paging when matrix size is large

## Related Technologies
- trackBy
- Angular CDK Table
- Component Composition
