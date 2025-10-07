# #009 「Component クラスの基本構造」

## 概要
Componentクラスは、プロパティ、メソッド、ライフサイクルフックで構成されます。テンプレートで使用するデータとロジックを定義します。

## 学習目標
- Componentクラスの基本構造を理解する
- プロパティとメソッドの定義方法を習得する
- クラスの役割と責務を理解する

## 技術ポイント
- **プロパティ**: テンプレートで使用するデータ
- **メソッド**: イベント処理とビジネスロジック
- **TypeScriptクラス**: 型安全なComponent定義

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 基本的なComponentクラス
@Component({
  selector: 'app-user',
  template: '<p>{{name}}</p>'
})
export class UserComponent {
  name = 'John Doe';  // プロパティ

  greet() {           // メソッド
    console.log('Hello!');
  }
}
```

```typescript
// 型付きプロパティ
@Component({
  selector: 'app-product',
  template: '<h2>{{product.name}}: ¥{{product.price}}</h2>'
})
export class ProductComponent {
  product: { name: string; price: number } = {
    name: 'Laptop',
    price: 1200
  };
}
```

```typescript
// イベント処理を含む構造
@Component({
  selector: 'app-counter',
  template: '<button (click)="increment()">{{count}}</button>'
})
export class CounterComponent {
  count = 0;

  increment() {
    this.count++;
  }
}
```

## 💻 詳細実装例（学習用）

### 基本的なクラス構造
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  // プロパティ（パブリック）
  userName = 'John Doe';
  userEmail = 'john@example.com';
  isActive = true;

  // プライベートプロパティ
  private userId = 123;

  // 型定義されたプロパティ
  age: number = 25;
  hobbies: string[] = ['Reading', 'Gaming'];

  // メソッド
  displayUserInfo() {
    console.log(`Name: ${this.userName}, Email: ${this.userEmail}`);
  }

  // プライベートメソッド
  private validateUser(): boolean {
    return this.userId > 0;
  }
}
```

### インターフェースを使った型定義
```typescript
import { Component } from '@angular/core';

// インターフェース定義
interface User {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
}

interface Product {
  id: number;
  name: string;
  price: number;
  inStock: boolean;
}

@Component({
  selector: 'app-shop',
  standalone: true,
  template: `
    <div>
      <h2>User: {{currentUser.name}}</h2>
      <h3>Products</h3>
      <ul>
        <li *ngFor="let product of products">
          {{product.name}} - ¥{{product.price}}
        </li>
      </ul>
    </div>
  `
})
export class ShopComponent {
  // インターフェースを使った型定義
  currentUser: User = {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com',
    role: 'admin'
  };

  products: Product[] = [
    { id: 1, name: 'Laptop', price: 1200, inStock: true },
    { id: 2, name: 'Mouse', price: 25, inStock: true },
    { id: 3, name: 'Keyboard', price: 75, inStock: false }
  ];

  // 型安全なメソッド
  addProduct(product: Product): void {
    this.products.push(product);
  }

  getAvailableProducts(): Product[] {
    return this.products.filter(p => p.inStock);
  }

  getUserRole(): string {
    return this.currentUser.role;
  }
}
```

### ゲッターとセッターの使用
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-temperature',
  standalone: true,
  template: `
    <div>
      <p>Celsius: {{celsius}}°C</p>
      <p>Fahrenheit: {{fahrenheit}}°F</p>
      <button (click)="increaseCelsius()">+</button>
      <button (click)="decreaseCelsius()">-</button>
    </div>
  `
})
export class TemperatureComponent {
  private _celsius = 0;

  // ゲッター
  get celsius(): number {
    return this._celsius;
  }

  // セッター
  set celsius(value: number) {
    this._celsius = value;
  }

  // 計算プロパティ
  get fahrenheit(): number {
    return (this._celsius * 9/5) + 32;
  }

  increaseCelsius() {
    this.celsius++;
  }

  decreaseCelsius() {
    this.celsius--;
  }
}
```

### 配列とオブジェクト操作
```typescript
import { Component } from '@angular/core';

interface Task {
  id: number;
  title: string;
  completed: boolean;
  priority: 'low' | 'medium' | 'high';
}

@Component({
  selector: 'app-task-manager',
  standalone: true,
  templateUrl: './task-manager.component.html'
})
export class TaskManagerComponent {
  tasks: Task[] = [
    { id: 1, title: 'Learn Angular', completed: false, priority: 'high' },
    { id: 2, title: 'Build app', completed: false, priority: 'medium' }
  ];

  newTaskTitle = '';

  // 追加
  addTask() {
    if (this.newTaskTitle.trim()) {
      const newTask: Task = {
        id: this.getNextId(),
        title: this.newTaskTitle,
        completed: false,
        priority: 'medium'
      };
      this.tasks.push(newTask);
      this.newTaskTitle = '';
    }
  }

  // 削除
  deleteTask(id: number) {
    this.tasks = this.tasks.filter(task => task.id !== id);
  }

  // 更新
  toggleTask(id: number) {
    const task = this.tasks.find(t => t.id === id);
    if (task) {
      task.completed = !task.completed;
    }
  }

