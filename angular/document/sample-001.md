# #001 「Component とは？Angular の基本単位」台本

四国めたん「Component とは？Angular の基本単位について学びましょう！」
ずんだもん「Componentって、どんな役割があるの？」
四国めたん「Componentは、Angularアプリケーションの基本構成要素です。UIの一部分を独立した単位として管理します」
ずんだもん「HTMLとTypeScriptが組み合わさった感じなの？」
四国めたん「はい！テンプレート、クラス、メタデータの3つの要素で構成されています」
ずんだもん「なるほど！再利用できる独立した部品として使えるんだね！」
四国めたん「その通りです！Componentベースの設計により、保守性と再利用性が向上します」

---

## 📺 画面表示用コード

// Componentの基本構造
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-hello',
  template: '<h1>Hello Angular!</h1>',
  styles: ['h1 { color: blue; }']
})
export class HelloComponent {
  message = 'Hello World!';
}
```

// Componentの3つの要素
```typescript
@Component({
  selector: 'app-user',     // メタデータ：セレクタ
  template: `               // テンプレート：HTML
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `,
  styles: [`               // スタイル：CSS
    div { padding: 20px; }
    h2 { color: #333; }
  `]
})
export class UserComponent {  // クラス：TypeScript
  user = {
    name: '田中太郎',
    email: 'tanaka@example.com'
  };
}
```

// Standalone Component（v14+）
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-standalone',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div *ngIf="isVisible">
      <p>Standalone Componentです！</p>
    </div>
  `
})
export class StandaloneComponent {
  isVisible = true;
}
```

// Componentの再利用例
```typescript
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <h3>{{title}}</h3>
      <p>{{content}}</p>
    </div>
  `,
  styles: [`
    .card {
      border: 1px solid #ccc;
      padding: 16px;
      margin: 8px;
      border-radius: 4px;
    }
  `]
})
export class CardComponent {
  @Input() title = '';
  @Input() content = '';
}
```

// Componentの組み合わせ
```typescript
@Component({
  selector: 'app-dashboard',
  template: `
    <h1>ダッシュボード</h1>
    <app-card title="ユーザー数" content="1,234人"></app-card>
    <app-card title="売上" content="¥1,000,000"></app-card>
  `
})
export class DashboardComponent {
  // 複数のComponentを組み合わせて使用
}
```
