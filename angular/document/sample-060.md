# #060 テンプレートのよくあるエラー

## 概要
Angular v20におけるテンプレートでよく発生するエラーとその解決方法を学びます。未定義プロパティ、型エラー、バインディング構文エラーなどの典型的な問題と、適切な対処法について解説します。

## 学習目標
- テンプレートでよく発生するエラーの種類を理解する
- エラーの原因と解決方法を把握する
- 予防的なコーディング手法を習得する

## 📺 画面表示用コード

```html
<!-- エラー：未定義プロパティ -->
<p>{{user.name}}</p> <!-- userがundefinedの場合エラー -->
```

```html
<!-- 修正：安全なアクセス -->
<p>{{user?.name}}</p>
<p>{{user && user.name}}</p>
```

```html
<!-- v20のControl Flowで安全に -->
@if (user()) {
  <p>{{user()!.name}}</p>
} @else {
  <p>ユーザーが存在しません</p>
}
```

```typescript
// 型安全な実装
export class SafeComponent {
  user = signal<User | null>(null);
  
  get userName() {
    return this.user()?.name ?? 'ゲスト';
  }
}
```

## 技術ポイント

### 1. エラー：未定義プロパティ
```html
<!-- エラー：userがundefinedの場合エラー -->
<p>{{user.name}}</p>
```

### 2. 修正：安全なアクセス
```html
<!-- 修正：安全なアクセス -->
<p>{{user?.name}}</p>
<p>{{user && user.name}}</p>
```

### 3. v20のControl Flowで安全に
```html
@if (user()) {
  <p>{{user()!.name}}</p>
} @else {
  <p>ユーザーが存在しません</p>
}
```

### 4. 型安全な実装
```typescript
export class SafeComponent {
  user = signal<User | null>(null);
  
  get userName() {
    return this.user()?.name ?? 'ゲスト';
  }
}
```

## 実践的な活用例

### 1. null/undefinedエラーの対処
```typescript
export class NullSafetyComponent {
  // 問題のある実装
  user = signal<any>(null);
  items = signal<any[]>([]);
  
  // 改善された実装
  user = signal<User | null>(null);
  items = signal<Item[]>([]);
  
  // 安全なアクセス用のgetter
  get safeUserName() {
    return this.user()?.name ?? 'ゲスト';
  }
  
  get safeUserEmail() {
    return this.user()?.email ?? 'メールアドレスなし';
  }
  
  get hasItems() {
    return this.items().length > 0;
  }
  
  get firstItem() {
    return this.items()[0] ?? null;
  }
}
```

```html
<!-- 問題のある実装 -->
<div>
  <h2>{{user.name}}</h2>
  <p>{{user.email}}</p>
  <p>アイテム数: {{items.length}}</p>
  <p>最初のアイテム: {{items[0].name}}</p>
</div>

<!-- 改善された実装 -->
<div>
  <h2>{{safeUserName}}</h2>
  <p>{{safeUserEmail}}</p>
  
  @if (hasItems) {
    <p>アイテム数: {{items().length}}</p>
    @if (firstItem) {
      <p>最初のアイテム: {{firstItem.name}}</p>
    }
  } @else {
    <p>アイテムがありません</p>
  }
</div>
```

### 2. 型エラーの対処
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

interface Item {
  id: number;
  title: string;
  description: string;
  price: number;
}

export class TypeSafetyComponent {
  // 型安全なSignal定義
  user = signal<User | null>(null);
  items = signal<Item[]>([]);
  loading = signal<boolean>(false);
  error = signal<string | null>(null);
  
  // 型安全なメソッド
  getUserDisplayName(): string {
    const user = this.user();
    if (!user) {
      return 'ユーザーなし';
    }
    return user.name;
  }
  
  getTotalPrice(): number {
    return this.items().reduce((sum, item) => sum + item.price, 0);
  }
  
  getFormattedPrice(price: number): string {
    return new Intl.NumberFormat('ja-JP', {
      style: 'currency',
      currency: 'JPY'
    }).format(price);
  }
  
