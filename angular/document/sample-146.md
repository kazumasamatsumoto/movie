# #146 「ContentChild の基本構文」

## 概要
Angular v20におけるContentChildの基本構文とセレクタ指定方法。コンポーネントクラス、ディレクティブ、テンプレート参照変数など、様々なセレクタを使用した投影コンテンツ参照の実装方法を学ぶ。

## 学習目標
- ContentChildの基本構文を理解する
- セレクタの種類と使い分けを学ぶ
- 投影コンテンツの参照方法を把握する

## 技術ポイント
- @ContentChild() の基本構文
- セレクタの種類（クラス、文字列、型）
- 投影コンテンツの参照
- 型安全性の確保

## 📺 画面表示用コード

### コンポーネントクラスでの参照
```typescript
@Component({
  selector: 'app-container',
  template: `
    <div class="container">
      <ng-content></ng-content>
    </div>
  `
})
export class ContainerComponent implements AfterContentInit {
  @ContentChild(ChildComponent) childComponent!: ChildComponent;

  ngAfterContentInit() {
    if (this.childComponent) {
      this.childComponent.initialize();
    }
  }
}
```

### テンプレート参照変数での参照
```typescript
@Component({
  selector: 'app-wrapper',
  template: `
    <div class="wrapper">
      <ng-content></ng-content>
    </div>
  `
})
export class WrapperComponent implements AfterContentInit {
  @ContentChild('#contentRef') contentElement!: ElementRef;

  ngAfterContentInit() {
    if (this.contentElement) {
      this.contentElement.nativeElement.style.border = '1px solid #ccc';
    }
  }
}
```

## 実践的な活用例
- レイアウトコンポーネント
- フォームラッパー
- カードコンポーネント

## ベストプラクティス
- 適切なセレクタタイプを選択
- 型安全性を保つ
- ngAfterContentInitでアクセス

## 注意点
- 投影コンテンツの存在チェック
- セレクタの一意性
- ライフサイクルのタイミング

## 関連技術
- コンテンツ投影
- セレクタ指定
- 型安全性
