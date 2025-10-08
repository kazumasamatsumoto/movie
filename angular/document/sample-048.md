# #048 「(focus) / (blur) フォーカスイベント」

## 概要
フォーム要素へのフォーカス移動と離脱を検出する(focus)/(blur)イベントを利用し、ユーザーの注意に応じたUIガイダンスを実装します。

## 学習目標
- (focus) と (blur) の発火タイミングと扱い方を理解する
- フォーカスに応じてヒントやバリデーションメッセージを切り替える
- アクセシビリティを意識したフォーカス管理を学ぶ

## 技術ポイント
- **フォーカスイベント**: フォーム要素やボタンに対してフォーカス出入りを検知
- **テンプレート組み合わせ**: 同一要素に複数イベントを並べて記述可能
- **アクセシブル構成**: ヒント表示時はARIA属性で読み上げを支援

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<input (focus)="showHint()" (blur)="hideHint()" placeholder="ユーザー名" />
```

```html
<input (focus)="highlight = true" (blur)="highlight = false" />
```

```html
<textarea (focus)="selectAll($event)" rows="3"></textarea>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-focus-blur-demo',
  standalone: true,
  templateUrl: './focus-blur-demo.component.html',
})
export class FocusBlurDemoComponent {
  hintVisible = signal(false);
  isFocused = signal(false);
  message = signal('');

  showHint(): void {
    this.hintVisible.set(true);
    this.isFocused.set(true);
  }

  hideHint(): void {
    this.hintVisible.set(false);
    this.isFocused.set(false);
  }

  selectAll(event: FocusEvent): void {
    const target = event.target as HTMLTextAreaElement;
    setTimeout(() => target.select());
  }

  updateMessage(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.message.set(input.value);
  }
}
```

```html
<label>
  メールアドレス
  <input
    type="email"
    (focus)="showHint()"
    (blur)="hideHint()"
    (input)="updateMessage($event)"
    [attr.aria-describedby]="hintVisible() ? 'email-hint' : null"
  />
</label>
<p id="email-hint" *ngIf="hintVisible()">
  会社ドメインで登録してください
</p>
<p>入力中の値: {{ message() }}</p>

<textarea
  rows="3"
  (focus)="selectAll($event)"
  (blur)="hideHint()"
>Angular Signals make state simple.</textarea>
<p>フォーカス状態: {{ isFocused() ? 'ON' : 'OFF' }}</p>
```

## ベストプラクティス
- ヒント表示はフォーカス時に限り、視認性と読み上げの両方をカバーする
- フォーカス制御はTemplate参照や`focus()`メソッドと組み合わせて設計する
- 共有状態はSignalで管理し、複数フィールドでも一貫したUIにする

## 注意点
- (blur)は要素からフォーカスが完全に離れたときのみ発火する
- マウス押下中はフォーカス移動が確定しない場合があるためタイミングに注意
- タッチデバイスではフォーカス操作が異なる場合があるので実機で検証する

## 関連技術
- フォームアクセシビリティ（ARIA属性）
- Angularのテンプレートリファレンス変数（#input）
- Reactive Formsのフォーカス管理
