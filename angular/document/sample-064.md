# #064 ngOnInit - 初期化処理

## 概要
Angular v20におけるngOnInitの使用方法を学びます。コンポーネントの初期化処理を適切なタイミングで実行する方法について解説します。

## 学習目標
- ngOnInitの基本的な使用方法を理解する
- constructorとの違いを把握する
- 適切な初期化処理の実装方法を習得する

## 📺 画面表示用コード

```typescript
// ngOnInitの基本実装
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-init-demo',
  standalone: true,
  template: `<p>{{message}}</p>`
})
export class InitDemoComponent implements OnInit {
  message = '';
  
  ngOnInit() {
    this.message = 'コンポーネントが初期化されました';
    console.log('ngOnInit実行');
  }
}
```

```typescript
// データ初期化
export class DataInitComponent implements OnInit {
  data: any[] = [];
  
  ngOnInit() {
    this.loadInitialData();
  }
  
  private loadInitialData() {
    // 初期データの読み込み
  }
}
```

## 技術ポイント

### 1. ngOnInitの基本
ngOnInitは、コンポーネントが初期化された後に実行されるLifecycle Hookです。OnInitインターフェースを実装することで使用できます。

### 2. constructorとの違い
- **constructor**: 依存性注入、プロパティの初期化
- **ngOnInit**: データ取得、イベントリスナー登録、初期化処理

### 3. 実行タイミング
- 入力プロパティが設定された後
- コンポーネントの準備が整った後
- constructorの実行後

## 実践的な活用例

### 1. API呼び出し
```typescript
export class ApiComponent implements OnInit {
  users: User[] = [];
  
  ngOnInit() {
    this.loadUsers();
  }
  
  private loadUsers() {
    this.userService.getUsers().subscribe(users => {
      this.users = users;
    });
  }
}
```

### 2. フォーム初期化
```typescript
export class FormComponent implements OnInit {
  form: FormGroup;
  
  ngOnInit() {
    this.initializeForm();
  }
  
  private initializeForm() {
    this.form = new FormGroup({
      name: new FormControl(''),
      email: new FormControl('')
    });
  }
}
```

### 3. イベントリスナー登録
```typescript
export class EventComponent implements OnInit {
  ngOnInit() {
    this.registerEventListeners();
  }
  
  private registerEventListeners() {
    window.addEventListener('resize', this.onResize.bind(this));
  }
}
```

## ベストプラクティス

1. **適切なタイミング**: 必要な処理を適切なタイミングで実行
2. **エラーハンドリング**: 初期化処理での例外処理
3. **非同期処理**: async/awaitやObservableの活用
4. **Signalとの組み合わせ**: Angular v20の新機能を活用

## 注意点

- 重い処理は避ける
- 適切なエラーハンドリング
- メモリリークの防止
- パフォーマンスへの影響を考慮

## 関連技術
- Lifecycle Hooks
- 初期化処理
- Angular v20のSignal
- エラーハンドリング
