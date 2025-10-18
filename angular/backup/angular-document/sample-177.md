# #177 「[ngClass] オブジェクト構文」

## 概要
`[ngClass]`のオブジェクト構文で複数の条件付きクラスを読みやすく管理する方法を紹介します。

## 学習目標
- `[ngClass]="{ クラス名: 真偽値 }"`形式の構文を理解する
- コンポーネント側でクラスマップを返す実装を習得する
- 可読性を高めるための分割・補助メソッドを学ぶ

## 技術ポイント
- **基本構文**: `[ngClass]="{ 'is-valid': valid, 'is-disabled': disabled }"`
- **複雑な条件の分離**: クラスマップをgetterで計算
- **再利用**: 共通クラスをコンポーネント内にまとめて管理

```html
<div [ngClass]="{ 'form-field--invalid': invalid, 'form-field--disabled': disabled }"></div>
```

```typescript
get classMap() {
  return {
    'btn--primary': type === 'primary',
    'btn--secondary': type === 'secondary',
  };
}
```

```html
<button [ngClass]="classMap">ボタン</button>
```

## 💻 詳細実装例（学習用）
```typescript
// toggle-button.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-toggle-button',
  standalone: true,
  templateUrl: './toggle-button.component.html',
  styleUrls: ['./toggle-button.component.scss'],
})
export class ToggleButtonComponent {
  @Input() active = false;
  @Input() disabled = false;

  get classMap(): Record<string, boolean> {
    return {
      'toggle-button--active': this.active,
      'toggle-button--disabled': this.disabled,
    };
  }
}
```

```html
<!-- toggle-button.component.html -->
<button class="toggle-button" [ngClass]="classMap">
  <ng-content></ng-content>
</button>
```

```scss
/* toggle-button.component.scss */
.toggle-button {
  padding: 8px 14px;
  border-radius: 999px;
  border: 1px solid transparent;
}
.toggle-button--active {
  background: #1976d2;
  color: #fff;
}
.toggle-button--disabled {
  opacity: 0.4;
  pointer-events: none;
}
```

## ベストプラクティス
- 条件が増えたらクラスマップをコンポーネントのメソッドやgetterで分離し、テンプレートを簡潔に保つ
- クラス名は状態を表す形（`--active`, `--disabled`）にして命名規則を統一する
- `Object.assign`やスプレッド構文でクラスマップを合成し、再利用性を高める

## 注意点
- `[ngClass]`にオブジェクトを渡すと、Angularが毎回再評価するため、大量の要素に適用する場合はパフォーマンスへの影響を確認する
- 同じクラス名に複数の条件が重なると、true/falseの切り替えが混乱するので注意する
- ブーリアンプロパティを利用することで条件式を短く保つ

## 関連技術
- `[class.some-class]="condition"`による単一クラス制御
- `[ngClass]`配列構文
- Tailwindなどユーティリティクラスとの併用
