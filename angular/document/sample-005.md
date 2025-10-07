# #005 「template - インラインテンプレート」

## 概要
templateプロパティを使用すると、TypeScriptファイル内に直接HTMLを記述できます。小規模なComponentに適した方法です。

## 学習目標
- templateとtemplateUrlの違いを理解する
- インラインテンプレートの適切な使用場面を学ぶ
- バッククォートを使った複数行記述を習得する

## 技術ポイント
- **template**: インラインHTML記述
- **templateUrl**: 別ファイル参照
- **バッククォート**: 複数行文字列の記述

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 1行のインラインテンプレート
@Component({
  selector: 'app-simple',
  template: '<p>Hello Angular!</p>'
})
export class SimpleComponent {}
```

```typescript
// バッククォートで複数行
@Component({
  selector: 'app-card',
  standalone: true,
  template: `
    <div class="card">
      <h2>{{title}}</h2>
      <p>{{content}}</p>
    </div>
  `
})
export class CardComponent {
  title = 'Card Title';
  content = 'Card content here';
}
```

```typescript
// templateUrlとの比較
@Component({
  selector: 'app-user',
  templateUrl: './user.component.html'  // 別ファイル参照
})
export class UserComponent {}
```

## 💻 詳細実装例（学習用）

### シンプルなインラインテンプレート
```typescript
import { Component } from '@angular/core';

// 1行のシンプルなテンプレート
@Component({
  selector: 'app-hello',
  standalone: true,
  template: '<h1>Hello, {{name}}!</h1>'
})
export class HelloComponent {
  name = 'Angular Developer';
}

// 少し複雑なテンプレート
@Component({
  selector: 'app-greeting',
  standalone: true,
  template: '<div><h1>{{greeting}}</h1><p>{{message}}</p></div>'
})
export class GreetingComponent {
  greeting = 'Welcome';
  message = 'This is an inline template';
}
```

### バッククォートを使った複数行テンプレート
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-card',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="user-card">
      <img [src]="user.avatar" [alt]="user.name">
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
      <button (click)="viewProfile()">View Profile</button>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 16px;
      border-radius: 8px;
    }
    img {
      width: 64px;
      height: 64px;
      border-radius: 50%;
    }
  `]
})
export class UserCardComponent {
  user = {
    name: 'John Doe',
    email: 'john@example.com',
    avatar: 'https://via.placeholder.com/64'
  };

  viewProfile() {
    console.log('Viewing profile:', this.user.name);
  }
}
```

### 制御フロー構文を使ったテンプレート（v20）
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-task-list',
  standalone: true,
  template: `
    <div class="task-list">
      <h2>Tasks</h2>

      @if (tasks.length > 0) {
        <ul>
          @for (task of tasks; track task.id) {
            <li [class.completed]="task.completed">
              {{task.title}}
            </li>
          }
        </ul>
      } @else {
        <p>No tasks available</p>
      }
    </div>
  `,
  styles: [`
    .completed {
      text-decoration: line-through;
      color: #999;
    }
  `]
})
export class TaskListComponent {
  tasks = [
    { id: 1, title: 'Learn Angular', completed: true },
    { id: 2, title: 'Build a project', completed: false },
    { id: 3, title: 'Deploy to production', completed: false }
  ];
}
```

