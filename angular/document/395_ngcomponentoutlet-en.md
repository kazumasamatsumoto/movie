# #395 "ngComponentOutlet - Dynamic Components"

## Overview
`ngComponentOutlet` is a directive that can dynamically specify and render component classes, suitable for plugin architectures and CMS construction.

## Learning Objectives
- Understand basic usage of `ngComponentOutlet`
- Learn how to replace Injector and dependencies
- Grasp performance considerations for dynamic components

## Technical Points
- Dynamically generate with `[ngComponentOutlet]="componentType"`
- Can specify dependencies with `ngComponentOutletInjector`, `ngComponentOutletContent`, `ngComponentOutletNgModuleFactory`
- When dynamically generating standalone components, no special NgModule needed

## 📺 Display Code (for video)
```html
<ng-container [ngComponentOutlet]="currentComponent"></ng-container>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-dynamic-host',
  standalone: true,
  imports: [CommonModule, AlertCardComponent, InfoCardComponent],
  template: `
    <button (click)="toggle()">Toggle</button>
    <ng-container [ngComponentOutlet]="component"></ng-container>
  `
})
export class DynamicHostComponent {
  protected component: Type<unknown> = AlertCardComponent;
  protected toggle(): void {
    this.component = this.component === AlertCardComponent ? InfoCardComponent : AlertCardComponent;
  }
}
```

## Best Practices
- Create a dictionary of component list and map from keys
- When replacing Injector, using `EnvironmentInjector` is flexible even in standalone configuration
- Optimize performance of dynamically generated components with `OnPush` and Signals

## Considerations
- Component classes need to be included in bundle, so devise separately for lazy-load or CDN distribution
- Frequent switching has high regeneration cost, so consider caching
- For security, don't specify components directly from user input

## Related Technologies
- Dynamic Component Loader
- EnvironmentInjector
- Router lazy loading
