# #148 「ContentChild 複数投影の参照」

## 概要
Angular v20における複数のng-contentを使ったContentChildrenの実装方法。複数の投影スロットを管理し、柔軟なレイアウトとコンテンツ制御を実現する方法を学ぶ。

## 学習目標
- 複数投影の管理方法を理解する
- ContentChildrenの使い方を学ぶ
- 動的なレイアウト制御を把握する

## 技術ポイント
- 複数のng-content スロット
- @ContentChildren() での複数参照
- QueryList での管理
- 動的なコンテンツ制御

## 📺 画面表示用コード

### 複数投影の実装
```typescript
@Component({
  selector: 'app-layout',
  template: `
    <div class="layout">
      <header>
        <ng-content select=".header-content"></ng-content>
      </header>
      <main>
        <ng-content select=".main-content"></ng-content>
      </main>
      <aside>
        <ng-content select=".sidebar-content"></ng-content>
      </aside>
      <footer>
        <ng-content select=".footer-content"></ng-content>
      </footer>
    </div>
  `
})
export class LayoutComponent implements AfterContentInit {
  @ContentChildren('.header-content') headerElements!: QueryList<ElementRef>;
  @ContentChildren('.main-content') mainElements!: QueryList<ElementRef>;
  @ContentChildren('.sidebar-content') sidebarElements!: QueryList<ElementRef>;

  ngAfterContentInit() {
    // ヘッダー要素の処理
    this.headerElements.forEach(element => {
      element.nativeElement.style.backgroundColor = '#f0f0f0';
    });

    // メイン要素の処理
    this.mainElements.forEach(element => {
      element.nativeElement.style.padding = '20px';
    });

    // サイドバー要素の処理
    this.sidebarElements.forEach(element => {
      element.nativeElement.style.backgroundColor = '#e0e0e0';
    });
  }
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-layout>
      <div class="header-content">ヘッダー</div>
      <div class="main-content">メインコンテンツ</div>
      <div class="sidebar-content">サイドバー</div>
      <div class="footer-content">フッター</div>
    </app-layout>
  `
})
export class ParentComponent {}
```

## 実践的な活用例
- ページレイアウト
- ダッシュボード
- フォームレイアウト

## ベストプラクティス
- 明確なスロット定義
- 適切なセレクタ使用
- 再利用性の考慮

## 注意点
- セレクタの一意性
- 投影コンテンツの構造
- スタイルの管理

## 関連技術
- 複数投影
- レイアウト設計
- QueryList
