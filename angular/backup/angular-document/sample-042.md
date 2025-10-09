# #042 「(click) クリックイベント」

## 概要
Angular v20で最も頻繁に利用する(click)イベントバインディングを使い、クリック操作からコンポーネントのメソッドを呼び出す方法を学びます。

## 学習目標
- (click) イベントバインディングの基本構文を習得する
- 引数付きのメソッド呼び出しパターンを理解する
- シグナルや状態更新と組み合わせてクリック処理を整理する

## 技術ポイント
- **(click) イベント**: DOMのclickイベントをAngular式に接続
- **イベント引数**: `(click)="do(item)"` のようにテンプレートから値を渡す
- **テンプレートの簡潔性**: 処理はメソッドに切り出し、式は短く保つ

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<button (click)="like()">いいね！</button>
```

```html
<button (click)="select(plan)" *ngFor="let plan of plans">
  {{ plan.label }}
</button>
```

```html
<a (click)="toggle()" role="button">詳細を表示</a>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';

type Plan = { id: number; label: string };

@Component({
  selector: 'app-click-demo',
  standalone: true,
  templateUrl: './click-demo.component.html',
})
export class ClickDemoComponent {
  likes = signal(0);
  activePlan = signal<Plan | null>(null);
  plans = signal<Plan[]>([
    { id: 1, label: 'Basic' },
    { id: 2, label: 'Pro' },
    { id: 3, label: 'Enterprise' },
  ]);

  planLabel = computed(() => this.activePlan()?.label ?? '未選択');

  like(): void {
    this.likes.update((count) => count + 1);
  }

  select(plan: Plan): void {
    this.activePlan.set(plan);
  }

  toggle(): void {
    this.activePlan.update((value) => (value ? null : this.plans()[0]));
  }
}
```

```html
<section>
  <p>いいね数: {{ likes() }}</p>
  <button (click)="like()">いいね！</button>
</section>

<section>
  <h3>プラン選択: {{ planLabel() }}</h3>
  <button
    (click)="select(plan)"
    *ngFor="let plan of plans(); track plan.id"
  >
    {{ plan.label }}
  </button>
</section>

<section>
  <a (click)="toggle()" role="button">最初のプランをトグル</a>
</section>
```

## ベストプラクティス
- クリック時のロジックはメソッドに集約し、テンプレートは宣言的に保つ
- ボタン要素を優先し、リンクをボタンに変える場合はARIA属性を付与する
- SignalやRxJSと組み合わせて副作用の境界を明確にする

## 注意点
- `<a>`タグのclickで遷移を止める場合は`.preventDefault()`などを忘れない
- 複数ボタンをループ表示する際は`track`句で描画効率を確保する
- 同期処理で重いロジックを実行するとUIが固まるので非同期化を検討する

## 関連技術
- Templateの繰り返し構文 `@for` / `*ngFor`
- Angular Signals とcomputed
- HostListenerによるイベント処理
