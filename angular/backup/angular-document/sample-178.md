# #178 「[ngClass] 配列構文」

## 概要
`[ngClass]`で配列構文を使い、クラス名を順序付けて動的に付与する方法を紹介します。三項演算子などと組み合わせ、シンプルに条件を表現できます。

## 学習目標
- `[ngClass]="['btn', theme, condition ? 'active' : '']"`形式の使い方を理解する
- 配列構文とオブジェクト構文の使い分けを把握する
- コンポーネント側でクラスの配列を生成してテンプレートを整理する方法を学ぶ

## 技術ポイント
- **基本構文**: `[ngClass]="['base', size, isDisabled ? 'disabled' : '']"`
- **null/空文字**: falsy値は自動的に無視される
- **クラスの順番**: 配列の順に付与されるため優先度が明確

```html
<button [ngClass]="['btn', themeClass]"></button>
```

```html
<div [ngClass]="['alert', alertType === 'error' && 'alert--error']"></div>
```

```typescript
get classes(): (string | false)[] {
  return ['chip', sizeClass, selected && 'chip--selected'];
}
```

## 💻 詳細実装例（学習用）
```typescript
// chip.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-chip',
  standalone: true,
  templateUrl: './chip.component.html',
  styleUrls: ['./chip.component.scss'],
})
export class ChipComponent {
  @Input() size: 'sm' | 'md' | 'lg' = 'md';
  @Input() selected = false;

  get classList(): (string | false)[] {
    return [
      'chip',
      `chip--${this.size}`,
      this.selected && 'chip--selected',
    ];
  }
}
```

```html
<!-- chip.component.html -->
<span [ngClass]="classList">
  <ng-content></ng-content>
</span>
```

```scss
/* chip.component.scss */
.chip {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 4px 12px;
  border: 1px solid #90a4ae;
}
.chip--sm {
  font-size: 12px;
}
.chip--md {
  font-size: 14px;
}
.chip--lg {
  font-size: 16px;
}
.chip--selected {
  background: #1976d2;
  color: #fff;
  border-color: #1976d2;
}
```

## ベストプラクティス
- クラス名が少なく順序を保ちたいときは配列構文が読みやすい
- falsy値（`false`, `null`, `''`）を使って条件付きクラスをシンプルに制御する
- 再利用するクラス配列はコンポーネントのgetterに切り出し、テンプレートを見通しよくする

## 注意点
- 配列内で複雑な条件を直接書くと読みにくくなるため、変数や関数に抽出する
- クラス名の重複に注意し、同じクラスを2度追加しないようにする
- `[ngClass]` は `class` 属性と併用可能だが、重複を避けるため責務を分ける

## 関連技術
- `[ngClass]` オブジェクト構文
- `[class.className]` 単体バインディング
- Tailwindなどユーティリティ型CSSとの組み合わせ
