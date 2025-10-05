# #059 テンプレート構文のデバッグ

## 概要
Angular v20におけるテンプレート構文のデバッグ手法を学びます。Angular DevTools、コンソールログ、テンプレート内での値表示などを活用して、効率的に問題を特定し解決する方法を解説します。

## 学習目標
- テンプレート構文のデバッグ手法を理解する
- Angular DevToolsの活用方法を習得する
- 効率的な問題解決方法を身につける

## 📺 画面表示用コード

```html
<!-- デバッグ用の値表示 -->
<p>デバッグ: {{userName}}</p>
<p>配列: {{items | json}}</p>
<p>オブジェクト: {{user | json}}</p>
```

```typescript
// コンポーネントでのデバッグ
export class DebugComponent {
  userName = signal('');
  items = signal([1, 2, 3]);
  
  onInit() {
    console.log('初期値:', this.userName());
    console.log('配列:', this.items());
  }
  
  onValueChange() {
    console.log('値が変更されました:', this.userName());
  }
}
```

```html
<!-- 条件付きデバッグ表示 -->
@if (isDebugMode()) {
  <div class="debug-info">
    <p>ユーザー: {{userName()}}</p>
    <p>ステータス: {{status()}}</p>
  </div>
}
```

## 技術ポイント

### 1. デバッグ用の値表示
```html
<!-- デバッグ用の値表示 -->
<p>デバッグ: {{userName}}</p>
<p>配列: {{items | json}}</p>
<p>オブジェクト: {{user | json}}</p>
```

### 2. コンポーネントでのデバッグ
```typescript
export class DebugComponent {
  userName = signal('');
  items = signal([1, 2, 3]);
  
  onInit() {
    console.log('初期値:', this.userName());
    console.log('配列:', this.items());
  }
  
  onValueChange() {
    console.log('値が変更されました:', this.userName());
  }
}
```

### 3. 条件付きデバッグ表示
```html
@if (isDebugMode()) {
  <div class="debug-info">
    <p>ユーザー: {{userName()}}</p>
    <p>ステータス: {{status()}}</p>
  </div>
}
```

## 実践的な活用例

### 1. 包括的なデバッグコンポーネント
```typescript
export class ComprehensiveDebugComponent {
  // デバッグモードの制御
  isDebugMode = signal(false);
  
  // デバッグ対象のデータ
  user = signal({
    name: '太郎',
    email: 'taro@example.com',
    age: 25,
    preferences: {
      theme: 'dark',
      language: 'ja'
    }
  });
  
  formData = signal({
    firstName: '',
    lastName: '',
    email: ''
  });
  
  // デバッグ情報の計算
  debugInfo = computed(() => {
    return {
      user: this.user(),
      formData: this.formData(),
      timestamp: new Date().toISOString(),
      userAgent: navigator.userAgent
    };
  });
  
  // デバッグ用のメソッド
  logDebugInfo() {
    console.group('🔍 デバッグ情報');
    console.log('ユーザー情報:', this.user());
    console.log('フォームデータ:', this.formData());
    console.log('デバッグ情報:', this.debugInfo());
    console.groupEnd();
  }
  
  toggleDebugMode() {
    this.isDebugMode.update(mode => !mode);
    if (this.isDebugMode()) {
      this.logDebugInfo();
    }
  }
  
  // 値の変更を監視
  onUserChange() {
    console.log('ユーザー情報が変更されました:', this.user());
  }
  
  onFormChange() {
    console.log('フォームデータが変更されました:', this.formData());
  }
}
```

```html
<div class="debug-container">
  <!-- デバッグモード切り替え -->
  <button (click)="toggleDebugMode()">
    {{isDebugMode() ? 'デバッグモード OFF' : 'デバッグモード ON'}}
  </button>
  
  <!-- メインコンテンツ -->
  <div class="main-content">
    <h2>ユーザー情報</h2>
    <p>名前: {{user().name}}</p>
    <p>メール: {{user().email}}</p>
    <p>年齢: {{user().age}}</p>
    
    <h3>フォーム</h3>
    <input [(ngModel)]="formData.firstName" placeholder="名前">
    <input [(ngModel)]="formData.lastName" placeholder="姓">
    <input [(ngModel)]="formData.email" placeholder="メール">
  </div>
  
  <!-- デバッグ情報表示 -->
  @if (isDebugMode()) {
    <div class="debug-panel">
      <h3>🔍 デバッグ情報</h3>
      
      <div class="debug-section">
        <h4>現在の値</h4>
        <pre>{{debugInfo() | json}}</pre>
      </div>
      
      <div class="debug-section">
        <h4>ユーザー情報</h4>
        <pre>{{user() | json}}</pre>
      </div>
      
      <div class="debug-section">
        <h4>フォームデータ</h4>
        <pre>{{formData() | json}}</pre>
      </div>
      
      <div class="debug-section">
        <h4>Signal状態</h4>
        <p>ユーザーSignal: {{user()}}</p>
        <p>フォームSignal: {{formData()}}</p>
        <p>デバッグモードSignal: {{isDebugMode()}}</p>
      </div>
    </div>
  }
</div>
```

