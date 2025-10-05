# #147 「ContentChild と ng-content」

## 概要
Angular v20におけるContentChildとng-contentの組み合わせ。投影されたコンテンツを参照し、動的な制御やスタイル適用を実現する柔軟なコンポーネント設計方法を学ぶ。

## 学習目標
- ng-contentとContentChildの連携を理解する
- 動的コンテンツ制御を学ぶ
- 再利用可能なコンポーネント設計を把握する

## 技術ポイント
- ng-content でのコンテンツ投影
- ContentChild での参照取得
- 動的なコンテンツ制御
- 条件付き投影

## 📺 画面表示用コード

### ng-contentとContentChildの組み合わせ
```typescript
@Component({
  selector: 'app-panel',
  template: `
    <div class="panel">
      <div class="panel-header">
        <ng-content select=".panel-title"></ng-content>
      </div>
      <div class="panel-content">
        <ng-content></ng-content>
      </div>
      <div class="panel-actions">
        <ng-content select=".panel-actions"></ng-content>
      </div>
    </div>
  `
})
export class PanelComponent implements AfterContentInit {
  @ContentChild('.panel-title') titleElement!: ElementRef;
  @ContentChild('.panel-actions') actionsElement!: ElementRef;

  ngAfterContentInit() {
    if (this.titleElement) {
      this.titleElement.nativeElement.style.color = '#333';
    }
    
    if (this.actionsElement) {
      this.actionsElement.nativeElement.style.marginTop = '10px';
    }
  }
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-panel>
      <h2 class="panel-title">パネルタイトル</h2>
      <p>パネルの内容です</p>
      <div class="panel-actions">
        <button>保存</button>
        <button>キャンセル</button>
      </div>
    </app-panel>
  `
})
export class ParentComponent {}
```

## 実践的な活用例
- レイアウトコンポーネント
- モーダルダイアログ
- カードコンポーネント

## ベストプラクティス
- 明確なセレクタ指定
- 適切な構造設計
- 再利用性を考慮

## 注意点
- 投影コンテンツの構造
- セレクタの一意性
- スタイルの競合回避

## 関連技術
- コンテンツ投影
- コンポーネント設計
- CSS セレクタ
