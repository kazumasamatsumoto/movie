# #179 「[ngClass] 条件付きクラス」

## 概要
条件に基づいてクラスを付与/除去する代表的なパターンを紹介し、読みやすく保守しやすい`[ngClass]`の記述方法を学びます。

## 学習目標
- 複数条件を組み合わせたクラス制御の書き方を理解する
- コンポーネント側で条件を計算し、テンプレートを簡潔に保つ方法を習得する
- クラス命名規則と条件表現を整理して可読性を高める

## 技術ポイント
- **複数条件**: `[ngClass]="{ 'is-valid': valid, 'is-warning': score < 60 }"`
- **getter利用**: `get classMap()` で条件を集約
- **シングルクラス**: `[class.is-hidden]="hidden"` のシンタックスも併用

```html
<div [ngClass]="{ 'badge--success': score >= 80, 'badge--warning': score < 50 }">
  {{ score }}
></div>
```

```typescript
get stateClasses() {
  return {
    'form__field--error': this.invalid,
    'form__field--disabled': this.disabled,
  };
}
```

```html
<input class="form__field" [ngClass]="stateClasses" />
```

## 💻 詳細実装例（学習用）
```typescript
// rating.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-rating',
  standalone: true,
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.scss'],
})
export class RatingComponent {
  @Input() score = 0;

  get classMap(): Record<string, boolean> {
    return {
      'rating--excellent': this.score >= 80,
      'rating--warning': this.score < 50,
    };
  }
}
```

```html
<!-- rating.component.html -->
<span class="rating" [ngClass]="classMap">
  {{ score }} 点
></span>
```

```scss
/* rating.component.scss */
.rating {
  font-weight: 600;
  color: #424242;
}
.rating--excellent {
  color: #43a047;
}
.rating--warning {
  color: #e53935;
}
```

## ベストプラクティス
- 条件式はコンポーネント側に移し、テンプレートを最小限のバインディングにする
- クラス命名を状態ベース（例：`--error`, `--disabled`）に統一して意図を伝える
- 状態が増える場合はEnumやマップを使って管理する

## 注意点
- テンプレート内で複雑な条件式を書くとメンテナンス性が下がる。関数やgetterで隠蔽する
- `[ngClass]`を多用するとChange Detectionごとに再評価されるため、不要な再計算に注意する
- Tailwind等のユーティリティを使う場合は条件分岐を慎重に行い、クラスの重複を避ける

## 関連技術
- `[class.foo]="condition"`シンタックス
- `[ngStyle]`でのスタイル条件分岐
- Angularフォームのバリデーション状態をUIへ反映するパターン
