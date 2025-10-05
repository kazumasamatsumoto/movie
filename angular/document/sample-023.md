# #023 「Component の削除方法」台本

四国めたん「Component の削除方法について解説します！」
ずんだもん「Componentを削除する時って何に注意すればいいの？」
四国めたん「他のComponentで使用されていないか、NgModuleに登録されていないかを確認する必要があります」
ずんだもん「どんな手順で削除するの？」
四国めたん「使用箇所の確認、NgModuleからの削除、ファイルの削除の順番で行います」
ずんだもん「CLIで削除できるの？」
四国めたん「残念ながら、CLIには削除コマンドがないので、手動で削除する必要があります」

---

## 📺 画面表示用コード

// 削除対象のComponent例
```typescript
// user-card.component.ts（削除予定）
@Component({
  selector: 'app-user-card',
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
export class UserCardComponent {
  @Input() user: any;
}
```

// 削除前の使用例
```typescript
// user-list.component.ts
import { Component } from '@angular/core';
import { UserCardComponent } from './user-card/user-card.component'; // 削除対象

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [UserCardComponent], // 削除対象
  template: `
    <div>
      <h2>ユーザー一覧</h2>
      <app-user-card *ngFor="let user of users" [user]="user"></app-user-card>
    </div>
  `
})
export class UserListComponent {
  users = [
    { name: '田中太郎', email: 'tanaka@example.com' },
    { name: '佐藤花子', email: 'sato@example.com' }
  ];
}
```

// 削除手順1: 使用箇所の確認
```typescript
// 1. 検索で使用箇所を確認
// 以下の場所でUserCardComponentが使用されているかチェック:
// - テンプレートファイル（.html）
// - TypeScriptファイル（.ts）
// - モジュールファイル（.module.ts）

// 使用箇所の例
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [UserCardComponent], // ❌ 使用箇所
  template: `
    <div>
      <h1>ダッシュボード</h1>
      <app-user-card [user]="currentUser"></app-user-card> <!-- ❌ 使用箇所 -->
    </div>
  `
})
export class DashboardComponent {
  currentUser = { name: '管理者', email: 'admin@example.com' };
}
```

// 削除手順2: 使用箇所の削除
```typescript
// user-list.component.ts（修正後）
import { Component } from '@angular/core';
// import { UserCardComponent } from './user-card/user-card.component'; // ❌ 削除

@Component({
  selector: 'app-user-list',
  standalone: true,
  // imports: [UserCardComponent], // ❌ 削除
  template: `
    <div>
      <h2>ユーザー一覧</h2>
      <!-- <app-user-card *ngFor="let user of users" [user]="user"></app-user-card> --> <!-- ❌ 削除 -->
      <div *ngFor="let user of users" class="user-item">
        <h3>{{user.name}}</h3>
        <p>{{user.email}}</p>
      </div>
    </div>
  `,
  styles: [`
    .user-item {
      border: 1px solid #ddd;
      padding: 15px;
      margin-bottom: 10px;
      border-radius: 8px;
    }
  `]
})
export class UserListComponent {
  users = [
    { name: '田中太郎', email: 'tanaka@example.com' },
    { name: '佐藤花子', email: 'sato@example.com' }
  ];
}
```

// 削除手順3: NgModuleからの削除
```typescript
// user.module.ts（修正前）
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserCardComponent } from './user-card/user-card.component'; // ❌ 削除対象
import { UserListComponent } from './user-list/user-list.component';

@NgModule({
  declarations: [
    UserCardComponent, // ❌ 削除対象
    UserListComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    UserCardComponent, // ❌ 削除対象
    UserListComponent
  ]
})
export class UserModule { }

// user.module.ts（修正後）
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
// import { UserCardComponent } from './user-card/user-card.component'; // ❌ 削除
import { UserListComponent } from './user-list/user-list.component';

@NgModule({
  declarations: [
    // UserCardComponent, // ❌ 削除
    UserListComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    // UserCardComponent, // ❌ 削除
    UserListComponent
  ]
})
export class UserModule { }
```

// 削除手順4: ファイルの削除
```bash
# 削除するファイル
rm -rf src/app/user-card/
# または
rm src/app/user-card/user-card.component.ts
rm src/app/user-card/user-card.component.html
rm src/app/user-card/user-card.component.css
rm src/app/user-card/user-card.component.spec.ts
```

// 削除後の確認
```typescript
// 削除後の状態確認
@Component({
  selector: 'app-deletion-check',
  standalone: true,
  template: `
    <div class="deletion-check">
      <h2>削除確認</h2>
      <div class="check-item">
        <h3>✅ 使用箇所の削除</h3>
        <p>他のComponentでUserCardComponentが使用されていない</p>
      </div>
      <div class="check-item">
        <h3>✅ NgModuleからの削除</h3>
        <p>UserModuleからUserCardComponentが削除されている</p>
      </div>
      <div class="check-item">
        <h3>✅ ファイルの削除</h3>
        <p>user-card.component.* ファイルが削除されている</p>
      </div>
      <div class="check-item">
        <h3>✅ ビルドエラーの確認</h3>
        <p>ng build でエラーが発生しない</p>
      </div>
    </div>
  `,
  styles: [`
    .deletion-check {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .check-item {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    .check-item h3 {
      color: #155724;
      margin-top: 0;
    }
  `]
})
export class DeletionCheckComponent {
  // 削除が正しく完了したか確認
}
```

// 削除時の注意事項
```typescript
@Component({
  selector: 'app-deletion-notes',
  standalone: true,
  template: `
    <div class="deletion-notes">
      <h2>削除時の注意事項</h2>
      <div class="note-item">
        <h3>⚠️ 依存関係の確認</h3>
        <p>他のComponentやServiceが依存していないか確認</p>
      </div>
      <div class="note-item">
        <h3>⚠️ テストファイルの削除</h3>
        <p>spec.tsファイルも忘れずに削除</p>
      </div>
      <div class="note-item">
        <h3>⚠️ インポート文の削除</h3>
        <p>使用していないimport文を削除</p>
      </div>
      <div class="note-item">
        <h3>⚠️ バックアップの作成</h3>
        <p>重要なComponentは削除前にバックアップを作成</p>
      </div>
    </div>
  `,
  styles: [`
    .deletion-notes {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .note-item {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #ffc107;
      border-radius: 8px;
      background-color: #fff3cd;
    }
    .note-item h3 {
      color: #856404;
      margin-top: 0;
    }
  `]
})
export class DeletionNotesComponent {
  // 削除時の注意事項を説明
}
```

// 削除のベストプラクティス
```typescript
@Component({
  selector: 'app-deletion-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>削除のベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. 段階的な削除</h3>
        <p>一度にすべてを削除せず、段階的に削除</p>
      </div>
      <div class="practice-item">
        <h3>2. 検索機能の活用</h3>
        <p>IDEの検索機能で使用箇所を確認</p>
      </div>
      <div class="practice-item">
        <h3>3. テストの実行</h3>
        <p>削除後にテストを実行して動作確認</p>
      </div>
      <div class="practice-item">
        <h3>4. ドキュメントの更新</h3>
        <p>削除したComponentのドキュメントを更新</p>
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
export class DeletionBestPracticesComponent {
  // 削除のベストプラクティスを説明
}
```