### 2. フォームバリデーションのデバッグ
```typescript
export class FormValidationDebugComponent {
  formData = signal({
    name: '',
    email: '',
    age: 0
  });
  
  validationErrors = signal<Record<string, string>>({});
  
  // バリデーション結果のデバッグ
  debugValidation = computed(() => {
    const data = this.formData();
    const errors = this.validationErrors();
    
    return {
      formData: data,
      validationErrors: errors,
      hasErrors: Object.keys(errors).length > 0,
      errorCount: Object.keys(errors).length,
      isValid: Object.keys(errors).length === 0
    };
  });
  
  validateForm() {
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
    
    // デバッグログ
    console.log('バリデーション実行:', {
      formData: data,
      errors: errors,
      isValid: Object.keys(errors).length === 0
    });
  }
  
  private isValidEmail(email: string): boolean {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
  
  onFieldChange(field: string, value: any) {
    this.formData.update(data => ({
      ...data,
      [field]: value
    }));
    
    // フィールド変更時のデバッグログ
    console.log(`フィールド変更: ${field} = ${value}`);
  }
}
```

```html
<div class="form-debug-container">
  <h2>フォームバリデーション デバッグ</h2>
  
  <form>
    <div class="field">
      <label>名前</label>
      <input 
        [value]="formData().name"
        (input)="onFieldChange('name', $event.target.value)"
        (blur)="validateForm()">
      @if (validationErrors()['name']) {
        <span class="error">{{validationErrors()['name']}}</span>
      }
    </div>
    
    <div class="field">
      <label>メールアドレス</label>
      <input 
        [value]="formData().email"
        (input)="onFieldChange('email', $event.target.value)"
        (blur)="validateForm()">
      @if (validationErrors()['email']) {
        <span class="error">{{validationErrors()['email']}}</span>
      }
    </div>
    
    <div class="field">
      <label>年齢</label>
      <input 
        type="number"
        [value]="formData().age"
        (input)="onFieldChange('age', +$event.target.value)"
        (blur)="validateForm()">
      @if (validationErrors()['age']) {
        <span class="error">{{validationErrors()['age']}}</span>
      }
    </div>
    
    <button type="button" (click)="validateForm()">バリデーション実行</button>
  </form>
  
  <!-- デバッグ情報表示 -->
  <div class="debug-panel">
    <h3>🔍 バリデーションデバッグ</h3>
    <pre>{{debugValidation() | json}}</pre>
    
    <div class="debug-stats">
      <p>エラー数: {{debugValidation().errorCount}}</p>
      <p>フォーム有効性: {{debugValidation().isValid ? '有効' : '無効'}}</p>
      <p>エラー有無: {{debugValidation().hasErrors ? 'あり' : 'なし'}}</p>
    </div>
  </div>
</div>
```

### 3. パフォーマンスデバッグ
```typescript
export class PerformanceDebugComponent {
  items = signal<Item[]>([]);
  filter = signal('');
  sortBy = signal<'name' | 'date'>('name');
  
  // パフォーマンス測定用
  private performanceMarks = new Map<string, number>();
  
  // フィルタリング処理のパフォーマンス測定
  filteredItems = computed(() => {
    this.startPerformanceMark('filtering');
    
    const items = this.items();
    const filter = this.filter();
    const sortBy = this.sortBy();
    
    let filtered = items;
    if (filter) {
      filtered = items.filter(item => 
        item.name.toLowerCase().includes(filter.toLowerCase())
      );
    }
    
    const sorted = filtered.sort((a, b) => {
      if (sortBy === 'name') {
        return a.name.localeCompare(b.name);
      } else {
        return new Date(b.date).getTime() - new Date(a.date).getTime();
      }
    });
    
    this.endPerformanceMark('filtering');
    return sorted;
  });
  
  private startPerformanceMark(name: string) {
    this.performanceMarks.set(name, performance.now());
  }
  
  private endPerformanceMark(name: string) {
    const startTime = this.performanceMarks.get(name);
    if (startTime) {
      const duration = performance.now() - startTime;
      console.log(`⏱️ ${name}処理時間: ${duration.toFixed(2)}ms`);
    }
  }
  
  // 大量データの生成（デバッグ用）
  generateTestData(count: number) {
    this.startPerformanceMark('data-generation');
    
    const items: Item[] = [];
    for (let i = 0; i < count; i++) {
      items.push({
        id: i,
        name: `アイテム${i}`,
        date: new Date(Date.now() - Math.random() * 10000000000),
        description: `これはアイテム${i}の説明です`
      });
    }
    
    this.items.set(items);
    this.endPerformanceMark('data-generation');
  }
  
  // パフォーマンス統計
  performanceStats = computed(() => {
    const items = this.items();
    const filtered = this.filteredItems();
    
    return {
      totalItems: items.length,
      filteredItems: filtered.length,
      filterRatio: items.length > 0 ? (filtered.length / items.length) * 100 : 0,
      memoryUsage: (performance as any).memory?.usedJSHeapSize || 'N/A'
    };
  });
}
```

