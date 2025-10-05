# #026 「Component のバージョン管理」台本

四国めたん「Component のバージョン管理について学びましょう！」
ずんだもん「バージョン管理って何？」
四国めたん「Componentの変更履歴を追跡し、異なるバージョンを管理する仕組みです」
ずんだもん「どんなメリットがあるの？」
四国めたん「変更の追跡、ロールバック、ブランチ管理、チーム開発の効率化があります」
ずんだもん「どんなツールを使うの？」
四国めたん「Gitが最も一般的で、GitHub、GitLab、Bitbucketなどのサービスがあります」

---

## 📺 画面表示用コード

// バージョン管理の例：Componentの進化
```typescript
// v1.0.0 - 初期バージョン
@Component({
  selector: 'app-user-card-v1',
  standalone: true,
  template: `
    <div class="user-card">
      <h3>{{user.name}}</h3>
      <p>{{user.email}}</p>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 8px;
    }
  `]
})
export class UserCardV1Component {
  @Input() user!: User;
}
```

// v1.1.0 - 機能追加
```typescript
@Component({
  selector: 'app-user-card-v1-1',
  standalone: true,
  template: `
    <div class="user-card">
      <h3>{{user.name}}</h3>
      <p>{{user.email}}</p>
      <p>{{user.age}}歳</p>  <!-- 年齢表示を追加 -->
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ccc;
      padding: 15px;
      border-radius: 8px;
    }
  `]
})
export class UserCardV1_1Component {
  @Input() user!: User;
}
```

// v2.0.0 - 大幅な変更
```typescript
@Component({
  selector: 'app-user-card-v2',
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
        <button (click)="onEdit()">編集</button>
        <button (click)="onDelete()">削除</button>
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
    .user-actions button {
      margin-right: 10px;
      padding: 4px 8px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  `]
})
export class UserCardV2Component {
  @Input() user!: User;
  @Input() showActions = false;
  @Output() edit = new EventEmitter<User>();
  @Output() delete = new EventEmitter<User>();
  
  onEdit() {
    this.edit.emit(this.user);
  }
  
  onDelete() {
    this.delete.emit(this.user);
  }
}
```

// バージョン管理の設定ファイル
```json
// package.json
{
  "name": "angular-component-library",
  "version": "2.0.0",
  "description": "Angular Component Library",
  "main": "index.js",
  "scripts": {
    "build": "ng build",
    "test": "ng test",
    "lint": "ng lint",
    "version": "npm version",
    "release": "npm run build && npm publish"
  },
  "keywords": ["angular", "components", "ui"],
  "author": "Your Name",
  "license": "MIT",
  "peerDependencies": {
    "@angular/core": "^17.0.0",
    "@angular/common": "^17.0.0"
  }
}
```

// バージョン管理のタグ付け
```bash
# バージョンタグの作成
git tag -a v1.0.0 -m "初期バージョン: 基本的なユーザーカード"
git tag -a v1.1.0 -m "機能追加: 年齢表示を追加"
git tag -a v2.0.0 -m "大幅変更: 管理者機能とアクションボタンを追加"

# タグのプッシュ
git push origin v1.0.0
git push origin v1.1.0
git push origin v2.0.0

# タグの一覧表示
git tag -l

# 特定のバージョンにチェックアウト
git checkout v1.0.0
```

// バージョン管理のブランチ戦略
```typescript
// メインブランチ（main）
// - 安定版のコード
// - 本番環境にデプロイされるコード

// 開発ブランチ（develop）
// - 開発中の機能
// - 統合テスト用

// 機能ブランチ（feature/user-card-v2）
// - 新機能の開発
// - 個別の機能実装

// リリースブランチ（release/v2.0.0）
// - リリース準備
// - バグ修正

// ホットフィックスブランチ（hotfix/critical-bug-fix）
// - 緊急のバグ修正
// - 本番環境への即座の修正
```

// バージョン管理のコミットメッセージ
```bash
# 良いコミットメッセージの例
git commit -m "feat(user-card): 管理者機能を追加

- 管理者バッジの表示機能を追加
- 管理者用のスタイルを追加
- アクションボタンの表示/非表示を制御

Closes #123"

# コミットメッセージの規約
# feat: 新機能
# fix: バグ修正
# docs: ドキュメント更新
# style: コードスタイルの変更
# refactor: リファクタリング
# test: テストの追加・修正
# chore: ビルドプロセスやツールの変更
```

// バージョン管理の変更履歴
```markdown
# CHANGELOG.md

## [2.0.0] - 2024-01-15

### Added
- 管理者機能の追加
- アクションボタンの表示/非表示制御
- 部門情報の表示

### Changed
- ユーザーカードのレイアウトを大幅に変更
- スタイルの改善

### Breaking Changes
- `showActions`プロパティが必須になりました
- `edit`と`delete`イベントが必須になりました

## [1.1.0] - 2024-01-10

### Added
- 年齢表示機能を追加

## [1.0.0] - 2024-01-01

### Added
- 基本的なユーザーカード機能
- 名前とメールアドレスの表示
```

// バージョン管理の自動化
```typescript
// .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Run tests
        run: npm test
      - name: Publish to npm
        run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

// バージョン管理のベストプラクティス
```typescript
@Component({
  selector: 'app-version-control-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>バージョン管理のベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. セマンティックバージョニング</h3>
        <p>MAJOR.MINOR.PATCH形式でバージョンを管理</p>
      </div>
      <div class="practice-item">
        <h3>2. 意味のあるコミットメッセージ</h3>
        <p>変更内容が分かるコミットメッセージを書く</p>
      </div>
      <div class="practice-item">
        <h3>3. ブランチ戦略の統一</h3>
        <p>チームでブランチ戦略を統一する</p>
      </div>
      <div class="practice-item">
        <h3>4. 定期的なマージ</h3>
        <p>長期間のブランチを避け、定期的にマージする</p>
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
      border: 1px solid #007bff;
      border-radius: 8px;
      background-color: #e7f3ff;
    }
    .practice-item h3 {
      color: #004085;
      margin-top: 0;
    }
  `]
})
export class VersionControlBestPracticesComponent {
  // バージョン管理のベストプラクティスを説明
}
```
