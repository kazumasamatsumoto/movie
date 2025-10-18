# #126 「Component 通信のデザインパターン」

## 概要
コンポーネント間通信の主要デザインパターン（Input/Output、サービス、状態管理など）を整理し、状況に応じた選択基準を示します。

## 学習目標
- 代表的な通信パターンを理解する
- 各パターンのメリット・デメリットを把握する
- プロジェクトの規模や要件に応じた適切な選択を行う

## 技術ポイント
- **Input/Output**: シンプルな親子通信に最適
- **共有サービス/Signals**: 兄弟・祖先子孫で状態を共有
- **状態管理ライブラリ**: 大規模なグローバル状態を管理
- **イベントバス**: 特殊ケース（推奨されにくい）

```html
<!-- Input/Output -->
<app-child [value]="value" (valueChange)="handle($event)"></app-child>
```

```typescript
// 共有サービス
@Injectable({ providedIn: 'root' }) class Store { state = signal(0); }
```

```typescript
// NgRx例
store.dispatch(updateValue({ value: 10 }));
```

## 💻 詳細実装例（学習用）
```markdown
| パターン            | 代表例                           | 利点                                   | 注意点                                  |
|--------------------|----------------------------------|----------------------------------------|------------------------------------------|
| Input/Output        | 親子で@Input() / @Output()      | シンプル、依存が明確                   | 深い階層ではドリリングが発生            |
| 共有サービス        | Injectable + Signal/Subject      | 兄弟/祖先子孫で状態を共有              | スコープ管理が必要                      |
| 状態管理ライブラリ | NgRx / NgXs / Akita              | 大規模アプリの一貫した状態管理         | 初期コストが高い、ボイラープレート増   |
| イベントバス        | Subject/EventEmitterを単独利用   | 広域イベントの配信                     | 構造が不透明になりやすく推奨されない   |
```

```typescript
// store.service.ts
import { Injectable, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class CounterStore {
  readonly count = signal(0);
  increment(): void {
    this.count.update((c) => c + 1);
  }
}
```

```typescript
// feature.component.ts
import { Component } from '@angular/core';
import { CounterStore } from './store.service';

@Component({
  selector: 'app-feature',
  standalone: true,
  template: `
    <p>{{ store.count() }}</p>
    <button (click)="store.increment()">+</button>
  `,
})
export class FeatureComponent {
  constructor(public readonly store: CounterStore) {}
}
```

## ベストプラクティス
- 要件に合わせて最小限のパターンを選択し、過剰な抽象化を避ける
- 小規模ではInput/Outputと共有サービスで十分、大規模では状態管理ライブラリを検討する
- 通信パターンをドキュメント化し、チームメンバーが共通認識を持つようにする

## 注意点
- 複数パターンを混在させる場合は責務境界を明確にし、参照が循環しないようにする
- イベントバスやグローバルSubjectは管理が難しくなるため、意図とスコープを明示する
- 状態管理ライブラリを導入する前に問題を明確にし、必要性を検討する

## 関連技術
- Smart/Dumbコンポーネントアーキテクチャ
- Angular Signals vs NgRx
- CQRSやMediatorなどのアーキテクチャパターン