```html
<div class="performance-debug-container">
  <h2>パフォーマンスデバッグ</h2>
  
  <div class="controls">
    <button (click)="generateTestData(1000)">1000件生成</button>
    <button (click)="generateTestData(10000)">10000件生成</button>
    <button (click)="generateTestData(100000)">100000件生成</button>
    
    <input [(ngModel)]="filter" placeholder="フィルター">
    <select [(ngModel)]="sortBy">
      <option value="name">名前順</option>
      <option value="date">日付順</option>
    </select>
  </div>
  
  <!-- パフォーマンス統計 -->
  <div class="performance-stats">
    <h3>📊 パフォーマンス統計</h3>
    <p>総アイテム数: {{performanceStats().totalItems}}</p>
    <p>フィルター後: {{performanceStats().filteredItems}}</p>
    <p>フィルター率: {{performanceStats().filterRatio.toFixed(1)}}%</p>
    <p>メモリ使用量: {{performanceStats().memoryUsage}}</p>
  </div>
  
  <!-- アイテム表示 -->
  <div class="items-container">
    @for (item of filteredItems(); track item.id) {
      <div class="item">
        <h4>{{item.name}}</h4>
        <p>{{item.description}}</p>
        <small>{{item.date | date}}</small>
      </div>
    }
  </div>
</div>
```

### 4. ルーティングデバッグ
```typescript
export class RoutingDebugComponent {
  private router = inject(Router);
  private activatedRoute = inject(ActivatedRoute);
  
  // ルーティング情報のデバッグ
  routingInfo = computed(() => {
    return {
      currentUrl: this.router.url,
      currentRoute: this.activatedRoute.snapshot.routeConfig?.path,
      queryParams: this.activatedRoute.snapshot.queryParams,
      params: this.activatedRoute.snapshot.params,
      fragment: this.activatedRoute.snapshot.fragment
    };
  });
  
  ngOnInit() {
    // ルート変更の監視
    this.router.events.subscribe(event => {
      if (event instanceof NavigationStart) {
        console.log('🚀 ナビゲーション開始:', event.url);
      } else if (event instanceof NavigationEnd) {
        console.log('✅ ナビゲーション完了:', event.url);
      } else if (event instanceof NavigationError) {
        console.error('❌ ナビゲーションエラー:', event.error);
      }
    });
  }
}
```

## Angular DevToolsの活用

### 1. コンポーネントツリーの確認
```typescript
export class DevToolsComponent {
  // DevToolsで確認しやすいように名前を設定
  componentName = 'DevToolsComponent';
  
  // 状態の可視化
  state = signal({
    counter: 0,
    user: { name: '太郎', age: 25 },
    items: ['アイテム1', 'アイテム2']
  });
}
```

### 2. パフォーマンスプロファイリング
```typescript
export class ProfilingComponent {
  // パフォーマンス測定用のメソッド
  measurePerformance(name: string, fn: () => void) {
    const start = performance.now();
    fn();
    const end = performance.now();
    console.log(`⏱️ ${name}: ${(end - start).toFixed(2)}ms`);
  }
  
  // 重い処理の測定
  heavyOperation() {
    this.measurePerformance('重い処理', () => {
      let result = 0;
      for (let i = 0; i < 1000000; i++) {
        result += Math.random();
      }
      return result;
    });
  }
}
```

## ベストプラクティス

1. **段階的なデバッグ**: 問題を段階的に絞り込む
2. **適切なログレベル**: 本番環境では不要なログを出力しない
3. **デバッグモードの制御**: 環境変数でデバッグモードを制御
4. **パフォーマンス監視**: 継続的なパフォーマンス監視

## 注意点

- 本番環境でのデバッグ情報の漏洩に注意
- パフォーマンスへの影響を考慮
- セキュリティ情報の出力を避ける
- 適切なログレベル設定

## 関連技術
- Angular DevTools
- ブラウザ開発者ツール
- コンソールログ
- パフォーマンス測定
- デバッグ手法
