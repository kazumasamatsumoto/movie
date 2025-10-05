# #056 テンプレート式の制約事項

## 概要
Angular v20におけるテンプレート式の制約事項を学びます。セキュリティとパフォーマンスを考慮して、JavaScriptの一部構文が制限されている理由と、適切な代替手段について解説します。

## 学習目標
- テンプレート式の制約事項を理解する
- 使用できない構文とその理由を把握する
- 適切な代替手段を習得する

## 📺 画面表示用コード

```html
<!-- 使用可能：基本的な演算とメソッド呼び出し -->
<p>{{user.name}}</p>
<p>{{price * 1.1}}</p>
<p>{{getFullName()}}</p>
```

```html
<!-- 使用不可：new演算子 -->
<p>{{new Date()}}</p> <!-- エラー！ -->
```

```html
<!-- 使用不可：代入演算子 -->
<p>{{count++}}</p> <!-- エラー！ -->
<p>{{name = '新しい名前'}}</p> <!-- エラー！ -->
```

```typescript
// コンポーネントで適切に処理
export class MyComponent {
  name = '初期値';
  
  getCurrentDate() {
    return new Date(); // コンポーネント内では可能
  }
}
```

## 技術ポイント

### 1. 使用可能：基本的な演算とメソッド呼び出し
```html
<p>{{user.name}}</p>
<p>{{price * 1.1}}</p>
<p>{{getFullName()}}</p>
<p>{{items.length}}</p>
<p>{{isActive ? 'アクティブ' : '非アクティブ'}}</p>
```

### 2. 使用不可：new演算子
```html
<!-- エラー！ -->
<p>{{new Date()}}</p>
<p>{{new Array(10)}}</p>
<p>{{new Object()}}</p>
```

### 3. 使用不可：代入演算子
```html
<!-- エラー！ -->
<p>{{count++}}</p>
<p>{{name = '新しい名前'}}</p>
<p>{{items.push(newItem)}}</p>
```

### 4. 使用不可：インクリメント・デクリメント
```html
<!-- エラー！ -->
<p>{{++count}}</p>
<p>{{count--}}</p>
```

## 実践的な活用例

### 1. 日付の表示（コンポーネントで処理）
```typescript
export class DateComponent {
  currentDate = new Date();
  
  get formattedDate() {
    return this.currentDate.toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }
  
  get timeAgo() {
    const now = new Date();
    const diff = now.getTime() - this.currentDate.getTime();
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    return `${days}日前`;
  }
}
```

```html
<p>現在の日付: {{formattedDate}}</p>
<p>経過時間: {{timeAgo}}</p>
```

### 2. 配列操作（コンポーネントで処理）
```typescript
export class ArrayComponent {
  items = signal(['アイテム1', 'アイテム2', 'アイテム3']);
  newItem = signal('');
  
  addItem() {
    if (this.newItem().trim()) {
      this.items.update(items => [...items, this.newItem()]);
      this.newItem.set('');
    }
  }
  
  removeItem(index: number) {
    this.items.update(items => items.filter((_, i) => i !== index));
  }
  
  get sortedItems() {
    return [...this.items()].sort();
  }
}
```

```html
<div>
  <input [(ngModel)]="newItem" placeholder="新しいアイテム">
  <button (click)="addItem()">追加</button>
</div>

@for (item of sortedItems; track item; let i = $index) {
  <div>
    {{item}}
    <button (click)="removeItem(i)">削除</button>
  </div>
}
```

### 3. 計算処理（computedを使用）
```typescript
import { signal, computed } from '@angular/core';

export class CalculationComponent {
  private numbers = signal([1, 2, 3, 4, 5]);
  
  // テンプレートでは使用できない計算をcomputedで処理
  sum = computed(() => {
    return this.numbers().reduce((acc, num) => acc + num, 0);
  });
  
  average = computed(() => {
    return this.sum() / this.numbers().length;
  });
  
  max = computed(() => {
    return Math.max(...this.numbers());
  });
  
  min = computed(() => {
    return Math.min(...this.numbers());
  });
}
```

