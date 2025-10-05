# #057 テンプレート式でのメソッド呼び出し注意点

## 概要
Angular v20におけるテンプレート式でのメソッド呼び出しの注意点を学びます。パフォーマンスへの影響、変更検知の仕組み、そして適切な代替手段について解説します。

## 学習目標
- テンプレートでのメソッド呼び出しの問題点を理解する
- パフォーマンスへの影響を把握する
- 適切な代替手段を習得する

## 📺 画面表示用コード

```html
<!-- 注意が必要：メソッド呼び出し -->
<p>{{getExpensiveValue()}}</p> <!-- 毎回実行される -->
```

```typescript
// 問題のある実装
export class MyComponent {
  getExpensiveValue() {
    console.log('メソッドが実行されました'); // 毎回出力される
    return Math.random(); // 重い処理
  }
}
```

```typescript
// 推奨：computedを使用
import { computed, signal } from '@angular/core';

export class MyComponent {
  private data = signal(0);
  
  expensiveValue = computed(() => {
    console.log('computedが実行されました'); // 依存が変わった時のみ
    return this.data() * 1000;
  });
}
```

```html
<!-- 改善後：computedを使用 -->
<p>{{expensiveValue()}}</p>
```

## 技術ポイント

### 1. 問題のある実装：メソッド呼び出し
```typescript
export class ProblematicComponent {
  getExpensiveValue() {
    console.log('メソッドが実行されました'); // 毎回出力される
    return Math.random(); // 重い処理
  }
}
```

```html
<!-- 注意が必要：メソッド呼び出し -->
<p>{{getExpensiveValue()}}</p> <!-- 毎回実行される -->
```

### 2. 推奨：computedを使用
```typescript
import { computed, signal } from '@angular/core';

export class OptimizedComponent {
  private data = signal(0);
  
  expensiveValue = computed(() => {
    console.log('computedが実行されました'); // 依存が変わった時のみ
    return this.data() * 1000;
  });
}
```

```html
<!-- 改善後：computedを使用 -->
<p>{{expensiveValue()}}</p>
```

## 実践的な活用例

### 1. フィルタリング処理の最適化
```typescript
export class FilteringComponent {
  items = signal([
    { id: 1, name: 'アイテム1', category: 'A', active: true },
    { id: 2, name: 'アイテム2', category: 'B', active: false },
    { id: 3, name: 'アイテム3', category: 'A', active: true }
  ]);
  
  filterCategory = signal('A');
  
  // 問題のある実装
  getFilteredItems() {
    console.log('フィルタリング実行'); // 毎回実行される
    return this.items().filter(item => 
      item.category === this.filterCategory() && item.active
    );
  }
  
  // 推奨実装：computedを使用
  filteredItems = computed(() => {
    console.log('computedフィルタリング実行'); // 依存が変わった時のみ
    return this.items().filter(item => 
      item.category === this.filterCategory() && item.active
    );
  });
}
```

```html
<!-- 問題のある実装 -->
<div *ngFor="let item of getFilteredItems()">
  {{item.name}}
</div>

<!-- 推奨実装 -->
@for (item of filteredItems(); track item.id) {
  <div>{{item.name}}</div>
}
```

### 2. 計算処理の最適化
```typescript
export class CalculationComponent {
  numbers = signal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
  multiplier = signal(2);
  
  // 問題のある実装
  calculateSum() {
    console.log('合計計算実行'); // 毎回実行される
    return this.numbers().reduce((sum, num) => sum + num, 0);
  }
  
  calculateProduct() {
    console.log('積計算実行'); // 毎回実行される
    return this.numbers().reduce((product, num) => product * num, 1);
  }
  
  // 推奨実装：computedを使用
  sum = computed(() => {
    console.log('computed合計計算実行'); // 依存が変わった時のみ
    return this.numbers().reduce((sum, num) => sum + num, 0);
  });
  
  product = computed(() => {
    console.log('computed積計算実行'); // 依存が変わった時のみ
    return this.numbers().reduce((product, num) => product * num, 1);
  });
  
  multipliedSum = computed(() => {
    return this.sum() * this.multiplier();
  });
}
```

```html
<!-- 問題のある実装 -->
<p>合計: {{calculateSum()}}</p>
<p>積: {{calculateProduct()}}</p>

<!-- 推奨実装 -->
<p>合計: {{sum()}}</p>
<p>積: {{product()}}</p>
<p>合計×{{multiplier()}}: {{multipliedSum()}}</p>
```