  // 検索
  getTasksByPriority(priority: Task['priority']): Task[] {
    return this.tasks.filter(task => task.priority === priority);
  }

  // 統計
  get completedCount(): number {
    return this.tasks.filter(t => t.completed).length;
  }

  get totalCount(): number {
    return this.tasks.length;
  }

  // ユーティリティ
  private getNextId(): number {
    return this.tasks.length > 0
      ? Math.max(...this.tasks.map(t => t.id)) + 1
      : 1;
  }
}
```

### フォーム処理
```typescript
import { Component } from '@angular/core';

interface ContactForm {
  name: string;
  email: string;
  message: string;
}

@Component({
  selector: 'app-contact-form',
  standalone: true,
  templateUrl: './contact-form.component.html'
})
export class ContactFormComponent {
  // フォームデータ
  formData: ContactForm = {
    name: '',
    email: '',
    message: ''
  };

  // 状態管理
  isSubmitting = false;
  isSubmitted = false;
  errorMessage = '';

  // バリデーション
  isFormValid(): boolean {
    return this.formData.name.trim() !== '' &&
           this.formData.email.includes('@') &&
           this.formData.message.trim() !== '';
  }

  // 送信処理
  async onSubmit() {
    if (!this.isFormValid()) {
      this.errorMessage = 'Please fill in all fields correctly';
      return;
    }

    this.isSubmitting = true;
    this.errorMessage = '';

    try {
      // API呼び出しのシミュレーション
      await this.submitForm(this.formData);
      this.isSubmitted = true;
      this.resetForm();
    } catch (error) {
      this.errorMessage = 'Failed to submit form';
    } finally {
      this.isSubmitting = false;
    }
  }

  // フォームリセット
  resetForm() {
    this.formData = {
      name: '',
      email: '',
      message: ''
    };
  }

  // API呼び出し（モック）
  private submitForm(data: ContactForm): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log('Form submitted:', data);
        resolve();
      }, 1000);
    });
  }
}
```

### 状態管理とロジック
```typescript
import { Component } from '@angular/core';

enum LoadingState {
  Idle = 'idle',
  Loading = 'loading',
  Success = 'success',
  Error = 'error'
}

interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}

@Component({
  selector: 'app-data-fetcher',
  standalone: true,
  template: `
    <div>
      @switch (loadingState) {
        @case ('loading') {
          <p>Loading...</p>
        }
        @case ('success') {
          <p>Data: {{data}}</p>
        }
        @case ('error') {
          <p>Error: {{error}}</p>
        }
        @default {
          <button (click)="fetchData()">Fetch Data</button>
        }
      }
    </div>
  `
})
export class DataFetcherComponent {
  loadingState: LoadingState = LoadingState.Idle;
  data: string | null = null;
  error: string | null = null;

  async fetchData() {
    this.loadingState = LoadingState.Loading;

    try {
      const response = await this.apiCall();
      if (response.data) {
        this.data = response.data;
        this.loadingState = LoadingState.Success;
      } else {
        this.error = response.error;
        this.loadingState = LoadingState.Error;
      }
    } catch (err) {
      this.error = 'Unexpected error occurred';
      this.loadingState = LoadingState.Error;
    }
  }

  private async apiCall(): Promise<ApiResponse<string>> {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({ data: 'Hello from API', error: null });
      }, 1000);
    });
  }

  reset() {
    this.loadingState = LoadingState.Idle;
    this.data = null;
    this.error = null;
  }
}
```

### readonly と const の使用
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-config',
  standalone: true,
  template: `
    <div>
      <p>App Version: {{APP_VERSION}}</p>
      <p>Max Users: {{MAX_USERS}}</p>
      <p>Config: {{config.apiUrl}}</p>
    </div>
  `
})
export class ConfigComponent {
  // 定数（変更不可）
  readonly APP_VERSION = '1.0.0';
  readonly MAX_USERS = 100;

  // 読み取り専用オブジェクト
  readonly config = {
    apiUrl: 'https://api.example.com',
    timeout: 5000
  } as const;

  // readonly配列
  readonly allowedRoles: readonly string[] = ['admin', 'user', 'guest'];

  // ❌ コンパイルエラー
  // updateVersion() {
  //   this.APP_VERSION = '2.0.0';  // エラー: 読み取り専用
  // }

  // ✅ 正しい方法: 新しいインスタンスを作成
  getUpdatedConfig(newUrl: string) {
    return {
      ...this.config,
      apiUrl: newUrl
    };
  }
}
```

## ベストプラクティス

1. **型定義を活用**: TypeScriptの型システムで安全性向上
2. **単一責任の原則**: 1つのクラスは1つの責務のみ
3. **プライベートメンバーの活用**: カプセル化の徹底
4. **ゲッター/セッターの使用**: 計算プロパティとバリデーション

## 注意点

- パブリックプロパティのみテンプレートで使用可能
- メソッド名は明確で分かりやすく
- 複雑なロジックはサービスに分離
- 適切な型定義でバグを防ぐ

## 関連技術
- TypeScript Classes
- Object-Oriented Programming
- Type Safety
- Encapsulation