  // エラーハンドリング
  handleError(error: any): void {
    console.error('エラーが発生しました:', error);
    this.error.set(error.message || '不明なエラーが発生しました');
  }
}
```

```html
<!-- 型安全なテンプレート -->
<div class="type-safe-container">
  @if (loading()) {
    <div class="loading">読み込み中...</div>
  } @else if (error()) {
    <div class="error">
      <h3>エラーが発生しました</h3>
      <p>{{error()}}</p>
      <button (click)="error.set(null)">エラーをクリア</button>
    </div>
  } @else {
    <div class="content">
      <h2>{{getUserDisplayName()}}</h2>
      
      @if (items().length > 0) {
        <div class="items">
          <h3>アイテム一覧</h3>
          @for (item of items(); track item.id) {
            <div class="item">
              <h4>{{item.title}}</h4>
              <p>{{item.description}}</p>
              <p class="price">{{getFormattedPrice(item.price)}}</p>
            </div>
          }
          
          <div class="total">
            <strong>合計: {{getFormattedPrice(getTotalPrice())}}</strong>
          </div>
        </div>
      } @else {
        <p>アイテムがありません</p>
      }
    </div>
  }
</div>
```

### 3. バインディング構文エラーの対処
```typescript
export class BindingErrorComponent {
  // 正しい型定義
  counter = signal<number>(0);
  message = signal<string>('');
  isVisible = signal<boolean>(true);
  items = signal<string[]>([]);
  
  // 正しいメソッド定義
  increment(): void {
    this.counter.update(c => c + 1);
  }
  
  decrement(): void {
    this.counter.update(c => c - 1);
  }
  
  updateMessage(newMessage: string): void {
    this.message.set(newMessage);
  }
  
  toggleVisibility(): void {
    this.isVisible.update(v => !v);
  }
  
  addItem(item: string): void {
    this.items.update(items => [...items, item]);
  }
  
  removeItem(index: number): void {
    this.items.update(items => items.filter((_, i) => i !== index));
  }
}
```

```html
<!-- 正しいバインディング構文 -->
<div class="binding-examples">
  <!-- プロパティバインディング -->
  <div [class.visible]="isVisible()" [class.hidden]="!isVisible()">
    <h3>カウンター: {{counter()}}</h3>
    <p>メッセージ: {{message()}}</p>
  </div>
  
  <!-- イベントバインディング -->
  <div class="controls">
    <button (click)="increment()">増加</button>
    <button (click)="decrement()">減少</button>
    <button (click)="toggleVisibility()">
      {{isVisible() ? '非表示' : '表示'}}
    </button>
  </div>
  
  <!-- 双方向バインディング -->
  <div class="form">
    <input 
      [value]="message()" 
      (input)="updateMessage($event.target.value)"
      placeholder="メッセージを入力">
  </div>
  
  <!-- リストバインディング -->
  <div class="list">
    <h4>アイテム一覧</h4>
    @for (item of items(); track $index; let i = $index) {
      <div class="list-item">
        <span>{{item}}</span>
        <button (click)="removeItem(i)">削除</button>
      </div>
    }
    
    <div class="add-item">
      <input #newItemInput placeholder="新しいアイテム">
      <button (click)="addItem(newItemInput.value); newItemInput.value = ''">
        追加
      </button>
    </div>
  </div>
</div>
```

### 4. フォームエラーの対処
```typescript
export class FormErrorComponent {
  // フォームデータの型定義
  formData = signal({
    name: '',
    email: '',
    age: 0
  });
  
  // バリデーションエラー
  validationErrors = signal<Record<string, string>>({});
  
  // フォームの状態
  isSubmitting = signal<boolean>(false);
  submitError = signal<string | null>(null);
  
