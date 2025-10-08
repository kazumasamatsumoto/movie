# #044 「(change) 変更イベント」

## 概要
(change) イベントでフォーカスアウトや選択確定時に発火するタイミングを捉え、フォームの確定処理を実装する方法を学びます。

## 学習目標
- (change) の発火条件と(input)との違いを理解する
- セレクトボックスやチェックボックスの確定処理を実装する
- バリデーションやAPI呼び出しを確定タイミングに合わせて実行する

## 技術ポイント
- **確定後のイベント**: (change)は入力途中ではなく最終的な値変更に反応
- **フォーム制御**: 選択系UIと相性が良く、値確定後に副作用を安全に実行
- **$event.target**: 選択値やchecked状態を取り出しコンポーネント状態へ反映

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<select (change)="choosePlan($any($event.target).value)">
  <option value="basic">Basic</option>
  <option value="pro">Pro</option>
</select>
```

```html
<input type="checkbox" (change)="toggleNewsletter($event)" />
```

```html
<input type="file" (change)="upload($event)" accept="image/*" />
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

type Plan = 'basic' | 'pro' | 'enterprise';

@Component({
  selector: 'app-change-demo',
  standalone: true,
  templateUrl: './change-demo.component.html',
})
export class ChangeDemoComponent {
  selectedPlan = signal<Plan>('basic');
  newsletter = signal(false);
  fileName = signal('');

  choosePlan(plan: string): void {
    this.selectedPlan.set(plan as Plan);
    // サーバーへ確定プランを送信するなどの処理をここで実行
  }

  toggleNewsletter(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.newsletter.set(target.checked);
  }

  upload(event: Event): void {
    const input = event.target as HTMLInputElement;
    const file = input.files?.item(0);
    if (file) {
      this.fileName.set(file.name);
    }
  }
}
```

```html
<section>
  <label>プラン選択</label>
  <select (change)="choosePlan($any($event.target).value)" [value]="selectedPlan()">
    <option value="basic">Basic</option>
    <option value="pro">Pro</option>
    <option value="enterprise">Enterprise</option>
  </select>
  <p>選択中: {{ selectedPlan() }}</p>
</section>

<section>
  <label>
    <input type="checkbox" (change)="toggleNewsletter($event)" [checked]="newsletter()" />
    ニュースレターを購読する
  </label>
</section>

<section>
  <input type="file" (change)="upload($event)" accept="image/*" />
  <p>選択したファイル: {{ fileName() || '未選択' }}</p>
</section>
```

## ベストプラクティス
- 確定操作でのみ必要な副作用は(change)に集約して制御を簡潔に保つ
- イベントから取得した値は型を絞って取り扱いを明確にする
- 連続変更が想定される場合はローディング表示やキャンセル処理を整備する

## 注意点
- (change)はフォーカスを失って初めて発火する要素がある点に注意
- ファイル入力はセキュリティ上、ブラウザが加工した情報しか取得できない
- Checkboxのcheckedは`value`ではなく`checked`プロパティから取得する

## 関連技術
- Reactive Formsの`valueChanges`との比較
- DOMの`change`イベント仕様
- 状態管理と副作用制御（Signals / RxJS）
