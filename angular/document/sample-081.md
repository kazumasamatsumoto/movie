# #081 Lifecycle での状態初期化

## 概要
Angular v20におけるLifecycle Hooksでの状態初期化を学びます。コンポーネントの状態を適切に初期化し、安定した動作を実現する方法について解説します。

## 学習目標
- 状態初期化の基本を理解する
- 適切な初期化タイミングを把握する
- 状態管理のベストプラクティスを習得する

## 📺 画面表示用コード

```typescript
// 状態初期化の基本
export class StateInitComponent implements OnInit {
  // 状態の定義
  data: any[] = [];
  loading = false;
  error: string | null = null;
  user: User | null = null;
  
  ngOnInit() {
    this.initializeState();
  }
  
  private initializeState() {
    // 初期状態の設定
    this.data = [];
    this.loading = false;
    this.error = null;
    this.user = null;
    
    // 初期データの読み込み
    this.loadInitialData();
  }
}
```

```typescript
// 条件付き状態初期化
export class ConditionalStateComponent implements OnInit {
  @Input() mode: 'edit' | 'view' = 'view';
  
  // 状態の定義
  formData: FormData = {};
  isEditable = false;
  
  ngOnInit() {
    this.initializeStateBasedOnMode();
  }
  
  private initializeStateBasedOnMode() {
    if (this.mode === 'edit') {
      this.isEditable = true;
      this.initializeEditState();
    } else {
      this.isEditable = false;
      this.initializeViewState();
    }
  }
}
```

## 技術ポイント

### 1. 状態初期化の基本
- **初期値の設定**: 適切な初期値の設定
- **状態の一貫性**: 状態間の一貫性の確保
- **エラー状態の管理**: エラー状態の適切な管理

### 2. 初期化タイミング
- **ngOnInit**: 基本的な状態初期化
- **ngOnChanges**: 入力プロパティに基づく初期化
- **ngAfterViewInit**: ビュー関連の状態初期化

### 3. 状態管理パターン
- **単一責任**: 各状態の単一責任
- **不変性**: 状態の不変性の維持
- **予測可能性**: 状態変更の予測可能性

## 実践的な活用例

### 1. フォーム状態の初期化
```typescript
export class FormStateComponent implements OnInit {
  form: FormGroup;
  formState = {
    isDirty: false,
    isValid: false,
    isSubmitted: false
  };
  
  ngOnInit() {
    this.initializeForm();
    this.initializeFormState();
  }
  
  private initializeForm() {
    this.form = new FormGroup({
      name: new FormControl(''),
      email: new FormControl('')
    });
  }
  
  private initializeFormState() {
    this.formState = {
      isDirty: false,
      isValid: false,
      isSubmitted: false
    };
  }
}
```

### 2. データ取得状態の管理
```typescript
export class DataStateComponent implements OnInit {
  dataState = {
    items: [] as any[],
    loading: false,
    error: null as string | null,
    lastUpdated: null as Date | null
  };
  
  ngOnInit() {
    this.initializeDataState();
    this.loadData();
  }
  
  private initializeDataState() {
    this.dataState = {
      items: [],
      loading: false,
      error: null,
      lastUpdated: null
    };
  }
  
  private loadData() {
    this.dataState.loading = true;
    this.dataState.error = null;
    
    this.dataService.getData().subscribe({
      next: (data) => {
        this.dataState.items = data;
        this.dataState.loading = false;
        this.dataState.lastUpdated = new Date();
      },
      error: (error) => {
        this.dataState.error = 'データの取得に失敗しました';
        this.dataState.loading = false;
      }
    });
  }
}
```

### 3. ユーザー状態の初期化
```typescript
export class UserStateComponent implements OnInit {
  userState = {
    currentUser: null as User | null,
    isAuthenticated: false,
    permissions: [] as string[],
    preferences: {} as UserPreferences
  };
  
  ngOnInit() {
    this.initializeUserState();
    this.loadUserData();
  }
  
  private initializeUserState() {
    this.userState = {
      currentUser: null,
      isAuthenticated: false,
      permissions: [],
      preferences: {}
    };
  }
  
  private loadUserData() {
    this.authService.getCurrentUser().subscribe(user => {
      if (user) {
        this.userState.currentUser = user;
        this.userState.isAuthenticated = true;
        this.userState.permissions = user.permissions;
        this.userState.preferences = user.preferences;
      }
    });
  }
}
```

## ベストプラクティス

1. **一貫性**: 状態の一貫性を保つ
2. **予測可能性**: 状態変更の予測可能性
3. **エラーハンドリング**: 適切なエラー状態の管理
4. **パフォーマンス**: 効率的な状態管理

## 注意点

- 状態の一貫性を保つ
- 適切な初期値の設定
- エラー状態の管理
- メモリリークの防止

## 関連技術
- 状態管理
- 初期化処理
- エラーハンドリング
- Angular v20のSignal
