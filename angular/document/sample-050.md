# #050 「イベント修飾子 - .preventDefault()」

## 概要
Angular v20で利用できるイベント修飾子`.preventDefault()`を使い、テンプレート内から既定動作を抑止して明確な意図でイベントを処理する方法を学びます。

## 学習目標
- イベント修飾子の役割と構文を理解する
- `.preventDefault()`でSPA向けにリンクやフォーム送信を制御する
- 修飾子と通常のイベントロジックを組み合わせて可読性を高める

## 技術ポイント
- **イベント修飾子**: `(event.modifier)="..."` 形式で追加動作を宣言
- **preventDefault**: DOM既定挙動をテンプレート宣言だけで抑止
- **複合記述**: `.stopPropagation()`など他修飾子と併用して意図を明示

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<a href="/profile" (click.preventDefault)="openModal()">プロフィール</a>
```

```html
<form (submit.preventDefault)="save()">保存</form>
```

```html
<button (click.preventDefault.stop)="noop()">押しても遷移しない</button>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-prevent-default-demo',
  standalone: true,
  templateUrl: './prevent-default-demo.component.html',
})
export class PreventDefaultDemoComponent {
  modalOpen = signal(false);
  lastAction = signal('');

  openProfileModal(): void {
    this.modalOpen.set(true);
    this.lastAction.set('プロフィールモーダルを開きました');
  }

  saveForm(): void {
    this.lastAction.set('フォーム内容を保存しました');
  }

  close(): void {
    this.modalOpen.set(false);
  }
}
```

```html
<a href="/profile" (click.preventDefault)="openProfileModal()">
  プロフィールを表示
</a>

<form (submit.preventDefault)="saveForm()">
  <input placeholder="ニックネーム" />
  <button type="submit">保存</button>
</form>

<dialog *ngIf="modalOpen()">
  <p>SPA内でプロフィール編集ビューを表示します。</p>
  <button type="button" (click)="close()">閉じる</button>
</dialog>

<p>直近の処理: {{ lastAction() }}</p>
```

## ベストプラクティス
- 修飾子を使うときはテンプレート内で意図が明確になるよう命名を合わせる
- SPAでリンククリックを横取りするときは`role="button"`や`tabindex`を適切に設定
- `.preventDefault()`と`.stopPropagation()`の併用でイベントバブリング制御を明示する

## 注意点
- 修飾子はAngularが提供するものに限られるため、存在しない修飾子は使えない
- preventDefaultを多用するとユーザー期待とずれる場合があるのでUI設計を見直す
- ネイティブフォームバリデーションを利用する場合は送信阻害に注意する

## 関連技術
- Angularイベントバインディングとイベントオプション
- SPAでのリンク制御とRouterLink
- `.stopPropagation()`などのイベント修飾子
