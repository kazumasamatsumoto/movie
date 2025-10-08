# #114 「深い階層の Component 通信」

## 概要
親子孫と階層が深くなる場合のコンポーネント通信戦略を整理し、プロパティドリリングを避ける手法を学びます。

## 学習目標
- 入れ子が深い場合の課題を理解する
- Input/Outputのチェーンとサービス共有の比較を知る
- AngularのDI機構を活用した祖先→子孫通信を習得する

## 技術ポイント
- **プロパティドリリング**: 中間コンポーネントが必要ないデータを受け渡す問題
- **共有サービス**: `@Injectable({ providedIn: 'root' })`で全層に同じ状態を提供
- **Component-level provider**: `providers`配列でスコープを限定して共有する

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Injectable({ providedIn: 'root' })
export class SharedState { value = signal(0); }
```

```typescript
constructor(private readonly state: SharedState) {}
```

```html
<app-grand-child></app-grand-child>
```

## 💻 詳細実装例（学習用）
```typescript
// shared-state.service.ts
import { Injectable, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class SharedStateService {
  readonly counter = signal(0);

  increment(): void {
    this.counter.update((c) => c + 1);
  }
}
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { ChildComponent } from './child.component';
import { SharedStateService } from './shared-state.service';

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent],
  templateUrl: './parent.component.html',
})
export class ParentComponent {
  constructor(public readonly state: SharedStateService) {}
}
```

```html
<!-- parent.component.html -->
<section>
  <h3>親</h3>
  <p>値: {{ state.counter() }}</p>
  <button type="button" (click)="state.increment()">親から +1</button>
</section>
<app-child></app-child>
```

```typescript
// child.component.ts
import { Component } from '@angular/core';
import { GrandChildComponent } from './grand-child.component';
import { SharedStateService } from './shared-state.service';

@Component({
  selector: 'app-child',
  standalone: true,
  imports: [GrandChildComponent],
  templateUrl: './child.component.html',
})
export class ChildComponent {
  constructor(public readonly state: SharedStateService) {}
}
```

```html
<!-- child.component.html -->
<section>
  <h4>子</h4>
  <p>値: {{ state.counter() }}</p>
</section>
<app-grand-child></app-grand-child>
```

```typescript
// grand-child.component.ts
import { Component } from '@angular/core';
import { SharedStateService } from './shared-state.service';

@Component({
  selector: 'app-grand-child',
  standalone: true,
  template: `
    <section>
      <h5>孫</h5>
      <p>値: {{ state.counter() }}</p>
      <button type="button" (click)="state.increment()">孫から +1</button>
    </section>
  `,
})
export class GrandChildComponent {
  constructor(public readonly state: SharedStateService) {}
}
```

## ベストプラクティス
- 共有状態は専用サービスに封じ、コンポーネントはinjectして利用する
- スコープを限定したい場合は親コンポーネントの`providers`でサービスを提供する
- Signalsをサービスで使うと、ライフサイクルを意識せずに最新値を取得できる

## 注意点
- グローバルサービスは状態がアプリ全体で共有されるため、コンポーネントごとの隔離が必要ならプロバイダ階層を分ける
- プロパティドリリングを避けたいがために過剰なサービス化をするのは避け、シンプルなケースではInputチェーンも許容する
- `providedIn: 'root'`のサービスをテストする際はテストベッドでリセットし、状態が引き継がれないようにする

## 関連技術
- Dependency Injectionとプロバイダ階層
- Signals Storeパターン
- Angular RouterでのResolver/Injector活用
