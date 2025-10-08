# #059 「テンプレート構文のデバッグ」

## 概要
テンプレート構文で発生する表示不具合やエラーを素早く切り分けるためのデバッグ手法を紹介し、Angular DevToolsや診断用表示の活用方法を学びます。

## 学習目標
- ブラウザコンソールとAngular DevToolsで状態を確認する
- テンプレート内で一時的に値を可視化して原因を特定する
- エラーメッセージやスタックトレースから問題箇所を逆算する

## 技術ポイント
- **Angular DevTools**: ComponentsタブでプロパティやSignalsの値をリアルタイムに確認
- **一時表示**: `{{ value | json }}`や`@if`でデバッグ情報を条件表示
- **Strictモード**: strictTemplatesを有効にすることでビルド時にエラーを捕捉

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<pre class="debug">{{ formValue | json }}</pre>
```

```html
@if (errorMessage()) {
  <p class="error">{{ errorMessage() }}</p>
}
```

```html
<button type="button" (click)="logState()">状態をログ</button>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';
import { JsonPipe, NgIf } from '@angular/common';

@Component({
  selector: 'app-template-debug',
  standalone: true,
  imports: [JsonPipe, NgIf],
  templateUrl: './template-debug.component.html',
  styleUrls: ['./template-debug.component.css'],
})
export class TemplateDebugComponent {
  formValue = signal({ name: '', email: '' });
  errorMessage = signal('');

  update(field: 'name' | 'email', value: string): void {
    this.formValue.update((current) => ({ ...current, [field]: value }));
    if (!value) {
      this.errorMessage.set(`${field}が未入力です`);
    } else {
      this.errorMessage.set('');
    }
  }

  logState(): void {
    console.table(this.formValue());
  }
}
```

```html
<form>
  <label>
    名前
    <input (input)="update('name', $any($event.target).value)" />
  </label>
  <label>
    メール
    <input (input)="update('email', $any($event.target).value)" />
  </label>
</form>

@if (errorMessage()) {
  <p class="error">{{ errorMessage() }}</p>
}

<pre class="debug">{{ formValue() | json }}</pre>

<button type="button" (click)="logState()">状態をログ</button>
```

## ベストプラクティス
- 一時的なデバッグ表示は`debug`クラスを付けて分かりやすくし、原因解明後は忘れず削除する
- Angular DevToolsで問題のコンポーネントを選択し、入力バインディングやSignalsを確認する
- エラー再現手順をメモしユニットテストやE2Eテストに落とし込む

## 注意点
- テンプレートに`console.log`を直接書くとパフォーマンス低下を招くため避ける
- 本番ビルドでデバッグ表示を残さないようCIでlintやStatic analysisを活用する
- エラーがゾーンの外で発生している場合はスタックトレースから手動で追いかける必要がある

## 関連技術
- Angular DevTools Components/Profilerタブ
- strictTemplates とビルド時検証
- Ng probe (`ng.getComponent`) を使ったデバッグ
