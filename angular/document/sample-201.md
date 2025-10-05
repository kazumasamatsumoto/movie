# #201 「条件付きコンテンツ投影」

## 概要
Angular v20の@ifディレクティブとng-contentを組み合わせて、条件によってコンテンツ投影を制御する方法を学習します。

## 学習目標
- 条件付きコンテンツ投影の実装方法を理解する
- @ifディレクティブとng-contentの組み合わせを習得する
- 動的なコンテンツ投影制御を実現できるようになる

## 技術ポイント
- 条件付き投影
- @ifディレクティブ
- 動的コンテンツ制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-conditional-card [showContent]="true">
  <h3>条件付きコンテンツ</h3>
  <p>このコンテンツは条件によって表示されます</p>
</app-conditional-card>
```

```html
<!-- 子コンポーネント（app-conditional-card） -->
<div class="card">
  @if (showContent) {
    <div class="card-body">
      <ng-content></ng-content>
    </div>
  } @else {
    <div class="card-body">
      <p>コンテンツは非表示です</p>
    </div>
  }
</div>
```

```html
<!-- 使用例 -->
<app-dashboard [showStats]="isAdmin">
  <div class="admin-stats">管理者統計</div>
</app-dashboard>
```

## 実践的な活用例

```html
<!-- ロールベースコンテンツ -->
<app-user-panel [userRole]="currentUser.role">
  <div class="admin-panel">管理者パネル</div>
  <div class="user-panel">ユーザーパネル</div>
</app-user-panel>
```

## ベストプラクティス
- 条件は明確で理解しやすいものにする
- デフォルトの表示状態を考慮する
- パフォーマンスへの影響を最小限にする

## 注意点
- 条件の変更頻度を考慮する
- 投影されるコンテンツの初期化タイミング
- 条件がfalseの場合のメモリ使用量

## 関連技術
- Control Flow (@if)
- Conditional Rendering
- Dynamic Components
