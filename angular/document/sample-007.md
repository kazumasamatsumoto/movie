# #007 「styles - インラインスタイル」台本

四国めたん「styles - インラインスタイルについて学びましょう！」
ずんだもん「インラインスタイルって何？」
四国めたん「Componentクラス内に直接CSSを記述する方法です」
ずんだもん「外部ファイルとどっちがいいの？」
四国めたん「短いスタイルはインライン、複雑なスタイルは外部ファイルがおすすめです」
ずんだもん「どんな時に使うの？」
四国めたん「シンプルなスタイルや、Component固有のスタイルに便利です」

---

## 📺 画面表示用コード

// 基本的なインラインスタイル
```typescript
@Component({
  selector: 'app-inline-style',
  template: '<h1>インラインスタイル</h1>',
  styles: ['h1 { color: blue; font-size: 24px; }']
})
export class InlineStyleComponent {
  // シンプルなスタイル
}
```

// 複数行のインラインスタイル
```typescript
@Component({
  selector: 'app-multiline-style',
  template: `
    <div class="container">
      <h2>{{title}}</h2>
      <p>{{description}}</p>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      background-color: #f0f0f0;
      border-radius: 8px;
    }
    h2 {
      color: #333;
      margin-bottom: 10px;
    }
    p {
      color: #666;
      line-height: 1.5;
    }
  `]
})
export class MultilineStyleComponent {
  title = 'マルチラインスタイル';
  description = '複数行のスタイルです';
}
```

// 複数のスタイルブロック
```typescript
@Component({
  selector: 'app-multiple-styles',
  template: `
    <div class="card">
      <div class="header">
        <h3>{{title}}</h3>
      </div>
      <div class="content">
        <p>{{content}}</p>
      </div>
    </div>
  `,
  styles: [
    '.card { border: 1px solid #ccc; border-radius: 4px; }',
    '.header { background-color: #007bff; color: white; padding: 10px; }',
    '.content { padding: 15px; }',
    'h3 { margin: 0; }'
  ]
})
export class MultipleStylesComponent {
  title = 'カードタイトル';
  content = 'カードの内容です';
}
```

// 動的スタイルの例
```typescript
@Component({
  selector: 'app-dynamic-style',
  template: `
    <div [class]="cardClass">
      <h4>{{title}}</h4>
      <p>{{message}}</p>
    </div>
  `,
  styles: [`
    .success-card {
      background-color: #d4edda;
      border: 1px solid #c3e6cb;
      color: #155724;
      padding: 15px;
      border-radius: 4px;
    }
    .error-card {
      background-color: #f8d7da;
      border: 1px solid #f5c6cb;
      color: #721c24;
      padding: 15px;
      border-radius: 4px;
    }
    .warning-card {
      background-color: #fff3cd;
      border: 1px solid #ffeaa7;
      color: #856404;
      padding: 15px;
      border-radius: 4px;
    }
  `]
})
export class DynamicStyleComponent {
  title = '動的スタイル';
  message = '状態に応じてスタイルが変わります';
  cardType = 'success';
  
  get cardClass() {
    return `${this.cardType}-card`;
  }
}
```

// ホスト要素のスタイル
```typescript
@Component({
  selector: 'app-host-style',
  template: '<p>ホスト要素のスタイル</p>',
  styles: [`
    :host {
      display: block;
      padding: 20px;
      background-color: #e9ecef;
      border: 2px solid #dee2e6;
    }
    :host:hover {
      background-color: #f8f9fa;
      border-color: #007bff;
    }
  `]
})
export class HostStyleComponent {
  // :hostセレクタでComponent要素自体をスタイル
}
```

// 子要素のスタイル
```typescript
@Component({
  selector: 'app-child-style',
  template: `
    <div class="parent">
      <h5>親要素</h5>
      <div class="child">
        <p>子要素</p>
      </div>
    </div>
  `,
  styles: [`
    .parent {
      background-color: #f8f9fa;
      padding: 20px;
    }
    .parent .child {
      background-color: #e9ecef;
      padding: 10px;
      margin-top: 10px;
    }
    .parent .child p {
      margin: 0;
      color: #495057;
    }
  `]
})
export class ChildStyleComponent {
  // ネストした要素のスタイル
}
```

// インラインスタイルの利点
```typescript
@Component({
  selector: 'app-advantages',
  template: `
    <div class="advantages">
      <h6>インラインスタイルの利点</h6>
      <ul>
        <li>ファイル数が少ない</li>
        <li>Componentとスタイルが同じファイル</li>
        <li>IDEの補完が効く</li>
        <li>リファクタリングが簡単</li>
      </ul>
    </div>
  `,
  styles: [`
    .advantages {
      background-color: #d1ecf1;
      padding: 15px;
      border-radius: 4px;
    }
    .advantages h6 {
      color: #0c5460;
      margin-top: 0;
    }
    .advantages ul {
      margin-bottom: 0;
    }
  `]
})
export class AdvantagesComponent {
  // 短いスタイルには最適
}
```
