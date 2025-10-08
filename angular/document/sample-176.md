# #176 「[ngClass] 動的クラス制御」

## 概要
`[ngClass]`ディレクティブでクラスを動的に切り替える基本的な使い方を学び、状態に応じたスタイル制御をテンプレートから簡単に行えるようにします。

## 学習目標
- `[ngClass]`の基本構文（文字列/配列/オブジェクト）を理解する
- 状態に基づくクラス切り替えを実装する
- クラス管理ロジックをコンポーネントにまとめるパターンを習得する

## 技術ポイント
- **文字列**: `[ngClass]="'btn btn-primary'"`
- **配列**: `[ngClass]="['btn', theme]"`（条件付きなら三項演算子を利用）
- **オブジェクト**: `[ngClass]="{ active: isActive }"`

## 📺 画面表示用コード（動画用）

```html
<div [ngClass]="{ active: isActive, disabled: isDisabled }"></div>
```

```html
<div [ngClass]="['btn', sizeClass]"></div>
```

```typescript
get classMap() { return { 'is-valid': valid, 'is-error': error }; }
```

## 💻 詳細実装例（学習用）
```typescript
// status-badge.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-status-badge',
  standalone: true,
  templateUrl: './status-badge.component.html',
  styleUrls: ['./status-badge.component.scss'],
})
export class StatusBadgeComponent {
  @Input() status: 'success' | 'warning' | 'error' = 'success';

  get classMap(): Record<string, boolean> {
    return {
      'badge--success': this.status === 'success',
      'badge--warning': this.status === 'warning',
      'badge--error': this.status === 'error',
    };
  }
}
```

```html
<!-- status-badge.component.html -->
<span class="badge" [ngClass]="classMap">
  <ng-content></ng-content>
</span>
```

```scss
/* status-badge.component.scss */
.badge {
  padding: 4px 12px;
  border-radius: 999px;
  color: #fff;
}
.badge--success {
  background: #43a047;
}
.badge--warning {
  background: #fb8c00;
}
.badge--error {
  background: #e53935;
}
```

## ベストプラクティス
- 複数条件を扱う際はコンポーネント側でクラスマップを返すgetterを実装し、テンプレートを簡潔に保つ
- ブール値を返すプロパティを利用し、複雑な条件式をテンプレートに書かない
- 命名規則を統一し、クラス名から状態が読み取れるようにする

## 注意点
- `[ngClass]`は`class`属性と併用しても上書きされないが、複雑な組み合わせでは構文の重複に注意
- パフォーマンス上の懸念がある場合は、クラスマップをMemoize（Signalやgetter）して再計算を抑える
- `[class.active]="condition"`のように単一クラスを直接バインドするシンタックスも併用可能

## 関連技術
- `[ngStyle]`によるスタイル制御
- CSS Modulesやユーティリティクラスとの組み合わせ
- Angular Animationsでクラス切り替えをトリガにする手法
