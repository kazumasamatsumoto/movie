# #206 「コンテンツ投影とライフサイクル」

## 概要
Angular v20でコンテンツ投影とコンポーネントライフサイクルの関係について学習します。

## 学習目標
- コンテンツ投影のライフサイクルを理解する
- 投影タイミングとコンポーネント初期化の関係を習得する
- 適切なライフサイクル管理を実現できるようになる

## 技術ポイント
- コンテンツ投影ライフサイクル
- コンポーネント初期化順序
- ライフサイクル管理

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-lifecycle-demo>
  <div class="projected-content">
    <h3>投影されたコンテンツ</h3>
    <p>ライフサイクルテスト</p>
  </div>
</app-lifecycle-demo>
```

```html
<!-- 子コンポーネント（app-lifecycle-demo） -->
<div class="lifecycle-container">
  <ng-content></ng-content>
</div>
```

```typescript
// 子コンポーネントクラス
export class LifecycleDemoComponent implements OnInit, AfterContentInit {
  ngOnInit() {
    console.log('子コンポーネント OnInit');
  }
  
  ngAfterContentInit() {
    console.log('投影コンテンツ初期化完了');
  }
}
```

## 実践的な活用例

```html
<!-- データ依存の投影 -->
<app-data-dependent [data]="apiData">
  <div class="data-display">
    <h2>{{data.title}}</h2>
    <p>{{data.description}}</p>
  </div>
</app-data-dependent>
```

## ベストプラクティス
- 投影コンテンツの初期化を適切なタイミングで行う
- データ依存の投影は慎重に設計する
- ライフサイクルフックを適切に使用する

## 注意点
- 投影されるコンテンツの初期化タイミング
- データバインディングの実行順序
- メモリリークの防止

## 関連技術
- Component Lifecycle
- Lifecycle Hooks
- Content Projection Timing
