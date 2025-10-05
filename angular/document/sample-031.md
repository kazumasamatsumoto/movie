# #031 「{{ }} 補間バインディング - データ表示」台本

四国めたん「{{ }} 補間バインディング - データ表示について学びましょう！」
ずんだもん「補間バインディングって何？」
四国めたん「Componentのプロパティ値をテンプレートに表示する、最も基本的なバインディング方法です」
ずんだもん「どうやって使うの？」
四国めたん「二重の波括弧{{}}でプロパティ名を囲むだけです」
ずんだもん「どんな値を表示できるの？」
四国めたん「文字列、数値、真偽値、オブジェクトのプロパティ、メソッドの戻り値などが表示できます」

---

## 📺 画面表示用コード

// 基本的な補間バインディング
```typescript
@Component({
  selector: 'app-interpolation-basic',
  standalone: true,
  template: `
    <div class="interpolation-demo">
      <h2>基本的な補間バインディング</h2>
      <p>タイトル: {{title}}</p>
      <p>説明: {{description}}</p>
      <p>カウント: {{count}}</p>
      <p>アクティブ: {{isActive}}</p>
    </div>
  `,
  styles: [`
    .interpolation-demo {
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 8px;
      max-width: 600px;
      margin: 0 auto;
    }
    p {
      margin: 10px 0;
      font-size: 16px;
    }
  `]
})
export class InterpolationBasicComponent {
  title = 'Angular補間バインディング';
  description = 'データを表示する最も基本的な方法です';
  count = 42;
  isActive = true;
}
```

// 文字列の補間
```typescript
@Component({
  selector: 'app-string-interpolation',
  standalone: true,
  template: `
    <div class="string-demo">
      <h2>文字列の補間</h2>
      <p>名前: {{firstName}} {{lastName}}</p>
      <p>挨拶: {{greeting}}</p>
      <p>メッセージ: {{message}}</p>
      <p>完全な名前: {{fullName}}</p>
    </div>
  `,
  styles: [`
    .string-demo {
      padding: 20px;
      background-color: #f8f9fa;
      border-radius: 8px;
    }
  `]
})
export class StringInterpolationComponent {
  firstName = '田中';
  lastName = '太郎';
  greeting = 'こんにちは';
  message = 'Angularへようこそ！';
  fullName = `${this.firstName} ${this.lastName}`;
}
```

// 数値の補間
```typescript
@Component({
  selector: 'app-number-interpolation',
  standalone: true,
  template: `
    <div class="number-demo">
      <h2>数値の補間</h2>
      <p>価格: ¥{{price}}</p>
      <p>数量: {{quantity}}個</p>
      <p>合計: ¥{{total}}</p>
      <p>消費税(10%): ¥{{tax}}</p>
      <p>税込価格: ¥{{priceWithTax}}</p>
    </div>
  `,
  styles: [`
    .number-demo {
      padding: 20px;
      border: 1px solid #007bff;
      border-radius: 8px;
    }
    p {
      font-weight: bold;
      color: #007bff;
    }
  `]
})
export class NumberInterpolationComponent {
  price = 1000;
  quantity = 5;
  
  get total(): number {
    return this.price * this.quantity;
  }
  
  get tax(): number {
    return Math.floor(this.total * 0.1);
  }
  
  get priceWithTax(): number {
    return this.total + this.tax;
  }
}
```