### データバインディングを含むテンプレート
```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-input-demo',
  standalone: true,
  imports: [FormsModule],
  template: `
    <div class="input-demo">
      <label for="username">Username:</label>
      <input
        id="username"
        type="text"
        [(ngModel)]="username"
        (input)="onInputChange()"
      >
      <p>Hello, {{username || 'Guest'}}!</p>
      <p>Character count: {{username.length}}</p>
    </div>
  `,
  styles: [`
    .input-demo {
      padding: 16px;
    }
    input {
      margin: 8px 0;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  `]
})
export class InputDemoComponent {
  username = '';

  onInputChange() {
    console.log('Username changed:', this.username);
  }
}
```

### イベントハンドリングを含むテンプレート
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  standalone: true,
  template: `
    <div class="counter">
      <h2>Counter: {{count}}</h2>
      <div class="buttons">
        <button (click)="increment()">+</button>
        <button (click)="decrement()">-</button>
        <button (click)="reset()">Reset</button>
      </div>
      <p [class.warning]="count < 0">
        {{count < 0 ? 'Negative value!' : 'Positive or zero'}}
      </p>
    </div>
  `,
  styles: [`
    .counter {
      text-align: center;
      padding: 20px;
    }
    .buttons {
      margin: 16px 0;
    }
    button {
      margin: 0 8px;
      padding: 8px 16px;
      cursor: pointer;
    }
    .warning {
      color: red;
      font-weight: bold;
    }
  `]
})
export class CounterComponent {
  count = 0;

  increment() {
    this.count++;
  }

  decrement() {
    this.count--;
  }

  reset() {
    this.count = 0;
  }
}
```

### テンプレート vs ファイル参照の使い分け
```typescript
// ❌ 悪い例: 長すぎるインラインテンプレート
@Component({
  selector: 'app-complex-form',
  template: `
    <form>
      <div class="form-group">
        <label>Name</label>
        <input type="text" />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input type="email" />
      </div>
      <!-- ... 50行以上のフォーム ... -->
    </form>
  `
})
export class ComplexFormComponent {}

// ✅ 良い例: 短いテンプレートはインライン
@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="variant" (click)="handleClick()">
      {{label}}
    </button>
  `
})
export class ButtonComponent {
  label = 'Click me';
  variant = 'primary';

  handleClick() {
    console.log('Clicked');
  }
}

// ✅ 良い例: 長いテンプレートは別ファイル
@Component({
  selector: 'app-user-dashboard',
  standalone: true,
  templateUrl: './user-dashboard.component.html',
  styleUrls: ['./user-dashboard.component.css']
})
export class UserDashboardComponent {}
```

### インラインテンプレートの実践例
```typescript
// 再利用可能なアイコンボタン
@Component({
  selector: 'app-icon-button',
  standalone: true,
  template: `
    <button [title]="tooltip" (click)="handleClick()">
      <span class="icon">{{icon}}</span>
      @if (label) {
        <span class="label">{{label}}</span>
      }
    </button>
  `,
  styles: [`
    button {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border: none;
      background: #007bff;
      color: white;
      border-radius: 4px;
      cursor: pointer;
    }
    .icon { font-size: 20px; }
  `]
})
export class IconButtonComponent {
  icon = '🔍';
  label = '';
  tooltip = '';

  handleClick() {
    console.log('Icon button clicked');
  }
}

// ステータスバッジ
@Component({
  selector: 'app-status-badge',
  standalone: true,
  template: `
    <span [class]="'badge badge-' + status">
      {{statusText}}
    </span>
  `,
  styles: [`
    .badge {
      padding: 4px 8px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: bold;
    }
    .badge-success { background: #28a745; color: white; }
    .badge-warning { background: #ffc107; color: black; }
    .badge-error { background: #dc3545; color: white; }
  `]
})
export class StatusBadgeComponent {
  status: 'success' | 'warning' | 'error' = 'success';
  statusText = 'Active';
}
```

## ベストプラクティス

1. **短いテンプレートにはtemplateを使用**: 5-10行以内が目安
2. **複雑なテンプレートはtemplateUrlを使用**: 保守性向上
3. **バッククォートを活用**: 複数行の可読性向上
4. **適切なインデント**: テンプレート内のHTMLも整形

## 注意点

- templateとtemplateUrlは同時に使用できない
- 長すぎるインラインテンプレートは可読性が低下
- エディタのシンタックスハイライトが効きにくい場合がある
- バッククォート内のインデントに注意

## 関連技術
- Template Syntax
- Data Binding
- Control Flow (@if, @for)
- String Literals (Template Literals)
