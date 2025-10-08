# #181 「[ngStyle] オブジェクト構文」

## 概要
`[ngStyle]`へオブジェクトを渡して複数のスタイルを一度に適用する方法を解説し、条件に応じたスタイル更新を簡潔に表現します。

## 学習目標
- オブジェクト構文による複数プロパティの指定方法を理解する
- コンポーネント側でスタイルオブジェクトを生成する実装パターンを習得する
- 単位付きプロパティやCSS変数の設定を学ぶ

## 技術ポイント
- **構文**: `[ngStyle]="{ color: textColor, 'font-size.px': size }"`
- **スタイルマップ**: `get styleMap()`でまとめて返す
- **CSS変数**: `[ngStyle]="{ '--card-radius': radius + 'px' }"`

## 📺 画面表示用コード（動画用）

```html
<div [ngStyle]="{ background: bgColor, color: textColor }"></div>
```

```typescript
get styleMap() {
  return { 'font-size.px': fontSize, '--chip-gap': gap + 'px' };
}
```

```html
<div [ngStyle]="styleMap"></div>
```

## 💻 詳細実装例（学習用）
```typescript
// badge.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-badge',
  standalone: true,
  templateUrl: './badge.component.html',
  styleUrls: ['./badge.component.scss'],
})
export class BadgeComponent {
  @Input() color = '#1976d2';
  @Input() textColor = '#fff';
  @Input() size = 14;

  get styleMap(): Record<string, string> {
    return {
      background: this.color,
      color: this.textColor,
      'font-size.px': this.size,
    };
  }
}
```

```html
<!-- badge.component.html -->
<span class="badge" [ngStyle]="styleMap">
  <ng-content></ng-content>
></span>
```

```scss
/* badge.component.scss */
.badge {
  padding: 4px 10px;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
}
```

## ベストプラクティス
- スタイルオブジェクトをコンポーネント側で計算し、テンプレートは`[ngStyle]="styleMap"`の1行に抑える
- 同じスタイルを複数箇所で使う場合は関数化またはユーティリティを用意する
- CSS変数を活用すると、子コンポーネントやShadow DOMでも容易にスタイルを連携できる

## 注意点
- オブジェクトを直接テンプレートに書くと何度も再生成されるため、getterやメモ化を活用する
- 数値に単位が必要な場合は`.px`などをプロパティ名に付与する
- `[ngStyle]`で設定した値はインラインスタイルとして適用されるため、優先度が高い点を意識する

## 関連技術
- `[ngClass]`でのクラス切り替え
- Renderer2によるスタイル操作
- CSSカスタムプロパティとの連携