// オブジェクトのプロパティ補間
```typescript
@Component({
  selector: 'app-object-interpolation',
  standalone: true,
  template: `
    <div class="object-demo">
      <h2>オブジェクトのプロパティ補間</h2>
      <div class="user-card">
        <h3>{{user.name}}</h3>
        <p>メール: {{user.email}}</p>
        <p>年齢: {{user.age}}歳</p>
        <p>部門: {{user.department}}</p>
        <p>役職: {{user.position}}</p>
      </div>
      <div class="address-card">
        <h3>住所情報</h3>
        <p>郵便番号: {{user.address.zipCode}}</p>
        <p>都道府県: {{user.address.prefecture}}</p>
        <p>市区町村: {{user.address.city}}</p>
      </div>
    </div>
  `,
  styles: [`
    .object-demo {
      padding: 20px;
    }
    .user-card, .address-card {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    h3 {
      margin-top: 0;
      color: #155724;
    }
  `]
})
export class ObjectInterpolationComponent {
  user = {
    name: '田中太郎',
    email: 'tanaka@example.com',
    age: 30,
    department: '開発部',
    position: 'シニアエンジニア',
    address: {
      zipCode: '100-0001',
      prefecture: '東京都',
      city: '千代田区'
    }
  };
}
```

// 配列の補間
```typescript
@Component({
  selector: 'app-array-interpolation',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="array-demo">
      <h2>配列の補間</h2>
      <p>最初の項目: {{items[0]}}</p>
      <p>2番目の項目: {{items[1]}}</p>
      <p>最後の項目: {{items[items.length - 1]}}</p>
      <p>配列の長さ: {{items.length}}</p>
      <h3>全項目</h3>
      <ul>
        <li *ngFor="let item of items; let i = index">
          {{i + 1}}. {{item}}
        </li>
      </ul>
    </div>
  `,
  styles: [`
    .array-demo {
      padding: 20px;
      border: 1px solid #ffc107;
      border-radius: 8px;
    }
    ul {
      list-style-type: none;
      padding-left: 0;
    }
    li {
      padding: 8px;
      margin: 5px 0;
      background-color: #fff3cd;
      border-radius: 4px;
    }
  `]
})
export class ArrayInterpolationComponent {
  items = ['項目1', '項目2', '項目3', '項目4', '項目5'];
}
```

// メソッドの戻り値の補間
```typescript
@Component({
  selector: 'app-method-interpolation',
  standalone: true,
  template: `
    <div class="method-demo">
      <h2>メソッドの戻り値の補間</h2>
      <p>現在時刻: {{getCurrentTime()}}</p>
      <p>挨拶メッセージ: {{getGreeting()}}</p>
      <p>ランダム数: {{getRandomNumber()}}</p>
      <p>フォーマット日付: {{getFormattedDate()}}</p>
      <p>計算結果: {{calculate(10, 20)}}</p>
    </div>
  `,
  styles: [`
    .method-demo {
      padding: 20px;
      border: 1px solid #dc3545;
      border-radius: 8px;
    }
    p {
      color: #721c24;
      background-color: #f8d7da;
      padding: 10px;
      border-radius: 4px;
      margin: 10px 0;
    }
  `]
})
export class MethodInterpolationComponent {
  getCurrentTime(): string {
    return new Date().toLocaleTimeString('ja-JP');
  }
  
  getGreeting(): string {
    const hour = new Date().getHours();
    if (hour < 12) return 'おはようございます';
    if (hour < 18) return 'こんにちは';
    return 'こんばんは';
  }
  
  getRandomNumber(): number {
    return Math.floor(Math.random() * 100);
  }
  
  getFormattedDate(): string {
    const date = new Date();
    return `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日`;
  }
  
  calculate(a: number, b: number): number {
    return a + b;
  }
}
```

// 条件式の補間
```typescript
@Component({
  selector: 'app-conditional-interpolation',
  standalone: true,
  template: `
    <div class="conditional-demo">
      <h2>条件式の補間</h2>
      <p>ステータス: {{isActive ? 'アクティブ' : '非アクティブ'}}</p>
      <p>メッセージ: {{count > 0 ? count + '件のメッセージがあります' : 'メッセージはありません'}}</p>
      <p>会員種別: {{isPremium ? 'プレミアム会員' : '一般会員'}}</p>
      <p>年齢区分: {{age >= 18 ? '成人' : '未成年'}}</p>
      <button (click)="toggleActive()">ステータス切り替え</button>
      <button (click)="incrementCount()">カウント増加</button>
    </div>
  `,
  styles: [`
    .conditional-demo {
      padding: 20px;
      border: 1px solid #17a2b8;
      border-radius: 8px;
    }
    p {
      font-size: 16px;
      margin: 10px 0;
    }
    button {
      margin-right: 10px;
      padding: 8px 16px;
      background-color: #17a2b8;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #138496;
    }
  `]
})
export class ConditionalInterpolationComponent {
  isActive = true;
  count = 5;
  isPremium = false;
  age = 25;
  
  toggleActive(): void {
    this.isActive = !this.isActive;
  }
  
  incrementCount(): void {
    this.count++;
  }
}
```

// 補間バインディングの注意点
```typescript
@Component({
  selector: 'app-interpolation-notes',
  standalone: true,
  template: `
    <div class="notes">
      <h2>補間バインディングの注意点</h2>
      <div class="note-item">
        <h3>✅ 使用できるもの</h3>
        <ul>
          <li>プロパティ値: {{title}}</li>
          <li>式の評価: {{1 + 1}}</li>
          <li>メソッド呼び出し: {{getMessage()}}</li>
          <li>三項演算子: {{isActive ? 'ON' : 'OFF'}}</li>
        </ul>
      </div>
      <div class="note-item">
        <h3>❌ 使用できないもの</h3>
        <ul>
          <li>代入: {{ x = 10 }} ← エラー</li>
          <li>new演算子: {{ new Date() }} ← エラー</li>
          <li>インクリメント: {{ count++ }} ← エラー</li>
          <li>複数の文: {{ a = 1; b = 2 }} ← エラー</li>
        </ul>
      </div>
    </div>
  `,
  styles: [`
    .notes {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .note-item {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    .note-item h3 {
      margin-top: 0;
    }
    ul {
      margin-bottom: 0;
    }
  `]
})
export class InterpolationNotesComponent {
  title = 'タイトル';
  isActive = true;
  
  getMessage(): string {
    return 'メソッドの戻り値';
  }
}
```
