# #151 「ViewChild vs ContentChild 使い分け」

## 概要
Angular v20におけるViewChildとContentChildの適切な使い分け。要素の場所と用途に応じて最適な参照方法を選択し、柔軟で保守性の高いコンポーネント設計を実現する方法を学ぶ。

## 学習目標
- ViewChildとContentChildの違いを理解する
- 適切な使い分けの基準を学ぶ
- コンポーネント設計の最適化を把握する

## 技術ポイント
- ViewChild: テンプレート内要素の参照
- ContentChild: 投影コンテンツの参照
- 使い分けの判断基準
- コンポーネント設計への影響

## 📺 画面表示用コード

### ViewChildの使用場面
```typescript
@Component({
  selector: 'app-viewchild-example',
  template: `
    <div #internalElement>内部要素</div>
    <button (click)="accessInternal()">内部要素アクセス</button>
  `
})
export class ViewChildExampleComponent implements AfterViewInit {
  @ViewChild('internalElement') internalElement!: ElementRef;

  ngAfterViewInit() {
    console.log('ViewChild:', this.internalElement);
  }

  accessInternal() {
    this.internalElement.nativeElement.style.color = 'red';
  }
}
```

### ContentChildの使用場面
```typescript
@Component({
  selector: 'app-contentchild-example',
  template: `
    <div class="container">
      <ng-content></ng-content>
    </div>
  `
})
export class ContentChildExampleComponent implements AfterContentInit {
  @ContentChild('.projected-content') projectedContent!: ElementRef;

  ngAfterContentInit() {
    if (this.projectedContent) {
      this.projectedContent.nativeElement.style.border = '1px solid blue';
    }
  }
}
```

## 実践的な活用例
- 内部要素制御: ViewChild
- 投影コンテンツ制御: ContentChild
- レイアウトコンポーネント設計

## ベストプラクティス
- 要素の場所で使い分ける
- 適切なライフサイクルを使用
- 明確な責任分離

## 注意点
- 参照のタイミング
- 存在チェックの実装
- パフォーマンスの考慮

## 関連技術
- コンポーネント設計
- 要素参照
- ライフサイクル
