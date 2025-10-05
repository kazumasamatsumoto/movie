# #010 「TypeScript で Component を書く」台本

四国めたん「TypeScript で Component を書くについて解説します！」
ずんだもん「TypeScriptを使うメリットは？」
四国めたん「型安全性、IDEの補完、リファクタリングの安全性が向上します」
ずんだもん「どんな型定義があるの？」
四国めたん「プリミティブ型、オブジェクト型、配列型、関数型などがあります」
ずんだもん「型定義は必須なの？」
四国めたん「必須ではありませんが、型安全性のため推奨されています」

---

## 📺 画面表示用コード

// 基本的な型定義
```typescript
import { Component } from '@angular/core';

interface User {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
}

@Component({
  selector: 'app-typescript',
  template: `
    <div>
      <h1>{{title}}</h1>
      <p>ユーザー数: {{userCount}}</p>
      <p>アクティブ: {{isActive}}</p>
    </div>
  `
})
export class TypeScriptComponent {
  // プリミティブ型
  title: string = 'TypeScript Component';
  userCount: number = 0;
  isActive: boolean = true;
  
  // 配列型
  users: User[] = [];
  
  // オブジェクト型
  currentUser: User | null = null;
}
```

// インターフェースの定義
```typescript
interface Product {
  id: number;
  name: string;
  price: number;
  category: string;
  inStock: boolean;
}

interface CartItem {
  product: Product;
  quantity: number;
}

@Component({
  selector: 'app-interfaces',
  template: `
    <div>
      <h2>商品管理</h2>
      <div *ngFor="let product of products">
        <h3>{{product.name}}</h3>
        <p>価格: ¥{{product.price}}</p>
        <p>在庫: {{product.inStock ? 'あり' : 'なし'}}</p>
      </div>
    </div>
  `
})
export class InterfacesComponent {
  products: Product[] = [
    {
      id: 1,
      name: 'ノートパソコン',
      price: 80000,
      category: 'PC',
      inStock: true
    },
    {
      id: 2,
      name: 'マウス',
      price: 3000,
      category: 'アクセサリ',
      inStock: false
    }
  ];
  
  cart: CartItem[] = [];
}
```

// 型エイリアス
```typescript
type Status = 'loading' | 'success' | 'error';
type Theme = 'light' | 'dark';

@Component({
  selector: 'app-type-aliases',
  template: `
    <div [class]="theme">
      <h2>ステータス: {{status}}</h2>
      <p>テーマ: {{theme}}</p>
    </div>
  `
})
export class TypeAliasesComponent {
  status: Status = 'loading';
  theme: Theme = 'light';
  
  setStatus(newStatus: Status) {
    this.status = newStatus;
  }
  
  toggleTheme() {
    this.theme = this.theme === 'light' ? 'dark' : 'light';
  }
}
```

// ジェネリクス
```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

@Component({
  selector: 'app-generics',
  template: `
    <div>
      <h2>API レスポンス</h2>
      <p>ステータス: {{response.status}}</p>
      <p>メッセージ: {{response.message}}</p>
      <p>データ: {{response.data}}</p>
    </div>
  `
})
export class GenericsComponent {
  response: ApiResponse<string> = {
    data: 'サンプルデータ',
    status: 200,
    message: '成功'
  };
  
  // ジェネリックメソッド
  processData<T>(data: T): T {
    return data;
  }
}
```

// オプショナルプロパティ
```typescript
interface UserProfile {
  id: number;
  name: string;
  email: string;
  avatar?: string;  // オプショナル
  bio?: string;     // オプショナル
}

@Component({
  selector: 'app-optional',
  template: `
    <div>
      <h2>ユーザープロフィール</h2>
      <h3>{{profile.name}}</h3>
      <p>{{profile.email}}</p>
      <img *ngIf="profile.avatar" [src]="profile.avatar" alt="アバター">
      <p *ngIf="profile.bio">{{profile.bio}}</p>
    </div>
  `
})
export class OptionalComponent {
  profile: UserProfile = {
    id: 1,
    name: '田中太郎',
    email: 'tanaka@example.com'
    // avatar と bio は省略可能
  };
}
```

// 型ガード
```typescript
function isString(value: any): value is string {
  return typeof value === 'string';
}

function isNumber(value: any): value is number {
  return typeof value === 'number';
}

@Component({
  selector: 'app-type-guards',
  template: `
    <div>
      <h2>型ガード</h2>
      <p>値: {{displayValue}}</p>
      <p>型: {{valueType}}</p>
    </div>
  `
})
export class TypeGuardsComponent {
  value: string | number = 'Hello';
  
  get displayValue(): string {
    if (isString(this.value)) {
      return this.value.toUpperCase();
    } else if (isNumber(this.value)) {
      return this.value.toString();
    }
    return 'Unknown';
  }
  
  get valueType(): string {
    if (isString(this.value)) {
      return '文字列';
    } else if (isNumber(this.value)) {
      return '数値';
    }
    return '不明';
  }
}
```

// 型安全性の例
```typescript
@Component({
  selector: 'app-type-safety',
  template: `
    <div>
      <h2>型安全性</h2>
      <button (click)="addUser()">ユーザー追加</button>
      <button (click)="calculateAge()">年齢計算</button>
    </div>
  `
})
export class TypeSafetyComponent {
  users: User[] = [];
  
  // 型安全なメソッド
  addUser(): void {
    const newUser: User = {
      id: this.users.length + 1,
      name: '新しいユーザー',
      email: 'new@example.com',
      isActive: true
    };
    this.users.push(newUser);
  }
  
  // 型安全な計算
  calculateAge(birthYear: number): number {
    const currentYear = new Date().getFullYear();
    return currentYear - birthYear;
  }
  
  // 型エラーの例（コメントアウト）
  // addUser(): string {  // ❌ 戻り値の型が違う
  //   return 'ユーザー追加';
  // }
  
  // calculateAge(birthYear: string): number {  // ❌ 引数の型が違う
  //   return 2024 - birthYear;
  // }
}
```
