# #006 「templateUrl - 外部テンプレートファイル」台本

四国めたん「templateUrl - 外部テンプレートファイルについて解説します！」
ずんだもん「外部ファイルにするメリットは？」
四国めたん「HTMLエディタの機能が使え、可読性と保守性が向上します」
ずんだもん「どんな時に使うの？」
四国めたん「複雑なテンプレートや、チーム開発でHTMLとTypeScriptを分離したい場合です」
ずんだもん「ファイルの場所はどこに置くの？」
四国めたん「Componentと同じディレクトリに置くのが一般的です」

---

## 📺 画面表示用コード

// 基本的な外部テンプレートの使用
```typescript
@Component({
  selector: 'app-external',
  templateUrl: './external.component.html'
})
export class ExternalComponent {
  title = '外部テンプレート';
  items = ['項目1', '項目2', '項目3'];
}
```

// ファイル構造例
```
src/app/external/
├── external.component.ts
├── external.component.html
├── external.component.css
└── external.component.spec.ts
```

// 外部HTMLファイルの内容例
```html
<!-- external.component.html -->
<div class="container">
  <h1>{{title}}</h1>
  <div class="content">
    <p>外部テンプレートファイルを使用しています</p>
    <ul>
      <li *ngFor="let item of items">{{item}}</li>
    </ul>
  </div>
</div>
```

// 相対パスでの指定
```typescript
@Component({
  selector: 'app-relative',
  templateUrl: './templates/relative.component.html'
})
export class RelativeComponent {
  // 相対パスでテンプレートを指定
}
```

// 絶対パスでの指定
```typescript
@Component({
  selector: 'app-absolute',
  templateUrl: '/src/app/templates/absolute.component.html'
})
export class AbsoluteComponent {
  // 絶対パスでテンプレートを指定
}
```

// 複雑なテンプレートの例
```typescript
@Component({
  selector: 'app-complex',
  templateUrl: './complex.component.html'
})
export class ComplexComponent {
  users = [
    { id: 1, name: '田中太郎', email: 'tanaka@example.com' },
    { id: 2, name: '佐藤花子', email: 'sato@example.com' }
  ];
  
  selectedUser: any = null;
  
  selectUser(user: any) {
    this.selectedUser = user;
  }
}
```

// 複雑なHTMLテンプレート
```html
<!-- complex.component.html -->
<div class="user-management">
  <h2>ユーザー管理</h2>
  
  <div class="user-list">
    <h3>ユーザー一覧</h3>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>名前</th>
          <th>メール</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr *ngFor="let user of users">
          <td>{{user.id}}</td>
          <td>{{user.name}}</td>
          <td>{{user.email}}</td>
          <td>
            <button (click)="selectUser(user)">選択</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <div class="user-detail" *ngIf="selectedUser">
    <h3>選択されたユーザー</h3>
    <div class="detail-card">
      <p><strong>ID:</strong> {{selectedUser.id}}</p>
      <p><strong>名前:</strong> {{selectedUser.name}}</p>
      <p><strong>メール:</strong> {{selectedUser.email}}</p>
    </div>
  </div>
</div>
```

// 外部テンプレートの利点
```typescript
@Component({
  selector: 'app-benefits',
  templateUrl: './benefits.component.html'
})
export class BenefitsComponent {
  benefits = [
    'HTMLエディタの機能が使える',
    'シンタックスハイライト',
    '自動補完',
    'エラーチェック',
    'フォーマット機能',
    '可読性の向上',
    '保守性の向上'
  ];
}
```

// 外部テンプレートの注意点
```typescript
@Component({
  selector: 'app-considerations',
  templateUrl: './considerations.component.html'
})
export class ConsiderationsComponent {
  // 注意点:
  // 1. ファイルパスが正しいか確認
  // 2. ファイルが存在するか確認
  // 3. 相対パスと絶対パスの使い分け
  // 4. ビルド時のパス解決
}
```
