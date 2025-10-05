# #208 「投影されたコンテンツの操作」

## 概要
Angular v20で投影されたコンテンツを動的に操作する方法を学習します。

## 学習目標
- 投影コンテンツの動的操作方法を理解する
- DOM操作とコンテンツ投影の組み合わせを習得する
- 高度なコンテンツ投影制御を実現できるようになる

## 技術ポイント
- 投影コンテンツ操作
- DOM操作
- 動的制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-content-controller>
  <div #contentBlock class="content-block">
    <h3>操作可能なコンテンツ</h3>
    <p>このコンテンツは動的に操作されます</p>
  </div>
</app-content-controller>
```

```html
<!-- 子コンポーネント（app-content-controller） -->
<div class="controller-container">
  <div class="controls">
    <button (click)="showContent()">表示</button>
    <button (click)="hideContent()">非表示</button>
    <button (click)="highlightContent()">ハイライト</button>
  </div>
  <ng-content></ng-content>
</div>
```

```typescript
// 子コンポーネントクラス
export class ContentControllerComponent implements AfterContentInit {
  @ContentChild('contentBlock') contentBlock!: ElementRef;
  
  ngAfterContentInit() {
    this.initializeContent();
  }
  
  showContent() {
    this.contentBlock.nativeElement.style.display = 'block';
  }
  
  hideContent() {
    this.contentBlock.nativeElement.style.display = 'none';
  }
  
  highlightContent() {
    this.contentBlock.nativeElement.classList.add('highlighted');
  }
}
```

## 実践的な活用例

```html
<!-- 動的フォーム -->
<app-form-manager>
  <form #dynamicForm class="dynamic-form">
    <input type="text" placeholder="名前">
    <input type="email" placeholder="メール">
  </form>
</app-form-manager>
```

## ベストプラクティス
- 投影コンテンツの操作は安全に行う
- 適切なエラーハンドリングを実装する
- パフォーマンスを考慮した操作を行う

## 注意点
- DOM操作の安全性
- 投影コンテンツの存在チェック
- メモリリークの防止

## 関連技術
- DOM Manipulation
- ElementRef
- ContentChild