  // バリデーション
  validateForm(): boolean {
    const data = this.formData();
    const errors: Record<string, string> = {};
    
    // 名前のバリデーション
    if (!data.name.trim()) {
      errors.name = '名前は必須です';
    } else if (data.name.length < 2) {
      errors.name = '名前は2文字以上で入力してください';
    }
    
    // メールのバリデーション
    if (!data.email.trim()) {
      errors.email = 'メールアドレスは必須です';
    } else if (!this.isValidEmail(data.email)) {
      errors.email = '有効なメールアドレスを入力してください';
    }
    
    // 年齢のバリデーション
    if (data.age < 0) {
      errors.age = '年齢は0以上で入力してください';
    } else if (data.age > 150) {
      errors.age = '年齢は150以下で入力してください';
    }
    
    this.validationErrors.set(errors);
    return Object.keys(errors).length === 0;
  }
  
  private isValidEmail(email: string): boolean {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
  
  // フォーム送信
  async submitForm(): Promise<void> {
    if (!this.validateForm()) {
      return;
    }
    
    this.isSubmitting.set(true);
    this.submitError.set(null);
    
    try {
      // フォーム送信のシミュレーション
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      console.log('フォーム送信成功:', this.formData());
      // 成功時の処理
      
    } catch (error) {
      this.submitError.set('フォーム送信に失敗しました');
      console.error('フォーム送信エラー:', error);
    } finally {
      this.isSubmitting.set(false);
    }
  }
  
  // フィールド更新
  updateField(field: keyof typeof this.formData, value: any): void {
    this.formData.update(data => ({
      ...data,
      [field]: value
    }));
    
    // リアルタイムバリデーション
    this.validateForm();
  }
}
```

```html
<!-- エラーハンドリング付きフォーム -->
<form (ngSubmit)="submitForm()">
  <div class="form-container">
    <h2>ユーザー登録フォーム</h2>
    
    <!-- 名前フィールド -->
    <div class="field">
      <label for="name">名前 *</label>
      <input 
        id="name"
        type="text"
        [value]="formData().name"
        (input)="updateField('name', $event.target.value)"
        [class.error]="validationErrors()['name']"
        placeholder="名前を入力してください">
      
      @if (validationErrors()['name']) {
        <span class="error-message">{{validationErrors()['name']}}</span>
      }
    </div>
    
    <!-- メールフィールド -->
    <div class="field">
      <label for="email">メールアドレス *</label>
      <input 
        id="email"
        type="email"
        [value]="formData().email"
        (input)="updateField('email', $event.target.value)"
        [class.error]="validationErrors()['email']"
        placeholder="メールアドレスを入力してください">
      
      @if (validationErrors()['email']) {
        <span class="error-message">{{validationErrors()['email']}}</span>
      }
    </div>
    
    <!-- 年齢フィールド -->
    <div class="field">
      <label for="age">年齢 *</label>
      <input 
        id="age"
        type="number"
        [value]="formData().age"
        (input)="updateField('age', +$event.target.value)"
        [class.error]="validationErrors()['age']"
        placeholder="年齢を入力してください">
      
      @if (validationErrors()['age']) {
        <span class="error-message">{{validationErrors()['age']}}</span>
      }
    </div>
    
    <!-- 送信エラー表示 -->
    @if (submitError()) {
      <div class="submit-error">
        <p>{{submitError()}}</p>
      </div>
    }
    
    <!-- 送信ボタン -->
    <button 
      type="submit"
      [disabled]="isSubmitting() || Object.keys(validationErrors()).length > 0"
      class="submit-button">
      
      @if (isSubmitting()) {
        送信中...
      } @else {
        送信
      }
    </button>
  </div>
</form>
```

### 5. 非同期処理エラーの対処
```typescript
export class AsyncErrorComponent {
  data = signal<any[]>([]);
  loading = signal<boolean>(false);
  error = signal<string | null>(null);
  
  // 非同期データ取得
  async loadData(): Promise<void> {
    this.loading.set(true);
    this.error.set(null);
    
    try {
      // 実際のAPI呼び出しをシミュレート
      const response = await this.simulateApiCall();
      this.data.set(response);
      
    } catch (error) {
      this.error.set(this.getErrorMessage(error));
      console.error('データ取得エラー:', error);
      
    } finally {
      this.loading.set(false);
    }
  }
  
