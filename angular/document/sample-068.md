# #068 ngAfterContentInit - コンテンツ投影後

## 概要
Angular v20におけるngAfterContentInitの使用方法を学びます。ng-contentによるコンテンツ投影が完了した後に処理を実行する方法について解説します。

## 学習目標
- ngAfterContentInitの基本的な使用方法を理解する
- コンテンツ投影のタイミングを把握する
- ContentChild/ContentChildrenの活用方法を習得する

## 📺 画面表示用コード

```typescript
// ngAfterContentInitの基本実装
export class ContentProjectionComponent implements AfterContentInit {
  @ContentChild('projectedContent') projectedElement?: ElementRef;
  
  ngAfterContentInit() {
    console.log('コンテンツ投影が完了しました');
    if (this.projectedElement) {
      this.setupProjectedContent();
    }
  }
  
  private setupProjectedContent() {
    // 投影されたコンテンツの設定
  }
}
```

```typescript
// ContentChildrenの活用
export class MultipleContentComponent implements AfterContentInit {
  @ContentChildren(ChildComponent) children?: QueryList<ChildComponent>;
  
  ngAfterContentInit() {
    this.children?.forEach(child => {
      child.initialize();
    });
  }
}
```

## 技術ポイント

### 1. ngAfterContentInitの基本
ngAfterContentInitは、コンテンツ投影が完了した後に実行されるHookです。AfterContentInitインターフェースを実装することで使用できます。

### 2. 実行タイミング
- 子コンポーネントの初期化後
- 親のngOnInit後
- コンテンツ投影の完了後

### 3. ContentChild/ContentChildren
投影されたコンテンツにアクセスするためのデコレータ：
- `ContentChild`: 単一の投影コンテンツ
- `ContentChildren`: 複数の投影コンテンツ

## 実践的な活用例

### 1. 投影コンテンツの初期化
```typescript
export class CardComponent implements AfterContentInit {
  @ContentChild('header') header?: ElementRef;
  @ContentChild('body') body?: ElementRef;
  
  ngAfterContentInit() {
    this.initializeCard();
  }
  
  private initializeCard() {
    if (this.header) {
      this.header.nativeElement.classList.add('card-header');
    }
    if (this.body) {
      this.body.nativeElement.classList.add('card-body');
    }
  }
}
```

### 2. 複数コンテンツの管理
```typescript
export class TabContainerComponent implements AfterContentInit {
  @ContentChildren(TabComponent) tabs?: QueryList<TabComponent>;
  
  ngAfterContentInit() {
    if (this.tabs) {
      this.setupTabs();
    }
  }
  
  private setupTabs() {
    this.tabs!.forEach((tab, index) => {
      tab.setIndex(index);
      if (index === 0) {
        tab.activate();
      }
    });
  }
}
```

### 3. 動的コンテンツの処理
```typescript
export class DynamicContentComponent implements AfterContentInit {
  @ContentChildren(ItemComponent) items?: QueryList<ItemComponent>;
  
  ngAfterContentInit() {
    this.items?.changes.subscribe(() => {
      this.updateLayout();
    });
  }
  
  private updateLayout() {
    // レイアウトの更新
  }
}
```

## ベストプラクティス

1. **適切なタイミング**: コンテンツ投影完了後の処理実行
2. **ContentChild/ContentChildrenの活用**: 投影コンテンツへの適切なアクセス
3. **エラーハンドリング**: 投影コンテンツの存在チェック
4. **パフォーマンス考慮**: 効率的な投影コンテンツの処理

## 注意点

- 投影コンテンツが存在する場合のみ処理を実行
- 適切なエラーハンドリングの実装
- パフォーマンスへの影響を考慮
- コンテンツ投影のタイミングを理解

## 関連技術
- コンテンツ投影
- ContentChild/ContentChildren
- AfterContentInit
- Angular v20のSignal
