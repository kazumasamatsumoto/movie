# #076 Lifecycle Hooks の使い分け

## 概要
Angular v20におけるLifecycle Hooksの適切な使い分けを学びます。各Hookの特徴と用途を理解し、効率的なコンポーネント設計を行う方法について解説します。

## 学習目標
- 各Lifecycle Hookの特徴と用途を理解する
- 適切なHookの選択方法を習得する
- 効率的なコンポーネント設計を身につける

## 📺 画面表示用コード

```typescript
// 適切なHookの使い分け
export class HookSelectionComponent implements 
  OnInit, OnDestroy, OnChanges {
  
  @Input() data: any;
  
  ngOnInit() {
    // 初期化処理
    this.initializeComponent();
  }
  
  ngOnChanges(changes: SimpleChanges) {
    // 入力プロパティの変更監視
    if (changes['data']) {
      this.handleDataChange();
    }
  }
  
  ngOnDestroy() {
    // クリーンアップ処理
    this.cleanup();
  }
}
```

```typescript
// 用途別のHook選択
export class PurposeBasedComponent implements 
  OnInit, AfterViewInit, AfterContentInit {
  
  ngOnInit() {
    // データ取得
    this.loadData();
  }
  
  ngAfterContentInit() {
    // コンテンツ投影の処理
    this.setupProjectedContent();
  }
  
  ngAfterViewInit() {
    // DOM操作
    this.setupViewElements();
  }
}
```

## 技術ポイント

### 1. 主要なHookの用途
- **ngOnInit**: 初期化処理、データ取得
- **ngOnDestroy**: クリーンアップ、リソース解放
- **ngOnChanges**: 入力プロパティの変更監視
- **ngDoCheck**: カスタム変更検知
- **ngAfterViewInit**: DOM操作、フォーカス制御
- **ngAfterContentInit**: コンテンツ投影の処理

### 2. 選択の基準
- **処理の目的**: 何をしたいか
- **実行タイミング**: いつ実行したいか
- **データの可用性**: 必要なデータが利用可能か
- **パフォーマンス**: 実行頻度と処理の重さ

### 3. 組み合わせパターン
- 基本的なパターン: OnInit + OnDestroy
- 入力監視: OnInit + OnChanges + OnDestroy
- DOM操作: OnInit + AfterViewInit + OnDestroy

## 実践的な活用例

### 1. データ取得コンポーネント
```typescript
export class DataFetchComponent implements OnInit, OnDestroy {
  private subscription = new Subscription();
  
  ngOnInit() {
    // データ取得
    this.subscription.add(
      this.dataService.getData().subscribe(data => {
        this.handleData(data);
      })
    );
  }
  
  ngOnDestroy() {
    // 購読解除
    this.subscription.unsubscribe();
  }
}
```

### 2. 入力監視コンポーネント
```typescript
export class InputMonitorComponent implements OnInit, OnChanges, OnDestroy {
  @Input() userId: string = '';
  private subscription = new Subscription();
  
  ngOnInit() {
    // 初期データ取得
    this.loadUserData();
  }
  
  ngOnChanges(changes: SimpleChanges) {
    // 入力変更時の処理
    if (changes['userId'] && !changes['userId'].firstChange) {
      this.loadUserData();
    }
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
```

### 3. DOM操作コンポーネント
```typescript
export class DOMComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild('canvas') canvas?: ElementRef<HTMLCanvasElement>;
  private ctx?: CanvasRenderingContext2D;
  
  ngOnInit() {
    // 初期設定
    this.prepareCanvas();
  }
  
  ngAfterViewInit() {
    // DOM操作
    if (this.canvas) {
      this.ctx = this.canvas.nativeElement.getContext('2d');
      this.draw();
    }
  }
  
  ngOnDestroy() {
    // クリーンアップ
    this.ctx = undefined;
  }
}
```

## ベストプラクティス

1. **目的に応じた選択**: 処理の目的に応じて適切なHookを選択
2. **最小限の使用**: 必要なHookのみを使用
3. **パフォーマンス考慮**: 実行頻度と処理の重さを考慮
4. **適切な組み合わせ**: 複数Hookの適切な組み合わせ

## 注意点

- 過度なHook使用を避ける
- 適切なタイミングでの処理実行
- パフォーマンスへの影響を考慮
- メモリリークの防止

## 関連技術
- Lifecycle Hooks
- コンポーネント設計
- パフォーマンス最適化
- ベストプラクティス
