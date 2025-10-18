# #166 「:host セレクタ - ホスト要素」

## 概要
コンポーネントのホスト要素にスタイルを適用する`:host`擬似クラスの使い方を学び、コンテナ要素のレイアウトや状態を制御します。

## 学習目標
- `:host`セレクタの基本的な書式を理解する
- 条件付きでホスト要素へクラスを適用する手順を習得する
- `:host`と通常のクラス指定の違いを把握する

## 技術ポイント
- **基本**: `:host { display: block; }`
- **条件付き**: `:host(.active) { border-color: #29b6f6; }`
- **属性利用**: `@HostBinding('class.active')`と併用して状態を切り替える

```scss
:host {
  display: block;
  padding: 16px;
}
```

```scss
:host(.error) {
  border: 1px solid #ef5350;
}
```

```typescript
@HostBinding('class.error') hasError = false;
```

## 💻 詳細実装例（学習用）
```typescript
// alert.component.ts
import { Component, HostBinding, Input } from '@angular/core';

@Component({
  selector: 'app-alert',
  standalone: true,
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.scss'],
})
export class AlertComponent {
  @Input() type: 'info' | 'error' = 'info';

  @HostBinding('class.error')
  get errorClass(): boolean {
    return this.type === 'error';
  }
}
```

```html
<!-- alert.component.html -->
<ng-content></ng-content>
```

```scss
/* alert.component.scss */
:host {
  display: block;
  border-left: 4px solid #42a5f5;
  background: #e3f2fd;
  padding: 12px;
}

:host(.error) {
  border-left-color: #ef5350;
  background: #ffebee;
}
```

## ベストプラクティス
- コンポーネント全体のレイアウト（display、marginなど）は`:host`で定義し、子要素用のクラスと分離する
- 状態による見た目変更は`@HostBinding`やInputを組み合わせて制御する
- `:host`内で`@media`を使えばブレークポイントに応じたレイアウト変更が容易

## 注意点
- `:host`はコンポーネント自身にのみ適用され、子要素には作用しない
- `ViewEncapsulation.None`の場合は:hostが一般的なタグセレクタに変換されるため、他コンポーネントへ影響する可能性がある
- `:host-context`と混同しないよう、役割（祖先条件 vs 自身）を区別する

## 関連技術
- `:host-context` 擬似クラス
- `@HostBinding`, `@HostListener`
- ViewEncapsulation戦略
