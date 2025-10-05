# #199 「select ディレクティブでの選択」

## 概要
Angular v20のselect属性でカスタムディレクティブを使用してコンテンツ投影を制御する方法を学習します。

## 学習目標
- ディレクティブセレクターの使用方法を理解する
- カスタムディレクティブによる投影制御を習得する
- 高度なコンテンツ投影パターンを実現できるようになる

## 技術ポイント
- ディレクティブセレクター
- カスタムディレクティブ投影
- 動的投影制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-content>
  <div appHighlight>ハイライトされるコンテンツ</div>
  <div appRequired>必須フィールド</div>
  <div appOptional>オプションコンテンツ</div>
</app-content>
```

```html
<!-- 子コンポーネント（app-content） -->
<div class="content-container">
  <div class="highlight-section">
    <ng-content select="[appHighlight]"></ng-content>
  </div>
  <div class="required-section">
    <ng-content select="[appRequired]"></ng-content>
  </div>
  <div class="optional-section">
    <ng-content select="[appOptional]"></ng-content>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-form>
  <input appRequiredField name="email">
  <input appOptionalField name="phone">
  <textarea appTextArea name="message"></textarea>
</app-form>
```

## 実践的な活用例

```html
<!-- 動的フォーム -->
<app-dynamic-form>
  <input appTextField name="title">
  <select appSelectField name="category">
    <option>カテゴリ1</option>
  </select>
  <input appCheckboxField name="agree">
</app-dynamic-form>
```

## ベストプラクティス
- ディレクティブ名は機能を明確に表現する
- ディレクティブの責任範囲を明確にする
- 投影されるディレクティブ構造をドキュメント化する

## 注意点
- ディレクティブの依存関係
- ディレクティブの実行順序
- パフォーマンスへの影響

## 関連技術
- Custom Directives
- Directive Composition
- Dynamic Components
