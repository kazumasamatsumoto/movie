# #036 「[href] リンクバインディング」台本

四国めたん「[href] リンクバインディングについて解説します！」
ずんだもん「リンクのURLを動的に設定できるの？」
四国めたん「はい！プロパティバインディングでhref属性を動的に設定できます」
ずんだもん「どんな場面で使うの？」
四国めたん「ユーザープロフィール、商品詳細ページ、条件に応じたリンクなどです」
ずんだもん「外部リンクと内部リンクは違う？」
四国めたん「外部リンクはtarget="_blank"を追加して、セキュリティ対策も必要です」

---

## 📺 画面表示用コード

// 基本的なリンクバインディング
```typescript
@Component({
  selector: 'app-href-binding',
  standalone: true,
  template: `
    <div class="link-demo">
      <h2>基本的なリンクバインディング</h2>
      <a [href]="linkUrl">{{linkText}}</a>
      <p>URL: {{linkUrl}}</p>
    </div>
  `,
  styles: [`
    .link-demo {
      padding: 20px;
    }
    a {
      color: #007bff;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  `]
})
export class HrefBindingComponent {
  linkUrl = 'https://angular.io';
  linkText = 'Angular公式サイト';
}
```

// 動的なリンク生成
```typescript
@Component({
  selector: 'app-dynamic-link',
  standalone: true,
  template: `
    <div class="dynamic-demo">
      <h2>動的なリンク生成</h2>
      <a [href]="getProfileLink()" target="_blank">
        プロフィールを見る
      </a>
      <br>
      <a [href]="getProductLink(productId)">
        商品詳細: {{productName}}
      </a>
    </div>
  `,
  styles: [`
    .dynamic-demo {
      padding: 20px;
    }
    a {
      display: block;
      margin: 10px 0;
      color: #28a745;
    }
  `]
})
export class DynamicLinkComponent {
  userId = '12345';
  productId = 'abc-789';
  productName = 'Angular本';
  
  getProfileLink(): string {
    return `https://example.com/profile/${this.userId}`;
  }
  
  getProductLink(id: string): string {
    return `/products/${id}`;
  }
}
```

// 条件付きリンク
```typescript
@Component({
  selector: 'app-conditional-link',
  standalone: true,
  template: `
    <div class="conditional-demo">
      <h2>条件付きリンク</h2>
      <a [href]="isLoggedIn ? '/dashboard' : '/login'">
        {{isLoggedIn ? 'ダッシュボード' : 'ログイン'}}
      </a>
      <br>
      <a [href]="hasPermission ? '/admin' : '#'" 
         [class.disabled]="!hasPermission">
        管理画面
      </a>
    </div>
  `,
  styles: [`
    .conditional-demo {
      padding: 20px;
    }
    a {
      display: block;
      margin: 10px 0;
      color: #007bff;
    }
    a.disabled {
      color: #6c757d;
      cursor: not-allowed;
    }
  `]
})
export class ConditionalLinkComponent {
  isLoggedIn = false;
  hasPermission = true;
}
```
