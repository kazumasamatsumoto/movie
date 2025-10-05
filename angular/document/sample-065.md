# #065 ngOnInit のベストプラクティス

## 概要
Angular v20におけるngOnInitのベストプラクティスを学びます。効率的で保守性の高い初期化処理の実装方法について解説します。

## 学習目標
- ngOnInitでの適切な処理の種類を理解する
- 避けるべき処理を把握する
- エラーハンドリングとパフォーマンス最適化を習得する

## 📺 画面表示用コード

```typescript
// 適切なngOnInitの実装
export class BestPracticeComponent implements OnInit {
  data: any[] = [];
  loading = false;
  
  ngOnInit() {
    this.initializeComponent();
  }
  
  private async initializeComponent() {
    try {
      this.loading = true;
      await this.loadData();
    } catch (error) {
      this.handleError(error);
    } finally {
      this.loading = false;
    }
  }
}
```

```typescript
// エラーハンドリング付き
ngOnInit() {
  this.loadData().catch(error => {
    console.error('データ読み込みエラー:', error);
  });
}
```

## 技術ポイント

### 1. 適切な処理の種類
ngOnInitで実行すべき処理：
- データの初期化
- API呼び出し
- イベントリスナー登録
- フォームの初期化

### 2. 避けるべき処理
ngOnInitで避けるべき処理：
- 重い同期的な処理
- DOM操作（ngAfterViewInit以降が適切）
- 無限ループを引き起こす処理

### 3. エラーハンドリング
- try-catch文の使用
- 非同期処理での適切なエラーハンドリング
- ユーザーフレンドリーなエラーメッセージ

## 実践的な活用例

### 1. 非同期データ取得
```typescript
export class AsyncDataComponent implements OnInit {
  users: User[] = [];
  error: string | null = null;
  
  ngOnInit() {
    this.loadUsers();
  }
  
  private async loadUsers() {
    try {
      this.users = await this.userService.getUsers().toPromise();
    } catch (error) {
      this.error = 'ユーザーデータの読み込みに失敗しました';
      console.error('Error loading users:', error);
    }
  }
}
```

### 2. 複数の初期化処理
```typescript
export class MultiInitComponent implements OnInit {
  ngOnInit() {
    this.initializeData();
    this.setupEventListeners();
    this.configureSettings();
  }
  
  private initializeData() {
    // データ初期化
  }
  
  private setupEventListeners() {
    // イベントリスナー設定
  }
  
  private configureSettings() {
    // 設定の適用
  }
}
```

### 3. 条件付き初期化
```typescript
export class ConditionalInitComponent implements OnInit {
  @Input() mode: 'edit' | 'view' = 'view';
  
  ngOnInit() {
    if (this.mode === 'edit') {
      this.initializeEditMode();
    } else {
      this.initializeViewMode();
    }
  }
  
  private initializeEditMode() {
    // 編集モードの初期化
  }
  
  private initializeViewMode() {
    // 表示モードの初期化
  }
}
```

## ベストプラクティス

1. **単一責任の原則**: 各初期化処理を分離
2. **エラーハンドリング**: 適切な例外処理
3. **非同期処理**: async/awaitの活用
4. **パフォーマンス**: 軽量で効率的な処理

## 注意点

- 重い処理は避ける
- 適切なエラーハンドリング
- メモリリークの防止
- ユーザーエクスペリエンスの考慮

## 関連技術
- 非同期処理
- エラーハンドリング
- パフォーマンス最適化
- Angular v20のSignal
