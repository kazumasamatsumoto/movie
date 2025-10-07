# #033 「{{ }} 安全な補間 - XSS対策」

## 概要
Angularの補間バインディングは、デフォルトでHTMLエスケープを行い、XSS（クロスサイトスクリプティング）攻撃から自動的に保護します。ユーザー入力などの信頼できないデータを安全に表示できます。

## 学習目標
- 補間バインディングの自動エスケープ機能を理解する
- XSS攻撃のリスクと対策を学ぶ
- 安全なデータ表示の実装方法を習得する

## 技術ポイント
- 自動HTMLエスケープ
- XSS攻撃の防止
- 信頼できないデータの安全な表示
- サニタイゼーション機能

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class CommentComponent {
  userInput = '<script>alert("XSS")</script>';
}
```

```html
<!-- 安全に表示（エスケープされる） -->
<p>{{userInput}}</p>
<!-- 表示結果: <script>alert("XSS")</script> -->
```

```html
<!-- 危険な例（使わない） -->
<div [innerHTML]="userInput"></div>
```

## 💻 詳細実装例（学習用）

```typescript
// safe-display.component.ts
import { Component } from '@angular/core';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Component({
  selector: 'app-safe-display',
  standalone: true,
  template: `
    <div class="examples">
      <h2>補間の安全性デモ</h2>

      <!-- 安全な補間（自動エスケープ） -->
      <h3>安全な表示（推奨）</h3>
      <div class="safe">
        <p>入力: {{dangerousInput}}</p>
        <p>コメント: {{userComment}}</p>
        <p>タグ付き: {{htmlContent}}</p>
      </div>

      <!-- エスケープの動作確認 -->
      <h3>エスケープされた内容</h3>
      <div class="escaped">
        {{scriptTag}}
        {{imgTag}}
        {{linkTag}}
      </div>

      <!-- 信頼できるHTMLを表示する場合（要注意） -->
      <h3>サニタイズ済みHTML（特殊用途）</h3>
      <div [innerHTML]="trustedHtml"></div>
    </div>
  `,
  styles: [`
    .examples { padding: 20px; }
    .safe, .escaped {
      margin: 10px 0;
      padding: 10px;
      background: #f0f0f0;
      border-radius: 4px;
    }
  `]
})
export class SafeDisplayComponent {
  // 危険な入力例
  dangerousInput = '<script>alert("攻撃")</script>';
  userComment = '<img src=x onerror="alert(1)">';
  htmlContent = '<b>太字</b><i>斜体</i>';

  scriptTag = '<script>console.log("実行されない")</script>';
  imgTag = '<img src="evil.jpg" onerror="alert(\'XSS\')">';
  linkTag = '<a href="javascript:alert(\'XSS\')">リンク</a>';

  // DOMサニタイザーで信頼できるHTMLとしてマーク
  trustedHtml: SafeHtml;

  constructor(private sanitizer: DomSanitizer) {
    // 管理者が作成した安全なHTMLのみこの方法を使用
    const adminContent = '<p style="color: blue;">これは<b>安全な</b>HTMLです</p>';
    this.trustedHtml = this.sanitizer.sanitize(1, adminContent) || '';
  }
}
```

### 比較例：安全 vs 危険

```typescript
// 安全な実装
@Component({
  template: `
    <!-- ✅ 推奨: 自動エスケープ -->
    <p>{{userInput}}</p>

    <!-- ✅ 推奨: パイプでサニタイズ -->
    <p>{{userInput | sanitize}}</p>
  `
})
export class SafeComponent {
  userInput = '<script>alert("XSS")</script>';
}

// 危険な実装（避けるべき）
@Component({
  template: `
    <!-- ❌ 危険: 生のHTML挿入 -->
    <div [innerHTML]="userInput"></div>

    <!-- ❌ 危険: バイパス -->
    <div [innerHTML]="bypassedHtml"></div>
  `
})
export class UnsafeComponent {
  userInput = '<script>alert("XSS")</script>';
  bypassedHtml: SafeHtml;

  constructor(private sanitizer: DomSanitizer) {
    // 信頼できないデータには絶対に使わない
    this.bypassedHtml = this.sanitizer.bypassSecurityTrustHtml(this.userInput);
  }
}
```

## ベストプラクティス
- ユーザー入力は常に補間`{{ }}`で表示する
- HTMLを表示する必要がある場合は十分にサニタイズする
- `bypassSecurityTrust*`メソッドは慎重に使用する
- 信頼できるデータソースのみでinnerHTMLを使用する

## 注意点
- `[innerHTML]`を使う場合は必ずサニタイズする
- ユーザー入力を`bypassSecurityTrustHtml`で処理しない
- スクリプトタグだけでなく、イベントハンドラも危険
- URLやスタイルにも同様のリスクがある

## 関連技術
- DomSanitizer
- SecurityContext
- Sanitization Pipe
- Content Security Policy (CSP)