  private async simulateApiCall(): Promise<any[]> {
    // ランダムにエラーを発生させる
    if (Math.random() < 0.3) {
      throw new Error('サーバーエラーが発生しました');
    }
    
    // データ取得をシミュレート
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    return [
      { id: 1, name: 'アイテム1', description: '説明1' },
      { id: 2, name: 'アイテム2', description: '説明2' },
      { id: 3, name: 'アイテム3', description: '説明3' }
    ];
  }
  
  private getErrorMessage(error: any): string {
    if (error instanceof Error) {
      return error.message;
    }
    return '不明なエラーが発生しました';
  }
  
  // リトライ機能
  async retry(): Promise<void> {
    await this.loadData();
  }
}
```

```html
<!-- 非同期処理エラーハンドリング -->
<div class="async-container">
  <h2>データ取得</h2>
  
  <div class="controls">
    <button (click)="loadData()" [disabled]="loading()">
      {{loading() ? '読み込み中...' : 'データを取得'}}
    </button>
    
    @if (error()) {
      <button (click)="retry()" class="retry-button">再試行</button>
    }
  </div>
  
  <!-- ローディング状態 -->
  @if (loading()) {
    <div class="loading">
      <p>データを読み込み中...</p>
    </div>
  }
  
  <!-- エラー状態 -->
  @else if (error()) {
    <div class="error">
      <h3>エラーが発生しました</h3>
      <p>{{error()}}</p>
      <button (click)="retry()">再試行</button>
    </div>
  }
  
  <!-- データ表示 -->
  @else if (data().length > 0) {
    <div class="data-list">
      <h3>データ一覧</h3>
      @for (item of data(); track item.id) {
        <div class="data-item">
          <h4>{{item.name}}</h4>
          <p>{{item.description}}</p>
        </div>
      }
    </div>
  }
  
  <!-- データなし -->
  @else {
    <div class="no-data">
      <p>データがありません</p>
      <button (click)="loadData()">データを取得</button>
    </div>
  }
</div>
```

## エラーパターンと解決方法

### 1. よくあるエラーパターン
```typescript
// エラー例1: 未定義プロパティ
// ❌ エラー: Cannot read property 'name' of undefined
user.name

// ✅ 解決: 安全なアクセス
user?.name
user && user.name
```

```typescript
// エラー例2: 型エラー
// ❌ エラー: Type 'string' is not assignable to type 'number'
age = '25'

// ✅ 解決: 適切な型変換
age = 25
age = +'25'
age = parseInt('25', 10)
```

```typescript
// エラー例3: 配列アクセスエラー
// ❌ エラー: Cannot read property 'name' of undefined
items[0].name

// ✅ 解決: 安全な配列アクセス
items[0]?.name
items.length > 0 ? items[0].name : 'なし'
```

### 2. 予防的なコーディング
```typescript
export class PreventiveCodingComponent {
  // 型定義を明確にする
  user = signal<User | null>(null);
  items = signal<Item[]>([]);
  
  // デフォルト値を設定
  defaultUser: User = {
    id: 0,
    name: 'ゲスト',
    email: '',
    age: 0
  };
  
  // 安全なアクセス用メソッド
  getSafeUser(): User {
    return this.user() ?? this.defaultUser;
  }
  
  getSafeItems(): Item[] {
    return this.items() ?? [];
  }
  
  // バリデーション付きメソッド
  updateUser(updates: Partial<User>): void {
    const currentUser = this.user();
    if (currentUser) {
      this.user.set({ ...currentUser, ...updates });
    }
  }
}
```

## ベストプラクティス

1. **型安全性**: TypeScriptの型定義を活用
2. **null安全性**: 安全なアクセス演算子を使用
3. **エラーハンドリング**: 適切なエラーハンドリングを実装
4. **予防的コーディング**: エラーが発生しにくいコードを書く
5. **テスト**: エラーケースも含めてテスト

## 注意点

- 本番環境でのエラー情報の漏洩に注意
- ユーザーフレンドリーなエラーメッセージ
- 適切なログ出力
- エラーの根本原因を特定

## 関連技術
- TypeScript型安全性
- エラーハンドリング
- null安全性
- バリデーション
- デバッグ手法
