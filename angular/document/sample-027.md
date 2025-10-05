# #027 「Component のドキュメント作成」台本

四国めたん「Component のドキュメント作成について解説します！」
ずんだもん「ドキュメントってなぜ重要なの？」
四国めたん「Componentの使用方法、API、例を明確にすることで、開発効率と保守性が向上します」
ずんだもん「どんなドキュメントを作るの？」
四国めたん「README、API仕様書、使用例、変更履歴などがあります」
ずんだもん「どうやって書くの？」
四国めたん「JSDoc、Storybook、Markdownなどを活用して、分かりやすく書くことが重要です」

---

## 📺 画面表示用コード

// JSDocを使ったComponentドキュメント
```typescript
/**
 * ユーザー情報を表示するカードComponent
 * 
 * @example
 * ```html
 * <app-user-card 
 *   [user]="userData" 
 *   [showActions]="true"
 *   (edit)="onEdit($event)"
 *   (delete)="onDelete($event)">
 * </app-user-card>
 * ```
 * 
 * @since 1.0.0
 * @version 2.0.0
 */
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <div class="user-card" [class.admin]="user.role === 'admin'">
      <div class="user-header">
        <h3>{{user.name}}</h3>
        <span *ngIf="user.role === 'admin'" class="admin-badge">管理者</span>
      </div>
      <div class="user-info">
        <p class="email">{{user.email}}</p>
        <p class="age">{{user.age}}歳</p>
        <p *ngIf="user.department" class="department">{{user.department}}</p>
      </div>
      <div class="user-actions" *ngIf="showActions">
        <button (click)="onEdit()" class="edit-btn">編集</button>
        <button (click)="onDelete()" class="delete-btn">削除</button>
      </div>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 8px;
      margin-bottom: 10px;
    }
    .user-card.admin {
      border-color: #007bff;
      background-color: #f8f9fa;
    }
    .user-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .admin-badge {
      background-color: #007bff;
      color: white;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 12px;
    }
    .user-info p {
      margin: 5px 0;
    }
    .email {
      color: #666;
    }
    .age {
      color: #888;
    }
    .department {
      color: #28a745;
      font-weight: bold;
    }
    .user-actions {
      margin-top: 10px;
    }
    .edit-btn, .delete-btn {
      margin-right: 10px;
      padding: 4px 8px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .edit-btn {
      background-color: #28a745;
      color: white;
    }
    .delete-btn {
      background-color: #dc3545;
      color: white;
    }
  `]
})
export class UserCardComponent {
  /**
   * 表示するユーザー情報
   * @required
   */
  @Input() user!: User;
  
  /**
   * アクションボタンの表示/非表示
   * @default false
   */
  @Input() showActions = false;
  
  /**
   * ユーザー編集イベント
   * @emits User 編集対象のユーザー情報
   */
  @Output() edit = new EventEmitter<User>();
  
  /**
   * ユーザー削除イベント
   * @emits User 削除対象のユーザー情報
   */
  @Output() delete = new EventEmitter<User>();
  
  /**
   * 編集ボタンクリック時の処理
   * @private
   */
  onEdit(): void {
    this.edit.emit(this.user);
  }
  
  /**
   * 削除ボタンクリック時の処理
   * @private
   */
  onDelete(): void {
    this.delete.emit(this.user);
  }
}
```

// 型定義のドキュメント
```typescript
/**
 * ユーザー情報のインターフェース
 * 
 * @interface User
 * @since 1.0.0
 */
interface User {
  /** ユーザーID */
  id: number;
  
  /** ユーザー名 */
  name: string;
  
  /** メールアドレス */
  email: string;
  
  /** 年齢 */
  age: number;
  
  /** 部門（オプション） */
  department?: string;
  
  /** ロール（オプション） */
  role?: 'admin' | 'user';
}
```

// README.mdの例
```markdown
# UserCard Component

ユーザー情報を表示する再利用可能なAngular Componentです。

## インストール

```bash
npm install @your-org/user-card
```

## 基本的な使用方法

```typescript
import { UserCardComponent } from '@your-org/user-card';

@Component({
  selector: 'app-example',
  standalone: true,
  imports: [UserCardComponent],
  template: `
    <app-user-card [user]="userData"></app-user-card>
  `
})
export class ExampleComponent {
  userData: User = {
    id: 1,
    name: '田中太郎',
    email: 'tanaka@example.com',
    age: 30,
    department: '開発部'
  };
}
```

