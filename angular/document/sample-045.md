# #045 「(submit) フォーム送信イベント」

## 概要
フォーム送信を契機にロジックを実行する( submit )イベントを利用し、SPAらしくブラウザ標準の送信を制御しながらAPI処理へつなげる方法を整理します。

## 学習目標
- (submit) イベントの発火と`event.preventDefault()`による送信抑制を理解する
- フォームから入力値をまとめて取得する基本パターンを学ぶ
- 非同期処理やバリデーションを送信タイミングに組み込む

## 技術ポイント
- **(submit) イベント**: form要素でEnterキーや送信ボタンをトリガーに発火
- **preventDefault**: 既定のページ遷移を抑止し、独自ロジックへ切り替える
- **フォームの取り扱い**: Template reference variablesやFormGroupで値を取得

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<form (submit)="onSubmit($event)">
  <input name="email" required />
  <button type="submit">登録</button>
</form>
```

```html
<form (submit)="saveProfile(profileForm, $event)" #profileForm="ngForm">
  <!-- fields -->
</form>
```

```html
<button type="submit" form="contactForm">送信</button>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

interface ContactRequest {
  name: string;
  email: string;
  message: string;
}

@Component({
  selector: 'app-submit-demo',
  standalone: true,
  templateUrl: './submit-demo.component.html',
})
export class SubmitDemoComponent {
  status = signal<'idle' | 'sending' | 'done' | 'error'>('idle');

  async onSubmit(event: Event): Promise<void> {
    event.preventDefault();
    const form = event.target as HTMLFormElement;
    const formData = new FormData(form);
    const payload: ContactRequest = {
      name: String(formData.get('name') ?? ''),
      email: String(formData.get('email') ?? ''),
      message: String(formData.get('message') ?? ''),
    };

    if (!payload.email || !payload.message) {
      this.status.set('error');
      return;
    }

    this.status.set('sending');
    try {
      await fakeSend(payload);
      this.status.set('done');
      form.reset();
    } catch {
      this.status.set('error');
    }
  }
}

async function fakeSend(_payload: ContactRequest): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, 800));
}
```

```html
<form (submit)="onSubmit($event)">
  <label>
    お名前
    <input name="name" autocomplete="name" />
  </label>
  <label>
    メール
    <input name="email" type="email" required />
  </label>
  <label>
    メッセージ
    <textarea name="message" rows="3" required></textarea>
  </label>
  <button type="submit" [disabled]="status() === 'sending'">送信</button>
</form>
<p>状態: {{ status() }}</p>
```

## ベストプラクティス
- 送信前に必須入力チェックや形式検証を行い、ユーザーにフィードバックする
- 非同期処理中はローディング表示や重複送信防止ロジックを導入する
- 入力値の正規化やトリミングをコンポーネント側で実施しサーバー負荷を軽減する

## 注意点
- 送信ボタンがフォーム外にある場合は`form`属性で紐付ける必要がある
- ファイルアップロードなど`FormData`が必要なケースではContent-Type設定に注意
- HTML5検証を併用する際は`novalidate`属性やカスタムメッセージを適切に調整する

## 関連技術
- Angular Forms（Reactive Forms / Template-driven Forms）
- fetch API や HttpClient でのAPI通信
- フォームバリデーション戦略
