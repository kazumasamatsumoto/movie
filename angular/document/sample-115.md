# #115 「祖先-子孫間の通信戦略」

## 概要
直系の親子以外、祖先コンポーネントと深い子孫コンポーネント間でデータを共有する戦略を整理します。AngularのDIとInjectionTokenを活用する方法を学びます。

## 学習目標
- 祖先→子孫への依存注入パターンを理解する
- InjectionTokenを使ってインターフェースを共有する手法を習得する
- サービスを使わないコントラクトベースの通信を知る

## 技術ポイント
- **InjectionToken**: `export const PANEL_CONTEXT = new InjectionToken<Context>('...');`
- **provide**: 祖先側で`providers: [{ provide: PANEL_CONTEXT, useValue: ... }]`
- **inject**: 子孫コンポーネントで`inject(PANEL_CONTEXT)`

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
export const PANEL_CONTEXT = new InjectionToken<PanelContext>('PanelContext');
```

```typescript
providers: [{ provide: PANEL_CONTEXT, useValue: { title: 'Dashboard' } }]
```

```typescript
const ctx = inject(PANEL_CONTEXT);
```

## 💻 詳細実装例（学習用）
```typescript
// panel-context.ts
import { InjectionToken } from '@angular/core';

export type PanelContext = {
  title: string;
  setTitle(title: string): void;
};

export const PANEL_CONTEXT = new InjectionToken<PanelContext>('PanelContext');
```

```typescript
// ancestor.component.ts
import { Component, signal } from '@angular/core';
import { PANEL_CONTEXT, PanelContext } from './panel-context';
import { ChildComponent } from './child.component';

@Component({
  selector: 'app-ancestor',
  standalone: true,
  imports: [ChildComponent],
  templateUrl: './ancestor.component.html',
  providers: [
    {
      provide: PANEL_CONTEXT,
      useFactory: () => {
        const title = signal('初期タイトル');
        const context: PanelContext = {
          get title() {
            return title();
          },
          setTitle(value: string) {
            title.set(value);
          },
        } as PanelContext;
        Object.defineProperty(context, 'title', {
          get: () => title(),
        });
        return context;
      },
    },
  ],
})
export class AncestorComponent {
  constructor(public readonly panel: PanelContext) {}
}
```

```html
<!-- ancestor.component.html -->
<section>
  <h2>祖先: {{ panel.title }}</h2>
  <button type="button" (click)="panel.setTitle('祖先から更新')">
    祖先から更新
  </button>
</section>
<app-child></app-child>
```

```typescript
// child.component.ts
import { Component } from '@angular/core';
import { GrandChildComponent } from './grand-child.component';
import { PANEL_CONTEXT } from './panel-context';
import { inject } from '@angular/core';

@Component({
  selector: 'app-child',
  standalone: true,
  imports: [GrandChildComponent],
  template: `
    <section>
      <h3>子</h3>
      <p>ctx.title: {{ panel.title }}</p>
    </section>
    <app-grand-child></app-grand-child>
  `,
})
export class ChildComponent {
  panel = inject(PANEL_CONTEXT);
}
```

```typescript
// grand-child.component.ts
import { Component, inject } from '@angular/core';
import { PANEL_CONTEXT } from './panel-context';

@Component({
  selector: 'app-grand-child',
  standalone: true,
  template: `
    <section>
      <h4>孫</h4>
      <p>ctx.title: {{ panel.title }}</p>
      <button type="button" (click)="panel.setTitle('孫から更新')">
        孫から更新
      </button>
    </section>
  `,
})
export class GrandChildComponent {
  panel = inject(PANEL_CONTEXT);
}
```

## ベストプラクティス
- 共有したいインターフェースをInjectionTokenで公開し、祖先が具体実装を提供する
- `inject` APIを使う際は必ずプロバイダがあることを確認し、fallbackが必要なら`inject(token, { optional: true })`
- Signalsやサービスを組み合わせると状態の同期が容易になる

## 注意点
- 提供スコープを限定しないと意図せず複数インスタンスが生成される可能性がある
- InjectionTokenでクラスを隠蔽するとテストでモックが作りづらいのでFactoryなどを用意する
- 多段階で大量の依存を注入すると設計が複雑になるため、適切なレイヤに分割する

## 関連技術
- Angular DI (provide / inject)
- `viewProviders` と `providers` の違い
- Signals + InjectionTokenでのcontext共有 (View Context API)