## API

### Inputs

| プロパティ | 型 | 必須 | デフォルト | 説明 |
|-----------|----|----|---------|------|
| user | User | ✅ | - | 表示するユーザー情報 |
| showActions | boolean | ❌ | false | アクションボタンの表示/非表示 |

### Outputs

| イベント | 型 | 説明 |
|---------|----|------|
| edit | EventEmitter<User> | 編集ボタンクリック時 |
| delete | EventEmitter<User> | 削除ボタンクリック時 |

## 使用例

### 基本的な表示

```html
<app-user-card [user]="userData"></app-user-card>
```

### アクションボタン付き

```html
<app-user-card 
  [user]="userData" 
  [showActions]="true"
  (edit)="onEdit($event)"
  (delete)="onDelete($event)">
</app-user-card>
```

### 管理者表示

```html
<app-user-card 
  [user]="adminUser" 
  [showActions]="true">
</app-user-card>
```

## スタイリング

Componentは以下のCSSクラスを提供します：

- `.user-card` - メインコンテナ
- `.user-card.admin` - 管理者用スタイル
- `.user-header` - ヘッダー部分
- `.user-info` - ユーザー情報部分
- `.user-actions` - アクションボタン部分

## 変更履歴

### v2.0.0
- 管理者機能を追加
- アクションボタンの表示/非表示制御を追加
- 部門情報の表示を追加

### v1.1.0
- 年齢表示機能を追加

### v1.0.0
- 初期リリース
```

// Storybookの設定例
```typescript
// user-card.stories.ts
import type { Meta, StoryObj } from '@storybook/angular';
import { UserCardComponent } from './user-card.component';

const meta: Meta<UserCardComponent> = {
  title: 'Components/UserCard',
  component: UserCardComponent,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    user: {
      control: 'object',
      description: '表示するユーザー情報',
    },
    showActions: {
      control: 'boolean',
      description: 'アクションボタンの表示/非表示',
    },
  },
};

export default meta;
type Story = StoryObj<UserCardComponent>;

export const Default: Story = {
  args: {
    user: {
      id: 1,
      name: '田中太郎',
      email: 'tanaka@example.com',
      age: 30,
      department: '開発部'
    },
    showActions: false,
  },
};

export const WithActions: Story = {
  args: {
    user: {
      id: 1,
      name: '田中太郎',
      email: 'tanaka@example.com',
      age: 30,
      department: '開発部'
    },
    showActions: true,
  },
};

export const AdminUser: Story = {
  args: {
    user: {
      id: 1,
      name: '管理者太郎',
      email: 'admin@example.com',
      age: 35,
      department: '管理部',
      role: 'admin'
    },
    showActions: true,
  },
};
```

// ドキュメント生成の自動化
```json
// package.json
{
  "scripts": {
    "docs:build": "compodoc -p tsconfig.json -s",
    "docs:serve": "compodoc -p tsconfig.json -s -w",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build"
  },
  "devDependencies": {
    "@compodoc/compodoc": "^1.1.23",
    "@storybook/angular": "^7.0.0"
  }
}
```

// ドキュメントのベストプラクティス
```typescript
@Component({
  selector: 'app-documentation-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>ドキュメントのベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. 明確な説明</h3>
        <p>Componentの目的と使用方法を明確に説明</p>
      </div>
      <div class="practice-item">
        <h3>2. 実用的な例</h3>
        <p>実際の使用場面を想定した例を提供</p>
      </div>
      <div class="practice-item">
        <h3>3. API仕様の明記</h3>
        <p>Input/Outputの詳細な仕様を記載</p>
      </div>
      <div class="practice-item">
        <h3>4. 定期的な更新</h3>
        <p>Componentの変更に合わせてドキュメントを更新</p>
      </div>
    </div>
  `,
  styles: [`
    .best-practices {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .practice-item {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    .practice-item h3 {
      color: #155724;
      margin-top: 0;
    }
  `]
})
export class DocumentationBestPracticesComponent {
  // ドキュメントのベストプラクティスを説明
}
```
