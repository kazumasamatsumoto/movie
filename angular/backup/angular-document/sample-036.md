# #036 「[href] リンクバインディング」

## 概要
`[href]`プロパティバインディングは、aタグのhref属性を動的に設定する手法です。コンポーネントのプロパティ値に基づいてリンク先を動的に変更でき、URLパラメータの生成や条件分岐による遷移先の制御が可能になります。

## 学習目標
- [href]バインディングの基本構文を理解する
- 動的なURL生成の方法を学ぶ
- セキュリティ対策とサニタイゼーションを理解する

## 技術ポイント
- `[href]`プロパティバインディング
- 動的なURL生成
- セキュリティ（URLサニタイゼーション）
- クエリパラメータの動的生成

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class LinkComponent {
  externalUrl = 'https://angular.dev';
  userId = 123;
}
```

```html
<!-- リンクバインディング -->
<a [href]="externalUrl">公式サイト</a>
<a [href]="'/user/' + userId">ユーザー詳細</a>
```

```html
<!-- メールリンク -->
<a [href]="'mailto:' + email">メール送信</a>
```

## 💻 詳細実装例（学習用）

```typescript
// dynamic-links.component.ts
import { Component } from '@angular/core';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-dynamic-links',
  standalone: true,
  template: `
    <div class="links">
      <h2>動的リンク例</h2>

      <!-- 基本的なリンクバインディング -->
      <h3>外部リンク</h3>
      <a [href]="officialSite" target="_blank">公式サイト</a>
      <a [href]="documentationUrl" target="_blank">ドキュメント</a>

      <!-- 動的なパス生成 -->
      <h3>動的パス</h3>
      <a [href]="getUserProfileUrl(userId)">ユーザープロフィール</a>
      <a [href]="getProductUrl(productId)">商品詳細</a>

      <!-- クエリパラメータ付きURL -->
      <h3>クエリパラメータ</h3>
      <a [href]="getSearchUrl('Angular', 'tutorial')">検索結果</a>
      <a [href]="getFilterUrl({ category: 'books', sort: 'price' })">フィルタ適用</a>

      <!-- メールとTELリンク -->
      <h3>通信リンク</h3>
      <a [href]="'mailto:' + email">メール送信</a>
      <a [href]="'tel:' + phoneNumber">電話をかける</a>

      <!-- 条件付きリンク -->
      <h3>条件分岐</h3>
      <a [href]="isLoggedIn ? dashboardUrl : loginUrl">
        {{isLoggedIn ? 'ダッシュボード' : 'ログイン'}}
      </a>

      <!-- 安全なURL（サニタイズ） -->
      <h3>外部URL（サニタイズ済み）</h3>
      <a [href]="trustedUrl" target="_blank">信頼できるリンク</a>

      <!-- ダウンロードリンク -->
      <h3>ダウンロード</h3>
      <a [href]="pdfUrl" download="document.pdf">PDFをダウンロード</a>
    </div>
  `,
  styles: [`
    .links {
      padding: 20px;
    }
    h3 {
      margin-top: 20px;
      font-size: 16px;
      color: #333;
    }
    a {
      display: block;
      margin: 8px 0;
      color: #007bff;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  `]
})
export class DynamicLinksComponent {
  // 基本URL
  officialSite = 'https://angular.dev';
  documentationUrl = 'https://angular.dev/docs';

  // 動的パラメータ
  userId = 123;
  productId = 'prod-456';

  // 通信情報
  email = 'support@example.com';
  phoneNumber = '03-1234-5678';

  // 条件分岐
  isLoggedIn = false;
  dashboardUrl = '/dashboard';
  loginUrl = '/login';

  // ダウンロード
  pdfUrl = '/assets/documents/guide.pdf';

  // 信頼できるURL
  trustedUrl: SafeUrl;

  constructor(private sanitizer: DomSanitizer) {
    // 外部URLをサニタイズ
    const externalUrl = 'https://trusted-site.com';
    this.trustedUrl = this.sanitizer.sanitize(4, externalUrl) || '';
  }

  getUserProfileUrl(userId: number): string {
    return `/users/${userId}/profile`;
  }

  getProductUrl(productId: string): string {
    return `/products/${productId}`;
  }

  getSearchUrl(query: string, type: string): string {
    return `/search?q=${encodeURIComponent(query)}&type=${type}`;
  }

  getFilterUrl(filters: { category: string; sort: string }): string {
    const params = new URLSearchParams(filters);
    return `/items?${params.toString()}`;
  }
}
```

### ルーター統合の例

```typescript
// router-links.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-router-links',
  standalone: true,
  template: `
    <!-- Angularルーター使用時は [href] より [routerLink] を推奨 -->
    <nav>
      <!-- ❌ 非推奨: [href] を使うとページリロードが発生 -->
      <a [href]="'/home'">ホーム</a>

      <!-- ✅ 推奨: [routerLink] を使う（SPAのまま遷移） -->
      <a [routerLink]="'/home'">ホーム</a>
      <a [routerLink]="['/user', userId]">ユーザー詳細</a>

      <!-- 外部サイトのみ [href] を使用 -->
      <a [href]="externalUrl" target="_blank">外部サイト</a>
    </nav>
  `
})
export class RouterLinksComponent {
  userId = 123;
  externalUrl = 'https://example.com';
}
```

### URLサニタイゼーションの例

```typescript
// safe-url.component.ts
import { Component } from '@angular/core';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-safe-url',
  template: `
    <!-- 危険なURLのサニタイズ -->
    <a [href]="safeUrl">安全なリンク</a>
  `
})
export class SafeUrlComponent {
  safeUrl: SafeUrl;

  constructor(private sanitizer: DomSanitizer) {
    // ユーザー入力などの信頼できないURLをサニタイズ
    const userInput = 'javascript:alert("XSS")'; // 危険なURL
    this.safeUrl = this.sanitizer.sanitize(4, userInput) || '#';
    // → 'unsafe:javascript:alert("XSS")' に変換され無効化される
  }
}
```

## ベストプラクティス
- 内部遷移にはRouterの`[routerLink]`を使用する（SPAを維持）
- 外部URLのみ`[href]`を使用し、`target="_blank"`を付ける
- ユーザー入力由来のURLは必ずサニタイズする
- クエリパラメータは`encodeURIComponent`でエンコードする
- URLパラメータの生成ロジックはメソッドに分離する

## 注意点
- `[href]`を使うとページがリロードされる（SPAが途切れる）
- `javascript:`などの危険なプロトコルは自動でブロックされる
- 外部リンクには`rel="noopener noreferrer"`を推奨
- メールや電話リンクはモバイルでの動作を確認する

## 関連技術
- RouterLink（SPA内部遷移）
- DomSanitizer（URLサニタイゼーション）
- URLSearchParams（クエリパラメータ生成）
- encodeURIComponent（URL エンコード）
