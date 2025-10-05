# #032 「{{ }} 式の評価 - 計算とメソッド呼び出し」台本

四国めたん「{{ }} 式の評価 - 計算とメソッド呼び出しについて解説します！」
ずんだもん「式の評価って何ができるの？」
四国めたん「補間バインディング内で、計算式やメソッド呼び出しが実行できます」
ずんだもん「どんな計算ができるの？」
四国めたん「四則演算、比較演算、論理演算、三項演算子などが使えます」
ずんだもん「パフォーマンスは大丈夫なの？」
四国めたん「頻繁に呼ばれるので、重い処理は避け、単純な計算に留めることが推奨されます」

---

## 📺 画面表示用コード

// 四則演算の評価
```typescript
@Component({
  selector: 'app-arithmetic-expressions',
  standalone: true,
  template: `
    <div class="arithmetic-demo">
      <h2>四則演算の評価</h2>
      <p>足し算: 10 + 5 = {{10 + 5}}</p>
      <p>引き算: 10 - 5 = {{10 - 5}}</p>
      <p>掛け算: 10 * 5 = {{10 * 5}}</p>
      <p>割り算: 10 / 5 = {{10 / 5}}</p>
      <p>余り: 10 % 3 = {{10 % 3}}</p>
      <p>累乗: 2 ** 3 = {{2 ** 3}}</p>
      <p>複合計算: (10 + 5) * 2 = {{(10 + 5) * 2}}</p>
    </div>
  `,
  styles: [`
    .arithmetic-demo {
      padding: 20px;
      border: 1px solid #007bff;
      border-radius: 8px;
    }
    p {
      font-family: monospace;
      font-size: 16px;
      margin: 8px 0;
    }
  `]
})
export class ArithmeticExpressionsComponent {}
```

// プロパティを使った計算
```typescript
@Component({
  selector: 'app-property-calculation',
  standalone: true,
  template: `
    <div class="calculation-demo">
      <h2>プロパティを使った計算</h2>
      <p>価格: ¥{{price}}</p>
      <p>数量: {{quantity}}</p>
      <p>小計: ¥{{price * quantity}}</p>
      <p>消費税(10%): ¥{{Math.floor(price * quantity * 0.1)}}</p>
      <p>合計: ¥{{price * quantity + Math.floor(price * quantity * 0.1)}}</p>
      <button (click)="increaseQuantity()">数量+1</button>
      <button (click)="decreaseQuantity()">数量-1</button>
    </div>
  `,
  styles: [`
    .calculation-demo {
      padding: 20px;
      border: 1px solid #28a745;
      border-radius: 8px;
    }
    p {
      font-size: 18px;
      font-weight: bold;
      margin: 10px 0;
    }
    button {
      margin-right: 10px;
      padding: 8px 16px;
      background-color: #28a745;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  `]
})
export class PropertyCalculationComponent {
  price = 1000;
  quantity = 3;
  Math = Math;
  
  increaseQuantity(): void {
    this.quantity++;
  }
  
  decreaseQuantity(): void {
    if (this.quantity > 0) {
      this.quantity--;
    }
  }
}
```

// 比較演算子の評価
```typescript
@Component({
  selector: 'app-comparison-expressions',
  standalone: true,
  template: `
    <div class="comparison-demo">
      <h2>比較演算子の評価</h2>
      <p>年齢: {{age}}</p>
      <p>age > 20: {{age > 20}}</p>
      <p>age >= 18: {{age >= 18}}</p>
      <p>age < 30: {{age < 30}}</p>
      <p>age === 25: {{age === 25}}</p>
      <p>age !== 30: {{age !== 30}}</p>
      <button (click)="age = age + 1">年齢+1</button>
      <button (click)="age = age - 1">年齢-1</button>
    </div>
  `,
  styles: [`
    .comparison-demo {
      padding: 20px;
      border: 1px solid #ffc107;
      border-radius: 8px;
    }
  `]
})
export class ComparisonExpressionsComponent {
  age = 25;
}
```

// 論理演算子の評価
```typescript
@Component({
  selector: 'app-logical-expressions',
  standalone: true,
  template: `
    <div class="logical-demo">
      <h2>論理演算子の評価</h2>
      <p>isActive: {{isActive}}</p>
      <p>isPremium: {{isPremium}}</p>
      <p>AND演算: {{isActive && isPremium}}</p>
      <p>OR演算: {{isActive || isPremium}}</p>
      <p>NOT演算: {{!isActive}}</p>
      <p>複合論理: {{isActive && (isPremium || age > 18)}}</p>
      <button (click)="toggleActive()">Active切り替え</button>
      <button (click)="togglePremium()">Premium切り替え</button>
    </div>
  `,
  styles: [`
    .logical-demo {
      padding: 20px;
      border: 1px solid #dc3545;
      border-radius: 8px;
    }
  `]
})
export class LogicalExpressionsComponent {
  isActive = true;
  isPremium = false;
  age = 20;
  
