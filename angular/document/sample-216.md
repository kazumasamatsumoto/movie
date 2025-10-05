# #216 「コンテンツ投影のデバッグ」

## 概要
Angular v20のコンテンツ投影におけるデバッグ手法とツールの使用方法を学習します。

## 学習目標
- コンテンツ投影のデバッグ手法を理解する
- Angular DevToolsの活用方法を習得する
- 効率的なデバッグワークフローを実現できるようになる

## 技術ポイント
- デバッグ手法
- Angular DevTools
- ブラウザ開発者ツール

## 📺 画面表示用コード

```html
<!-- デバッグ用のコンポーネント -->
<app-debug-content>
  <div class="projected-item" data-debug="true">
    <h3>デバッグ対象コンテンツ</h3>
    <p>このコンテンツの投影状況を確認</p>
  </div>
</app-debug-content>
```

```html
<!-- 子コンポーネント（app-debug-content） -->
<div class="debug-container">
  <div class="debug-info">
    <p>投影されたコンテンツ数: {{projectedContentCount}}</p>
    <p>投影状況: {{projectionStatus}}</p>
  </div>
  <div class="content-area">
    <ng-content></ng-content>
  </div>
</div>
```

```typescript
// デバッグ用のコンポーネントクラス
export class DebugContentComponent implements AfterContentInit {
  @ContentChildren('projectedItem') projectedItems!: QueryList<ElementRef>;
  
  projectedContentCount = 0;
  projectionStatus = '未初期化';
  
  ngAfterContentInit() {
    this.projectedContentCount = this.projectedItems.length;
    this.projectionStatus = '初期化完了';
    
    console.log('投影されたコンテンツ:', this.projectedItems);
    console.log('投影数:', this.projectedContentCount);
  }
}
```

## 実践的な活用例

```html
<!-- デバッグモードでの使用 -->
<app-content-debugger [debugMode]="true">
  <div class="content-block" #debugBlock>
    <h3>コンテンツブロック</h3>
    <p>デバッグ情報を表示</p>
  </div>
</app-content-debugger>
```

## ベストプラクティス
- 開発時にデバッグ情報を表示する
- Angular DevToolsを活用する
- コンソールログを適切に使用する
- 投影状況を可視化する

## 注意点
- 本番環境でのデバッグ情報の無効化
- パフォーマンスへの影響
- デバッグ情報のセキュリティ

## 関連技術
- Angular DevTools
- Browser DevTools
- Console Debugging
