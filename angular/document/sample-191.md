# #191 「ng-content - 基本的なコンテンツ投影」

## 概要
Angularコンポーネントで`ng-content`を用いて親から渡されたHTMLコンテンツを子コンポーネント内へ挿入する基本的なコンテンツ投影の仕組みを学びます。

## 学習目標
- `ng-content`の役割と構文を理解する
- 単一スロットで親のコンテンツを挿入する方法を習得する
- コンテンツ投影を利用したシンプルなラッパーコンポーネントを実装する

## 技術ポイント
- **タグ構文**: `<ng-content></ng-content>` をテンプレートに配置するだけで投影が行われる
- **単一スロット**: `select`属性を使用しない基本形。親の内容がそのまま挿入される
- **コンポーネント設計**: コンテンツ投影を使うことで汎用的なラッパーコンポーネントを作成できる

## 📺 画面表示用コード（動画用）

```typescript
@Component({
  selector: 'app-card',
  standalone: true,
  template: `<article class="card"><ng-content></ng-content></article>`,
})
```

```html
<app-card>
  <h3>タイトル</h3>
  <p>本文テキスト</p>
</app-card>
```

```scss
.card {
  padding: 16px;
  border-radius: 12px;
  background: #fff;
}
```

## 💻 詳細実装例（学習用）
```typescript
// card.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {}
```

```html
<!-- card.component.html -->
<article class="card">
  <ng-content></ng-content>
</article>
```

```scss
/* card.component.scss */
.card {
  display: block;
  padding: 16px;
  border-radius: 12px;
  background: #fafafa;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

```html
<!-- parent.component.html -->
<app-card>
  <h3>Angularコンテンツ投影</h3>
  <p>親コンポーネントから投影されたテキストです。</p>
</app-card>
```

## ベストプラクティス
- コンテンツの構造を親に委ねる場合は、コンテナ要素だけを用意して`ng-content`で受け取る
- ラッパーコンポーネントでは、コンテンツ投影に加えてヘッダーやサイドのInputを組み合わせると表現力が高まる
- ドキュメントに「どこへ何を投影できるか」を明記し、利用者が迷わないようにする

## 注意点
- 投影コンテンツは親のスコープで評価されるため、子コンポーネント内のプロパティは直接参照できない
- 条件付きでコンテンツを表示したい場合は`ng-template`や`ContentChild`を併用する
- 多数の`ng-content`をネストするとDOMが複雑になるため、適切に責務を分割する

## 関連技術
- Multi Slot Projection（#194）
- `ContentChild` / `ContentChildren` で投影内容を取得
- `ngTemplateOutlet`で動的にテンプレートを挿入


