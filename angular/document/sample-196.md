# #196 「select タグ名での選択」

## 概要
`ng-content`の`select`属性にタグ名を指定して、親が提供する特定のHTMLタグをスロットへ振り分ける方法を学びます。

## 学習目標
- タグ名セレクタを使ったスロットの構成方法を理解する
- セマンティックHTMLを活かした投影パターンを実装する
- タグ名指定で複数スロットを構成する際の注意点を把握する

## 技術ポイント
- **タグ名セレクタ**: `<ng-content select="header"></ng-content>`
- **構造保持**: HTMLタグの意味を保ちつつ投影できる
- **複数タグ**: 複数タグを扱う場合はセレクタを分けて宣言する

## 📺 画面表示用コード（動画用）

```html
<ng-content select="header"></ng-content>
<ng-content select="main"></ng-content>
<ng-content select="footer"></ng-content>
```

```html
<app-layout>
  <header>ヘッダー</header>
  <main>本文</main>
  <footer>フッター</footer>
</app-layout>
```

```scss
header { font-weight: bold; }
```

## 💻 詳細実装例（学習用）
```typescript
// layout.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-layout',
  standalone: true,
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss'],
})
export class LayoutComponent {}
```

```html
<!-- layout.component.html -->
<div class="layout">
  <header class="layout__header">
    <ng-content select="header"></ng-content>
  </header>
  <main class="layout__main">
    <ng-content select="main"></ng-content>
  </main>
  <footer class="layout__footer">
    <ng-content select="footer"></ng-content>
  </footer>
</div>
```

```html
<!-- parent.component.html -->
<app-layout>
  <header>タグヘッダー</header>
  <main>タグ本文</main>
  <footer>タグフッター</footer>
</app-layout>
```

## ベストプラクティス
- セマンティックなHTMLタグ（`header`, `main`, `footer`など）を用いて構造を明確にする
- タグ名セレクタはクラスや属性より直感的だが、複合レイアウトではクラス/属性と併用する
- フォールバックとして`select`なしの`ng-content`を最後に置き、マッチしないコンテンツを受ける

## 注意点
- 同じタグ名を複数個投影したい場合、すべて同じスロットに入るため個別制御できない
- タグ名セレクタはHTML仕様に依存するため、親側がカスタムタグを使うとマッチしない
- セレクタの競合が起きた場合、`ng-content`の宣言順序でマッチングが決まる

## 関連技術
- select クラス名/属性/ディレクティブ（#197〜#199）
- レイアウトコンポーネント設計（#213）
- `ContentChild`でのTemplateRef取得

