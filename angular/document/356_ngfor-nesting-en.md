# #356 "Nesting *ngFor"

## Overview
Nesting `*ngFor` allows displaying multidimensional data and parent-child relationships, but requires attention to readability and performance.

## Learning Objectives
- Understand how to write nested *ngFor
- Learn how to use outer context variables inside
- Grasp refactoring strategies according to nesting depth

## Technical Points
- Outer variables can be referenced in inner *ngFor
- Extract to child components when nesting is deep to separate responsibilities
- Implementing trackBy for each loop suppresses re-rendering

## 📺 Screen Display Code (For Video)
```html
<div *ngFor="let group of groups">
  <p>{{ group.title }}</p>
  <span *ngFor="let item of group.items">{{ item }}</span>
</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Group {
  id: number;
  title: string;
  items: string[];
}

@Component({
  selector: 'app-ngfor-nesting-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section *ngFor="let group of groups; trackBy: trackGroup">
      <h3>{{ group.title }}</h3>
      <ul>
        <li *ngFor="let item of group.items; trackBy: trackItem">{{ item }}</li>
      </ul>
    </section>
  `
})
export class NgForNestingDemoComponent {
  protected groups: Group[] = [
    { id: 1, title: 'Category A', items: ['A-1', 'A-2'] },
    { id: 2, title: 'Category B', items: ['B-1', 'B-2', 'B-3'] }
  ];

  protected trackGroup(_: number, group: Group): number {
    return group.id;
  }

  protected trackItem(index: number): number {
    return index;
  }
}
```

## Best Practices
- When nesting exceeds 2 levels, extract to child components to keep templates concise
- Decide track keys per hierarchy to suppress DOM regeneration
- Avoid heavy processing in nesting, format data in advance

## Cautions
- Ensure index variable names don't conflict
- Large amounts of nesting affect performance, consider virtual lists etc.
- Changing outer variables inside causes unexpected side effects

## Related Technologies
- Component Composition
- trackBy
- Angular CDK Tree
