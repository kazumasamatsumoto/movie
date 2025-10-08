# #198 「select 属性での選択」

## 概要
`ng-content`の`select`属性に属性セレクタを指定して、親が特定の属性を付与した要素のみを投影する方法を学びます。

## 学習目標
- 属性セレクタによるスロット選択の構文を理解する
- HTML構造を崩さずに役割を示す属性を定義する手法を習得する
- 属性ベースのAPI設計で可読性を高める方法を把握する

## 技術ポイント
- **属性セレクタ**: `<ng-content select="[modal-body]"></ng-content>`
- **役割指定**: カスタム属性で役割を明示し、親が使いやすいAPIを提供
- **複合条件**: `[modal-body].primary`のように属性とクラスを組み合わせ可能

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[modal-header]"></ng-content>
<ng-content select="[modal-body]"></ng-content>
<ng-content select="[modal-footer]"></ng-content>
```

```html
<app-modal>
  <h3 modal-header>ヘッダー</h3>
  <p modal-body>本文</p>
  <div modal-footer>フッター</div>
</app-modal>
```

```scss
[modal-header] { font-weight: bold; }
```

## 💻 詳細実装例（学習用）
```typescript
// modal.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-modal',
  standalone: true,
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.scss'],
})
export class ModalComponent {}
```

```html
<!-- modal.component.html -->
<div class="modal">
  <header class="modal__header">
    <ng-content select="[modal-header]"></ng-content>
  </header>
  <section class="modal__body">
    <ng-content select="[modal-body]"></ng-content>
  </section>
  <footer class="modal__footer">
    <ng-content select="[modal-footer]"></ng-content>
  </footer>
</div>
```

```html
<!-- parent.component.html -->
<app-modal>
  <h3 modal-header>属性選択の例</h3>
  <p modal-body>本文コンテンツをここに記述できます。</p>
  <button modal-footer>OK</button>
</app-modal>
```

## ベストプラクティス
- 属性名は`component-role`のようにコンポーネント名＋役割で命名すると衝突を避けられる
- 属性を付与するだけで役割が明確になるため、親側のマークアップが読みやすくなる
- ドキュメントで必須・任意の属性を明示し、利用者が迷わないAPI設計を行う

## 注意点
- 付与した属性にスタイルが必要な場合は、コンポーネント側のCSSで適切に指定する
- 属性を付け忘れるとデフォルトスロットへ回るため、テストでカバーするか警告を表示する
- 属性セレクタは大小文字区別に注意（HTMLでは小文字推奨）

## 関連技術
- `select`でのクラス名/タグ名/ディレクティブ指定
- `ContentChild`で特定属性を持つ要素の存在チェック
- `@Directive`で役割付与用ディレクティブを作成するパターン

