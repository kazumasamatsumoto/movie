# #184 「SCSS/SASS の使用」

## 概要
AngularプロジェクトでSCSS/SASSを採用し、変数・ミックスイン・ネストなどの機能でスタイル開発を効率化する方法を解説します。

## 学習目標
- Angular CLIでSCSSを有効化する手順を理解する
- SCSSの構文（変数、ネスト、ミックスイン）をコンポーネントスタイルに適用する
- 共通スタイルを`@use`/`@forward`でモジュール化する方法を習得する

## 技術ポイント
- **CLI設定**: `ng new --style=scss` または`angular.json`で`"style": "scss"`に変更
- **部分化**: `_variables.scss`, `_mixins.scss`を作成し`@use`で読み込む
- **コンポーネント単位**: `styleUrls`で`.scss`ファイルを参照

## 📺 画面表示用コード（動画用）

```bash
ng new my-app --style=scss
```

```scss
$color-primary: #7e57c2;
```

```scss
@use 'styles/variables' as vars;
```

## 💻 詳細実装例（学習用）
```scss
/* src/styles/_variables.scss */
$color-primary: #1976d2;
$spacing-lg: 24px;
```

```scss
/* src/styles/_mixins.scss */
@mixin card-shadow {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}
```

```scss
/* src/styles.scss */
@use 'styles/variables' as vars;
@use 'styles/mixins' as mixins;

:root {
  --color-primary: #{vars.$color-primary};
}
```

```scss
/* card.component.scss */
@use 'styles/variables' as vars;
@use 'styles/mixins' as mixins;

.card {
  padding: vars.$spacing-lg;
  @include mixins.card-shadow;
  background: #ffffff;
}
```

## ベストプラクティス
- 変数・ミックスインを`styles/`ディレクトリへ集約し、コンポーネントごとに`@use`して再利用する
- SCSS変数とCSSカスタムプロパティを併用し、ビルド時・ランタイムの双方でテーマを制御する
- `@use`/`@forward`を利用し、旧`@import`構文は使わない（Sass推奨事項）

## 注意点
- `stylePreprocessorOptions`で`"includePaths": ["src/styles"]`を設定すると`@use 'variables'`のような短いパスで読み込める
- SCSSの深いネストは可読性が低下するため、2～3階層までに抑える
- ビルド時間が若干増えるため、必要な部分だけSCSS機能を利用する

## 関連技術
- Tailwind CSS等のユーティリティファーストスタイル
- CSS Modulesとの比較
- Angular CLI Builderでのスタイルプリプロセッサ設定
