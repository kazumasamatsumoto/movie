# #170 「グローバルスタイルとの使い分け」

## 概要
コンポーネント固有スタイルとグローバルスタイルを使い分け、チーム開発でも衝突しないスタイル設計を行うためのポイントを整理します。

## 学習目標
- グローバル`styles.scss`とコンポーネントCSSの役割を理解する
- ユーティリティクラスやリセットCSSの配置方針を把握する
- プロジェクト規模に応じたスタイル構成を設計できるようになる

## 技術ポイント
- **グローバル**: リセット、テーマ、ユーティリティ、フォントなど全体共有要素を配置
- **コンポーネント**: ビュー固有スタイル、状態管理、ローカルユーティリティ
- **構成管理**: `styles.scss`->`styles/_utilities.scss`など分割し、`@use`で読み込む

## 📺 画面表示用コード（動画用）

```scss
/* styles.scss */
@use 'styles/reset';
@use 'styles/theme';
```

```scss
/* app.component.scss */
:host {
  font-family: var(--font-base);
}
```

```typescript
styleUrls: ['./feature.component.scss']
```

## 💻 詳細実装例（学習用）
```scss
/* src/styles.scss */
@use 'styles/reset';
@use 'styles/typography';
@use 'styles/utilities';

:root {
  --color-primary: #1976d2;
  --color-surface: #fafafa;
}
```

```scss
/* src/styles/_utilities.scss */
.u-text-center {
  text-align: center;
}

.u-mb-16 {
  margin-bottom: 16px;
}
```

```typescript
// feature.component.ts
@Component({
  selector: 'app-feature',
  standalone: true,
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss'],
})
export class FeatureComponent {}
```

```html
<!-- feature.component.html -->
<section class="feature">
  <h2 class="feature__title u-text-center">Feature</h2>
  <p class="feature__description">コンポーネント固有スタイルとグローバルユーティリティを併用します。</p>
</section>
```

## ベストプラクティス
- グローバルスタイルは`styles/`ディレクトリなどに分割し、責務ごとに管理する
- コンポーネントでグローバルユーティリティを使う場合はプレフィックス（`u-`など）で役割を明確化
- TailwindやCSS-in-JSを併用する場合はガイドラインを整備し、重複ルールを避ける

## 注意点
- グローバルCSSが増えすぎると依存関係が複雑になるため、定期的にレビューする
- ViewEncapsulation.Noneのコンポーネントはグローバルに影響するため管理対象に加える
- テーマ切り替えなど全体に関わる変更はグローバルに置き、コンポーネント側では最小限の上書きに留める

## 関連技術
- CSS変数によるテーマ共有
- SCSS `@use`, `@forward`
- デザイントークン管理（Style Dictionary 等）
