# #127 「プロパティドリリングの回避」

## 概要
深い階層に同じ@Input()を渡し続ける「プロパティドリリング」を避ける方法を学び、コードの可読性と保守性を向上させます。

## 学習目標
- プロパティドリリングの問題点を理解する
- 共有サービス、InjectionToken、Standalone Injectorを活用した代替策を習得する
- 依存範囲を最小化する設計手法を学ぶ

## 技術ポイント
- **共有サービス**: 状態をDIで共有し、中間コンポーネントを介さない
- **provideIn Component**: 祖先コンポーネントでスコープを限定して提供
- **View Context API**: Angular v17以降の`@let`などでcontextを共有（将来性）

```typescript
@Component({
  providers: [{ provide: PANEL_TOKEN, useValue: panelStore }],
})
```

```typescript
const panel = inject(PANEL_TOKEN);
```

```typescript
signalStore.update(...);
```

## 💻 詳細実装例（学習用）
```typescript
// panel-store.ts
import { Injectable, signal } from '@angular/core';

@Injectable()
export class PanelStore {
  readonly title = signal('初期タイトル');
  setTitle(value: string): void {
    this.title.set(value);
  }
}
```

```typescript
// panel-token.ts
import { InjectionToken } from '@angular/core';
import { PanelStore } from './panel-store';

export const PANEL_STORE = new InjectionToken<PanelStore>('PanelStore');
```

```typescript
// ancestor.component.ts
import { Component } from '@angular/core';
import { PANEL_STORE } from './panel-token';
import { PanelStore } from './panel-store';
import { ChildComponent } from './child.component';

@Component({
  selector: 'app-ancestor',
  standalone: true,
  imports: [ChildComponent],
  templateUrl: './ancestor.component.html',
  providers: [
    {
      provide: PANEL_STORE,
      useClass: PanelStore,
    },
  ],
})
export class AncestorComponent {
  panel = inject(PANEL_STORE);
}
```

```html
<!-- ancestor.component.html -->
<section>
  <h2>祖先: {{ panel.title() }}</h2>
  <button type="button" (click)="panel.setTitle('祖先から更新')">更新</button>
</section>
<app-child></app-child>
```

```typescript
// grand-child.component.ts
import { Component, inject } from '@angular/core';
import { PANEL_STORE } from './panel-token';

@Component({
  selector: 'app-grand-child',
  standalone: true,
  template: `
    <section>
      <h4>孫: {{ panel.title() }}</h4>
      <button type="button" (click)="panel.setTitle('孫から更新')">孫更新</button>
    </section>
  `,
})
export class GrandChildComponent {
  panel = inject(PANEL_STORE);
}
```

## ベストプラクティス
- 子孫全体で共有したいデータは、祖先コンポーネントでサービスを提供してDIで利用する
- 状態をSignalで管理すると、どの階層から更新しても即座に反映される
- ドリリングを避ける設計をドキュメント化し、新規コンポーネントでも同じパターンを適用する

## 注意点
- 共有サービスのスコープを正しく設定しないとアプリ全体で共有されてしまう
- 依存関係が増えすぎると設計が複雑になるため、明確な責務分割を保つ
- 未来のView Context APIなど、新しい機能が導入された際に再評価する

## 関連技術
- Angular Dependency Injection
- Signals Store
- Angular v17 View Context API (preview)
