# #188 「CSS Grid レイアウト」

## 概要
CSS Gridを活用して複雑な2次元レイアウトを構築する方法を紹介し、Angularコンポーネントでも利用しやすい書き方を整理します。

## 学習目標
- CSS Gridの基本プロパティ（`grid-template-columns`, `grid-template-areas`など）を理解する
- レスポンシブ対応に`auto-fit`や`minmax`を活用するテクニックを習得する
- AngularコンポーネントでGridレイアウトを適用する際のベストプラクティスを把握する

## 技術ポイント
- **基本構成**: `display: grid; grid-template-columns: repeat(3, 1fr);`
- **エリア指定**: `grid-template-areas`で可視的にレイアウト構造を記述
- **レスポンシブ**: `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));`

## 📺 画面表示用コード（動画用）

```scss
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
```

```scss
@media (max-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

```scss
.grid--auto {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

## 💻 詳細実装例（学習用）
```typescript
// gallery.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-gallery',
  standalone: true,
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.scss'],
})
export class GalleryComponent {
  items = Array.from({ length: 8 }, (_, i) => `Item ${i + 1}`);
}
```

```html
<!-- gallery.component.html -->
<section class="gallery">
  <div class="gallery__item" @for (item of items; track item)>{{ item }}</div>
</section>
```

```scss
/* gallery.component.scss */
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}

.gallery__item {
  background: #e1f5fe;
  padding: 16px;
  border-radius: 8px;
  text-align: center;
}

@media (max-width: 480px) {
  .gallery {
    grid-template-columns: 1fr;
  }
}
```

## ベストプラクティス
- Gridレイアウトは2次元配置に最適。コンポーネントレイアウトをエリア単位で設計する
- `repeat(auto-fit, minmax(...))`を利用するとカードギャラリーなど可変レイアウトが簡単に実装できる
- `gap`で余白を統一し、ネストしたGridは責務ごとにコンポーネントを分割する

## 注意点
- 古いブラウザではGridが利用できないため、サポート対象を確認する（IE11は未対応）
- `grid-template-areas`を使う際は命名に注意し、デザイン変更にも耐えられる構造にする
- Gridのネストが増えると可読性が下がるため、適切に責務を分割する

## 関連技術
- Flexboxとの使い分け
- Tailwind CSSのGridユーティリティ
- Angular CDK Layout