```html
<p>数値: {{numbers()}}</p>
<p>合計: {{sum()}}</p>
<p>平均: {{average()}}</p>
<p>最大値: {{max()}}</p>
<p>最小値: {{min()}}</p>
```

### 4. 条件付きオブジェクト作成
```typescript
export class ConditionalObjectComponent {
  user = signal({ name: '太郎', age: 25, isActive: true });
  
  get userInfo() {
    const user = this.user();
    return {
      displayName: user.name,
      ageGroup: user.age >= 18 ? '成人' : '未成年',
      status: user.isActive ? 'アクティブ' : '非アクティブ'
    };
  }
  
  get userSummary() {
    const info = this.userInfo;
    return `${info.displayName} (${info.ageGroup}, ${info.status})`;
  }
}
```

```html
<p>ユーザー情報: {{userSummary}}</p>
<p>表示名: {{userInfo.displayName}}</p>
<p>年齢区分: {{userInfo.ageGroup}}</p>
<p>ステータス: {{userInfo.status}}</p>
```

## 制約事項の詳細

### 1. セキュリティ上の制約
```html
<!-- 以下のような危険な操作は禁止 -->
<p>{{window.location.href}}</p>  <!-- グローバル変数アクセス -->
<p>{{document.cookie}}</p>       <!-- DOM操作 -->
<p>{{eval('malicious code')}}</p> <!-- コード実行 -->
```

### 2. パフォーマンス上の制約
```html
<!-- 以下のような重い操作は禁止 -->
<p>{{JSON.stringify(largeObject)}}</p>  <!-- 大量データ処理 -->
<p>{{heavyCalculation()}}</p>           <!-- 重い計算処理 -->
```

### 3. 副作用の制約
```html
<!-- 以下のような副作用のある操作は禁止 -->
<p>{{console.log('debug')}}</p>  <!-- コンソール出力 -->
<p>{{localStorage.setItem()}}</p> <!-- ストレージ操作 -->
<p>{{httpService.post()}}</p>    <!-- HTTP通信 -->
```

## 適切な代替手段

### 1. メソッドやgetterの活用
```typescript
export class AlternativeComponent {
  data = signal<any[]>([]);
  
  // テンプレートで使用できない処理をメソッドで実装
  processData() {
    return this.data()
      .filter(item => item.active)
      .map(item => ({ ...item, processed: true }))
      .sort((a, b) => a.priority - b.priority);
  }
  
  get processedData() {
    return this.processData();
  }
}
```

### 2. Pipeの活用
```typescript
@Pipe({ name: 'safeJson' })
export class SafeJsonPipe implements PipeTransform {
  transform(value: any): string {
    try {
      return JSON.stringify(value, null, 2);
    } catch (error) {
      return 'Invalid JSON';
    }
  }
}
```

### 3. コンポーネント内での処理
```typescript
export class ProcessingComponent {
  rawData = signal<any[]>([]);
  processedData = signal<any[]>([]);
  
  ngOnInit() {
    // 初期化時にデータを処理
    this.processData();
  }
  
  private processData() {
    const processed = this.rawData()
      .filter(item => item.valid)
      .map(item => this.transformItem(item));
    this.processedData.set(processed);
  }
  
  private transformItem(item: any) {
    return {
      ...item,
      displayName: `${item.firstName} ${item.lastName}`,
      formattedDate: new Date(item.createdAt).toLocaleDateString()
    };
  }
}
```

## ベストプラクティス

1. **制約を理解**: テンプレート式の制約を理解して適切に使用
2. **適切な分離**: 複雑な処理はコンポーネント側で実装
3. **パフォーマンス考慮**: 重い処理は避け、computedやgetterを活用
4. **型安全性**: TypeScriptの型定義を活用

## 注意点

- テンプレート式は表示に専念する
- セキュリティとパフォーマンスを考慮した制限
- 適切な代替手段を選択する
- Angular v20でも同じ制約が適用される

## 関連技術
- テンプレート式
- Angular v20のSignal
- computed
- Pipe
- セキュリティ
- パフォーマンス最適化
