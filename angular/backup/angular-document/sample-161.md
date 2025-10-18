# #161 「Component スタイルの基本」

## 概要
Angularコンポーネントで独自のスタイルを定義する基本手法を整理し、`styleUrls`や`styles`プロパティを使ったカプセル化されたスタイル管理を理解します。

## 学習目標
- コンポーネント固有スタイルの定義方法（`styleUrls`/`styles`）を理解する
- デフォルトのViewEncapsulationによるスコープ化を把握する
- グローバルスタイルとの住み分け方を学ぶ

## 技術ポイント
- **styleUrls**: 外部CSS/SCSSファイルを配列で指定
- **styles**: コンポーネント内にインラインでCSSを記述
- **ViewEncapsulation.Emulated**: コンポーネントごとに属性が付与されスタイルをカプセル化

```typescript
@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
```

```html
<article class="card">
  <h3>タイトル</h3>
  <p>説明文</p>
</article>
```

```scss
.card {
  padding: 16px;
  border-radius: 8px;
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
export class CardComponent {
  title = 'Angular Component Styling';
  description = 'コンポーネント固有のスタイルを簡単に管理できます。';
}
```

```html
<!-- card.component.html -->
<article class="card">
  <h3>{{ title }}</h3>
  <p>{{ description }}</p>
</article>
```

```scss
/* card.component.scss */
.card {
  padding: 16px;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

## ベストプラクティス
- コンポーネント固有のスタイルは`styleUrls`に分離し、ファイル名で責務が分かるようにする
- カプセル化を前提に、グローバルスタイルにはリセット・テーマ・ユーティリティなど共通要素だけ置く
- コンポーネントのクラス名はBEMやFSDなど一貫した命名規則に沿って管理する

## 注意点
- 同名クラスでも異なるコンポーネント間で干渉しないが、ViewEncapsulation.Noneを設定するとグローバルへ波及する
- SCSSを使う場合はビルド設定（angular.jsonの`"stylePreprocessorOptions"`）を整える
- グローバルスタイルが増えすぎると依存関係が複雑化するため定期的に棚卸しする

## 関連技術
- ViewEncapsulationの各戦略
- グローバルスタイル (`src/styles.scss`)
- Angular CLIの`ng generate component`オプション（style絡み）