### 3. フォーマット処理の最適化
```typescript
export class FormattingComponent {
  user = signal({
    firstName: '太郎',
    lastName: '田中',
    birthDate: new Date('1990-01-01'),
    salary: 5000000
  });
  
  // 問題のある実装
  getFullName() {
    console.log('名前フォーマット実行'); // 毎回実行される
    return `${this.user().firstName} ${this.user().lastName}`;
  }
  
  getFormattedBirthDate() {
    console.log('日付フォーマット実行'); // 毎回実行される
    return this.user().birthDate.toLocaleDateString('ja-JP');
  }
  
  getFormattedSalary() {
    console.log('給与フォーマット実行'); // 毎回実行される
    return new Intl.NumberFormat('ja-JP', {
      style: 'currency',
      currency: 'JPY'
    }).format(this.user().salary);
  }
  
  // 推奨実装：computedを使用
  fullName = computed(() => {
    console.log('computed名前フォーマット実行'); // 依存が変わった時のみ
    return `${this.user().firstName} ${this.user().lastName}`;
  });
  
  formattedBirthDate = computed(() => {
    console.log('computed日付フォーマット実行'); // 依存が変わった時のみ
    return this.user().birthDate.toLocaleDateString('ja-JP');
  });
  
  formattedSalary = computed(() => {
    console.log('computed給与フォーマット実行'); // 依存が変わった時のみ
    return new Intl.NumberFormat('ja-JP', {
      style: 'currency',
      currency: 'JPY'
    }).format(this.user().salary);
  });
}
```

```html
<!-- 問題のある実装 -->
<h2>{{getFullName()}}</h2>
<p>生年月日: {{getFormattedBirthDate()}}</p>
<p>給与: {{getFormattedSalary()}}</p>

<!-- 推奨実装 -->
<h2>{{fullName()}}</h2>
<p>生年月日: {{formattedBirthDate()}}</p>
<p>給与: {{formattedSalary()}}</p>
```

### 4. 条件付き表示の最適化
```typescript
export class ConditionalComponent {
  user = signal<User | null>(null);
  permissions = signal<string[]>([]);
  feature = signal('dashboard');
  
  // 問題のある実装
  hasPermission() {
    console.log('権限チェック実行'); // 毎回実行される
    const user = this.user();
    const userPermissions = this.permissions();
    return user && userPermissions.includes(this.feature());
  }
  
  getUserRole() {
    console.log('ロール取得実行'); // 毎回実行される
    const user = this.user();
    return user ? user.role : 'guest';
  }
  
  // 推奨実装：computedを使用
  hasPermission = computed(() => {
    console.log('computed権限チェック実行'); // 依存が変わった時のみ
    const user = this.user();
    const userPermissions = this.permissions();
    return user && userPermissions.includes(this.feature());
  });
  
  userRole = computed(() => {
    console.log('computedロール取得実行'); // 依存が変わった時のみ
    const user = this.user();
    return user ? user.role : 'guest';
  });
  
  canAccess = computed(() => {
    return this.hasPermission() && this.userRole() !== 'guest';
  });
}
```

```html
<!-- 問題のある実装 -->
@if (hasPermission()) {
  <div>アクセス可能</div>
}

<!-- 推奨実装 -->
@if (canAccess()) {
  <div>アクセス可能</div>
}
```

## パフォーマンス比較

### 1. メソッド呼び出しの問題
```typescript
export class PerformanceTestComponent {
  counter = signal(0);
  
  // 問題のある実装
  getExpensiveValue() {
    console.log('メソッド実行:', Date.now());
    // 重い処理をシミュレート
    let result = 0;
    for (let i = 0; i < 1000000; i++) {
      result += Math.random();
    }
    return result;
  }
  
  // 推奨実装
  expensiveValue = computed(() => {
    console.log('computed実行:', Date.now());
    let result = 0;
    for (let i = 0; i < 1000000; i++) {
      result += Math.random();
    }
    return result;
  });
  
  increment() {
    this.counter.update(c => c + 1);
  }
}
```

### 2. 測定結果の例
```html
<!-- メソッド呼び出し：counterが変更されるたびに実行される -->
<p>カウンター: {{counter()}}</p>
<p>重い計算: {{getExpensiveValue()}}</p>

<!-- computed：counterが変更されても実行されない -->
<p>カウンター: {{counter()}}</p>
<p>重い計算: {{expensiveValue()}}</p>
```

## ベストプラクティス

1. **computedの活用**: 重い計算や複雑な処理はcomputedを使用
2. **依存関係の明確化**: computedの依存関係を明確にする
3. **メソッド呼び出しの最小化**: テンプレートでのメソッド呼び出しを最小限に
4. **パフォーマンス測定**: 実際のパフォーマンスを測定して検証

## 注意点

- メソッド呼び出しは変更検知のたびに実行される
- computedは依存が変わった時のみ実行される
- 重い処理は特に注意が必要
- Angular v20のSignalベースのcomputedが最適

## 関連技術
- Angular v20のSignal
- computed
- パフォーマンス最適化
- 変更検知
- テンプレート式
