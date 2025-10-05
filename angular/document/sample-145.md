# #145 「ContentChild - 投影コンテンツ参照」

## 概要
Angular v20におけるContentChildデコレータを使った投影コンテンツの参照取得。ng-contentに投影された要素を参照し、柔軟なコンテンツ制御を実現する方法を学ぶ。

## 学習目標
- ContentChildの基本的な使い方を理解する
- 投影コンテンツとの違いを学ぶ
- 柔軟なコンポーネント設計を把握する

## 技術ポイント
- @ContentChild() デコレータの使用
- 投影コンテンツの参照
- ng-content との連携
- コンポーネント設計

## 📺 画面表示用コード

### ContentChildの基本的な使用
```typescript
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <div class="card-header">
        <ng-content select="[slot=header]"></ng-content>
      </div>
      <div class="card-body">
        <ng-content></ng-content>
      </div>
      <div class="card-footer">
        <ng-content select="[slot=footer]"></ng-content>
      </div>
    </div>
  `
})
export class CardComponent implements AfterContentInit {
  @ContentChild('[slot=header]') headerElement!: ElementRef;
  @ContentChild('[slot=footer]') footerElement!: ElementRef;

  ngAfterContentInit() {
    if (this.headerElement) {
      this.headerElement.nativeElement.style.fontWeight = 'bold';
    }
    
    if (this.footerElement) {
      this.footerElement.nativeElement.style.color = 'gray';
    }
  }
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-card>
      <div slot="header">カードタイトル</div>
      <p>カードの内容です</p>
      <div slot="footer">フッター情報</div>
    </app-card>
  `
})
export class ParentComponent {}
```

## 実践的な活用例
- レイアウトコンポーネント
- モーダルダイアログ
- 再利用可能なUI部品

## ベストプラクティス
- 適切なセレクタを使用
- ngAfterContentInitでアクセス
- 存在チェックを実装

## 注意点
- 投影コンテンツの存在確認
- ライフサイクルのタイミング
- セレクタの一意性

## 関連技術
- コンテンツ投影
- ng-content
- コンポーネント設計