  toggleActive(): void {
    this.isActive = !this.isActive;
  }
  
  togglePremium(): void {
    this.isPremium = !this.isPremium;
  }
}
```

// メソッド呼び出しの評価
```typescript
@Component({
  selector: 'app-method-calls',
  standalone: true,
  template: `
    <div class="method-demo">
      <h2>メソッド呼び出しの評価</h2>
      <p>現在時刻: {{getCurrentTime()}}</p>
      <p>挨拶: {{getGreeting()}}</p>
      <p>合計: {{getTotal()}}</p>
      <p>フォーマット価格: {{formatPrice(price)}}</p>
      <p>年齢チェック: {{checkAge(age)}}</p>
      <button (click)="refresh()">更新</button>
    </div>
  `,
  styles: [`
    .method-demo {
      padding: 20px;
      border: 1px solid #17a2b8;
      border-radius: 8px;
    }
  `]
})
export class MethodCallsComponent {
  price = 1500;
  age = 25;
  items = [100, 200, 300];
  
  getCurrentTime(): string {
    return new Date().toLocaleTimeString('ja-JP');
  }
  
  getGreeting(): string {
    const hour = new Date().getHours();
    return hour < 12 ? 'おはようございます' : 'こんにちは';
  }
  
  getTotal(): number {
    return this.items.reduce((sum, item) => sum + item, 0);
  }
  
  formatPrice(price: number): string {
    return `¥${price.toLocaleString()}`;
  }
  
  checkAge(age: number): string {
    return age >= 18 ? '成人' : '未成年';
  }
  
  refresh(): void {
    console.log('更新されました');
  }
}
```

// 三項演算子の評価
```typescript
@Component({
  selector: 'app-ternary-expressions',
  standalone: true,
  template: `
    <div class="ternary-demo">
      <h2>三項演算子の評価</h2>
      <p>ステータス: {{isActive ? 'アクティブ' : '非アクティブ'}}</p>
      <p>会員: {{isPremium ? 'プレミアム会員' : '一般会員'}}</p>
      <p>年齢区分: {{age >= 18 ? '成人' : '未成年'}}</p>
      <p>評価: {{score >= 80 ? '優秀' : score >= 60 ? '良好' : '要改善'}}</p>
      <p>在庫: {{stock > 0 ? stock + '個在庫あり' : '在庫なし'}}</p>
    </div>
  `,
  styles: [`
    .ternary-demo {
      padding: 20px;
      border: 1px solid #6610f2;
      border-radius: 8px;
    }
  `]
})
export class TernaryExpressionsComponent {
  isActive = true;
  isPremium = false;
  age = 25;
  score = 75;
  stock = 10;
}
```

// パフォーマンスの注意点
```typescript
@Component({
  selector: 'app-performance-notes',
  standalone: true,
  template: `
    <div class="performance-notes">
      <h2>パフォーマンスの注意点</h2>
      <div class="note good">
        <h3>✅ 良い例</h3>
        <p>シンプルな計算: {{price * quantity}}</p>
        <p>単純なメソッド: {{getTotal()}}</p>
        <p>Getter使用: {{total}}</p>
      </div>
      <div class="note bad">
        <h3>❌ 避けるべき例</h3>
        <p>重い計算: 避けるべき</p>
        <p>API呼び出し: 避けるべき</p>
        <p>複雑なループ: 避けるべき</p>
      </div>
    </div>
  `,
  styles: [`
    .performance-notes {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .note {
      margin: 15px 0;
      padding: 15px;
      border-radius: 8px;
    }
    .note.good {
      background-color: #d4edda;
      border: 1px solid #c3e6cb;
    }
    .note.bad {
      background-color: #f8d7da;
      border: 1px solid #f5c6cb;
    }
  `]
})
export class PerformanceNotesComponent {
  price = 1000;
  quantity = 5;
  
  get total(): number {
    return this.price * this.quantity;
  }
  
  getTotal(): number {
    return this.price * this.quantity;
  }
}
```
