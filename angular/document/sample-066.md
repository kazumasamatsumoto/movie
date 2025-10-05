# #066 constructor vs ngOnInit の使い分け

## 概要
Angular v20におけるconstructorとngOnInitの適切な使い分けを学びます。それぞれの役割と実行タイミングを理解し、効率的なコンポーネント設計を行う方法について解説します。

## 学習目標
- constructorとngOnInitの役割の違いを理解する
- 実行タイミングの違いを把握する
- 適切な使い分け方法を習得する

## 📺 画面表示用コード

```typescript
// constructorとngOnInitの適切な使い分け
export class ProperUsageComponent implements OnInit {
  private dataService: DataService;
  data: any[] = [];
  
  // constructor: 依存性注入
  constructor(dataService: DataService) {
    this.dataService = dataService;
    console.log('constructor実行');
  }
  
  // ngOnInit: 初期化処理
  ngOnInit() {
    this.loadData();
    console.log('ngOnInit実行');
  }
  
  private loadData() {
    this.dataService.getData().subscribe(data => {
      this.data = data;
    });
  }
}
```

```typescript
// 実行順序の確認
export class ExecutionOrderComponent implements OnInit {
  constructor() {
    console.log('1. constructor実行');
  }
  
  ngOnInit() {
    console.log('2. ngOnInit実行');
  }
}
```

## 技術ポイント

### 1. constructorの役割
- **依存性注入**: サービスの注入
- **プロパティの初期化**: 基本的な値の設定
- **オブジェクトの作成**: インスタンスの準備

### 2. ngOnInitの役割
- **データ取得**: API呼び出し
- **イベントリスナー登録**: DOMイベントの設定
- **初期化処理**: コンポーネントの準備

### 3. 実行タイミング
1. **constructor**: 最初に実行
2. **ngOnInit**: 入力プロパティ設定後に実行

## 実践的な活用例

### 1. 依存性注入とデータ取得
```typescript
export class ServiceComponent implements OnInit {
  private userService: UserService;
  private configService: ConfigService;
  
  constructor(
    userService: UserService,
    configService: ConfigService
  ) {
    this.userService = userService;
    this.configService = configService;
  }
  
  ngOnInit() {
    this.loadUserData();
    this.applyConfiguration();
  }
  
  private loadUserData() {
    this.userService.getCurrentUser().subscribe(user => {
      // ユーザーデータの処理
    });
  }
  
  private applyConfiguration() {
    const config = this.configService.getConfig();
    // 設定の適用
  }
}
```

### 2. フォームの初期化
```typescript
export class FormInitComponent implements OnInit {
  form: FormGroup;
  
  constructor(private fb: FormBuilder) {
    // FormBuilderの注入のみ
  }
  
  ngOnInit() {
    this.initializeForm();
  }
  
  private initializeForm() {
    this.form = this.fb.group({
      name: [''],
      email: ['']
    });
  }
}
```

### 3. 設定とイベントリスナー
```typescript
export class ConfigComponent implements OnInit {
  private settings: Settings = {};
  
  constructor(private configService: ConfigService) {
    // 設定サービスの注入
  }
  
  ngOnInit() {
    this.loadSettings();
    this.setupEventListeners();
  }
  
  private loadSettings() {
    this.settings = this.configService.getSettings();
  }
  
  private setupEventListeners() {
    window.addEventListener('resize', this.onResize.bind(this));
  }
}
```

## ベストプラクティス

1. **役割の分離**: constructorとngOnInitの役割を明確に分ける
2. **実行順序の理解**: 適切なタイミングでの処理実行
3. **依存性注入**: constructorでのサービスの注入
4. **初期化処理**: ngOnInitでのデータ取得と設定

## 注意点

- constructorでは重い処理を避ける
- ngOnInitでは入力プロパティが利用可能
- 適切なエラーハンドリング
- メモリリークの防止

## 関連技術
- 依存性注入
- Lifecycle Hooks
- 初期化処理
- Angular v20のSignal
