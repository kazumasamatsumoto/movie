# #214 「再利用可能な Component 設計」

## 概要
Angular v20のコンテンツ投影を活用した再利用可能なコンポーネント設計のベストプラクティスを学習します。

## 学習目標
- 再利用可能なコンポーネント設計原則を理解する
- コンテンツ投影による構造とコンテンツの分離を習得する
- 実践的な再利用可能コンポーネントを実現できるようになる

## 技術ポイント
- 再利用可能設計
- 構造とコンテンツの分離
- DRY原則

## 📺 画面表示用コード

```html
<!-- 汎用的なボタンコンポーネント -->
<app-button [variant]="'primary'" [size]="'large'">
  <i class="icon">🚀</i>
  実行
</app-button>

<app-button [variant]="'secondary'" [size]="'small'">
  キャンセル
</app-button>
```

```html
<!-- 子コンポーネント（app-button） -->
<button 
  class="btn" 
  [class]="'btn-' + variant + ' btn-' + size"
  [disabled]="disabled">
  <ng-content></ng-content>
</button>
```

```html
<!-- 汎用的なカードコンポーネント -->
<app-card [elevation]="'high'">
  <div class="card-header">
    <h3>タイトル</h3>
    <span class="badge">新着</span>
  </div>
  <div class="card-body">
    <p>コンテンツ</p>
  </div>
</app-card>
```

## 実践的な活用例

```html
<!-- 汎用的なフォームフィールド -->
<app-form-field [label]="'メールアドレス'" [required]="true">
  <input type="email" placeholder="メールアドレスを入力">
  <div class="error-message">エラーメッセージ</div>
</app-form-field>
```

```html
<!-- 汎用的なリストコンポーネント -->
<app-list [items]="userList" [itemTemplate]="userItemTemplate">
  <ng-template #userItemTemplate let-user>
    <div class="user-item">
      <img [src]="user.avatar" [alt]="user.name">
      <span>{{user.name}}</span>
    </div>
  </ng-template>
</app-list>
```

## ベストプラクティス
- 単一責任の原則に従う
- プロパティでコンポーネントの動作を制御する
- 適切なデフォルト値を提供する
- コンテンツ投影で柔軟性を確保する

## 注意点
- プロパティの複雑さ
- コンテンツ投影の制限
- パフォーマンスへの影響

## 関連技術
- Component Architecture
- Design Patterns
- SOLID Principles
