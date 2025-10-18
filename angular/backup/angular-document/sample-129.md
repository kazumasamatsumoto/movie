# #129 「Component 通信のセキュリティ考慮」

## 概要
コンポーネント間通信で扱うデータに対してセキュリティを意識し、XSSや不正入力を防ぐためのポイントを整理します。

## 学習目標
- @Input()経由で渡されるデータのサニタイズ方法を理解する
- @Output()で外部に通知するデータを検証する
- DOM操作やHTML挿入時のセキュリティリスクを把握する

## 技術ポイント
- **DomSanitizer**: 信頼できないHTML/URLを安全に処理
- **型ガード**: イベントで渡すデータに型やバリデーションを適用
- **セキュアなテンプレート**: `[innerHTML]`や`[src]`の取り扱いに注意

```typescript
constructor(private sanitizer: DomSanitizer) {}
```

```typescript
safeHtml = this.sanitizer.
  bypassSecurityTrustHtml(rawHtml);
```

```typescript
@Output() submitted = new EventEmitter<FormData>();
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DomSanitizer, EventEmitter, Input, Output } from '@angular/core';
import { SafeHtml } from '@angular/platform-browser';

type MessagePayload = {
  content: string;
  author: string;
};

@Component({
  selector: 'app-message-viewer',
  standalone: true,
  templateUrl: './message-viewer.component.html',
})
export class MessageViewerComponent {
  private _message: MessagePayload | null = null;
  safeContent: SafeHtml | null = null;

  @Input()
  set message(value: MessagePayload | null) {
    this._message = value;
    if (value) {
      this.safeContent = this.sanitizer.bypassSecurityTrustHtml(
        this.escapeHtml(value.content),
      );
    }
  }
  get message(): MessagePayload | null {
    return this._message;
  }

  @Output() report = new EventEmitter<{ author: string; reason: string }>();

  constructor(private readonly sanitizer: DomSanitizer) {}

  reportSpam(): void {
    if (!this.message) return;
    this.report.emit({ author: this.message.author, reason: 'spam' });
  }

  private escapeHtml(html: string): string {
    return html.replaceAll('<', '&lt;').replaceAll('>', '&gt;');
  }
}
```

```html
<!-- message-viewer.component.html -->
<article *ngIf="message">
  <h4>{{ message.author }}</h4>
  <div [innerHTML]="safeContent"></div>
  <button type="button" (click)="reportSpam()">不適切として報告</button>
</article>
```

## ベストプラクティス
- Inputで受け取ったHTML文字列は信頼できるソースのみを許可し、必要ならDomSanitizerでサニタイズする
- Outputで外部へ通知するデータは型やスキーマを定義し、予期しない値を排除する
- イベントで受け取ったデータをそのままDOM操作に使わない

## 注意点
- `bypassSecurityTrustHtml`は最終手段。可能ならテンプレートでエスケープする
- third partyライブラリから受け取ったデータをそのまま渡す場合はスキーマチェックを行う
- コンポーネント境界で信頼境界が変わる場合はバリデーションとサニタイズを徹底する

## 関連技術
- Angular Securityガイド
- DomSanitizer API
- Zod / Yup などのバリデーションライブラリ
