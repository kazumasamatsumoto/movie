# #405 「@Output EventEmitter vs SignalOutput あなたはどっち派？」

## 概要
EventEmitterは成熟しているが手動購読や型安全性に課題がある。SignalOutputは宣言的にイベントを表現し、Signalsグラフへ統合できるため新規アプリに向く。

## 学習目標
- EventEmitterの構成と得意なシナリオを整理する
- SignalOutputの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- EventEmitterを成り立たせる主要API/構成要素
- SignalOutputで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**EventEmitter派：従来の親子通信**
```typescript
@Output() result = new EventEmitter<number>();

calc() {
  this.result.emit(this.value * 2);
}

<child (result)="onResult($event)" />
```

**SignalOutput派：signal()グラフに統合**
```typescript
result = output<number>();

calc() {
  this.result.emit(this.value() * 2);
}

<child (result)="resultSignal.set($event)" />
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-child',
  standalone: true,
  template: `<button (click)="notify()">Send</button>`,
})
export class ChildComponent {
  readonly count = signal(0);
  readonly result = output<number>();

  notify(): void {
    this.count.update(v => v + 1);
    this.result.emit(this.count());
  }
}
```

## ベストプラクティス
- 幅広い互換性が必要な共有コンポーネントはEventEmitterを維持し、アプリ固有部分からSignalOutputを導入する
- SignalOutputを使う際は親側もSignalベースで受け取り、`effect`や`computed`に組み込む
- EventEmitterでも`takeUntilDestroyed`を使って購読解除をシステム化する

## 注意点
- SignalOutputはAngular v17+限定なのでバージョン条件を満たしているか確認する
- SignalとRxJSの境界で同一イベントを二重に処理しないように整理する
- EventEmitterの`async`フラグなど独自機能はSignalOutputに存在しないため挙動差を把握する

## 関連技術
- EventEmitter
- SignalOutput API
- Angular Signals
