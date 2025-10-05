# #040 「[attr.] 属性バインディング」台本

四国めたん「[attr.] 属性バインディングについて解説します！」
ずんだもん「attr.って何？」
四国めたん「HTML属性を動的に設定するためのバインディングです」
ずんだもん「どんな属性に使えるの？」
四国めたん「aria-、data-、title、tabindexなど、DOMプロパティではない属性に使用します」
ずんだもん「プロパティバインディングと何が違うの？」
四国めたん「プロパティは値が変更可能、属性は文字列のみで読み取り専用の場合が多いです」

---

## 📺 画面表示用コード

// 基本的な属性バインディング
```typescript
@Component({
  selector: 'app-attr-basic',
  standalone: true,
  template: `
    <div class="attr-demo">
      <h2>基本的な属性バインディング</h2>
      <input [attr.placeholder]="placeholder"
             [attr.title]="title"
             [attr.tabindex]="tabIndex">
      <button (click)="updateAttributes()">属性更新</button>
    </div>
  `,
  styles: [`
    .attr-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px;
      border: 1px solid #ccc;
    }
  `]
})
export class AttrBasicComponent {
  placeholder = 'デフォルトプレースホルダー';
  title = 'デフォルトタイトル';
  tabIndex = 1;
  
  updateAttributes() {
    this.placeholder = '更新されたプレースホルダー';
    this.title = '更新されたタイトル';
    this.tabIndex = this.tabIndex === 1 ? 2 : 1;
  }
}
```

// aria属性の設定
```typescript
@Component({
  selector: 'app-aria-attributes',
  standalone: true,
  template: `
    <div class="aria-demo">
      <h2>aria属性の設定</h2>
      <button [attr.aria-expanded]="isExpanded"
              [attr.aria-label]="ariaLabel"
              (click)="toggle()">
        {{isExpanded ? '閉じる' : '開く'}}
      </button>
      <div [attr.aria-hidden]="!isExpanded"
           [attr.aria-live]="isExpanded ? 'polite' : 'off'">
        コンテンツエリア
      </div>
    </div>
  `,
  styles: [`
    .aria-demo {
      padding: 20px;
    }
    button {
      padding: 8px 16px;
      margin: 10px;
    }
    div {
      padding: 15px;
      border: 1px solid #ccc;
      margin: 10px 0;
    }
  `]
})
export class AriaAttributesComponent {
  isExpanded = false;
  
  get ariaLabel(): string {
    return this.isExpanded ? 'メニューを閉じる' : 'メニューを開く';
  }
  
  toggle() {
    this.isExpanded = !this.isExpanded;
  }
}
```

// data属性の設定
```typescript
@Component({
  selector: 'app-data-attributes',
  standalone: true,
  template: `
    <div class="data-demo">
      <h2>data属性の設定</h2>
      <div [attr.data-user-id]="userId"
           [attr.data-role]="userRole"
           [attr.data-theme]="theme">
        ユーザー情報: {{userId}} - {{userRole}}
      </div>
      <button (click)="changeUser()">ユーザー変更</button>
      <button (click)="changeTheme()">テーマ変更</button>
    </div>
  `,
  styles: [`
    .data-demo {
      padding: 20px;
    }
    div {
      padding: 15px;
      border: 1px solid #ccc;
      margin: 10px 0;
    }
    button {
      margin: 5px;
      padding: 8px 16px;
    }
  `]
})
export class DataAttributesComponent {
  userId = 'user123';
  userRole = 'admin';
  theme = 'light';
  
  users = [
    { id: 'user123', role: 'admin' },
    { id: 'user456', role: 'user' },
    { id: 'user789', role: 'guest' }
  ];
  
  themes = ['light', 'dark', 'auto'];
  userIndex = 0;
  themeIndex = 0;
  
  changeUser() {
    this.userIndex = (this.userIndex + 1) % this.users.length;
    this.userId = this.users[this.userIndex].id;
    this.userRole = this.users[this.userIndex].role;
  }
  
  changeTheme() {
    this.themeIndex = (this.themeIndex + 1) % this.themes.length;
    this.theme = this.themes[this.themeIndex];
  }
}
```
