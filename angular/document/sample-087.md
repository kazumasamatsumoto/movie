# #087 「Lifecycle とSignals の組み合わせ」

## 概要
Lifecycle HooksとAngular Signalsを組み合わせて、状態初期化・副作用・解放処理をシンプルに構成する方法を学びます。

## 学習目標
- `ngOnInit`でSignalを初期化し、親からのInputと同期させる
- `effect`をLifecycleに合わせて開始・停止する
- `DestroyRef`とSignalsを組み合わせた安全なクリーンアップを実装する

## 技術ポイント
- **Signal初期化**: `signal()`で状態を宣言し、Lifecycleで値を設定
- **effect**: `effect(() => {...})`で副作用を定義し、`DestroyRef`で解放
- **input()**: 親からの値をSignal化する新API（v16+）

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
name = signal('めたん');
```

```typescript
effect(() => console.log(this.name()), { scope: destroyRef });
```

```typescript
@Input({ transform: toSignal }) score!: Signal<number>;
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DestroyRef, Input, OnInit, effect, inject, signal } from '@angular/core';

@Component({
  selector: 'app-signal-lifecycle',
  standalone: true,
  templateUrl: './signal-lifecycle.component.html',
})
export class SignalLifecycleComponent implements OnInit {
  @Input({ required: true }) initialName = 'Angular';
  private readonly destroyRef = inject(DestroyRef);
  readonly name = signal('');
  readonly length = signal(0);

  ngOnInit(): void {
    this.name.set(this.initialName);
    this.length.set(this.initialName.length);

    effect(
      () => {
        const value = this.name();
        this.length.set(value.length);
      },
      { scope: this.destroyRef },
    );
  }
}
```

```html
<label>
  名前
  <input [value]="name()" (input)="name.set($any($event.target).value)" />
</label>
<p>文字数: {{ length() }}</p>
```

## ベストプラクティス
- `DestroyRef`を使ってeffectやObservable購読をLifecycleに合わせて自動解放する
- InputからSignalへ変換する場合は`toSignal` / `input()`を使うと`ngOnChanges`が不要になる
- 副作用内でSignalを更新するときはループしないように注意し、必要なら条件を入れる

## 注意点
- effect内でDOM操作を行う場合は実行タイミングを考慮し、`ngAfterViewInit`内でeffectを登録する
- Signalのsetを`ngAfterViewChecked`など高頻度フックで行うと無限ループのリスクがある
- `input()`デコレータはAngular v17+の機能。バージョンに合わせて使い分ける

## 関連技術
- Angular Signals API (`signal`, `computed`, `effect`)
- `DestroyRef.onDestroy`
- `toSignal`, `toObservable`ユーティリティ
