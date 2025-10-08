# #082 「Lifecycle でのイベントリスナー登録」

## 概要
ブラウザイベントやカスタムイベントのリスナーをLifecycle Hooksを使って登録・解除し、リークなく運用する方法を学びます。

## 学習目標
- イベントリスナーを登録する最適なタイミングを理解する
- `ngOnDestroy`で解除を徹底する
- `HostListener`と手動登録の使い分けを把握する

## 技術ポイント
- **登録タイミング**: `ngOnInit`または`ngAfterViewInit`
- **解除**: `removeEventListener`、Renderer2の戻り値、`AbortController`
- **HostListener**: デコレータを使うと自動で解除される

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnInit() {
  window.addEventListener('resize', this.onResize);
}
```

```typescript
ngOnDestroy() {
  window.removeEventListener('resize', this.onResize);
}
```

```typescript
@HostListener('document:visibilitychange')
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, HostListener, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-listener-manager',
  standalone: true,
  templateUrl: './listener-manager.component.html',
})
export class ListenerManagerComponent implements OnInit, OnDestroy {
  size = { width: window.innerWidth, height: window.innerHeight };
  private readonly onResize = () => {
    this.size = { width: window.innerWidth, height: window.innerHeight };
  };

  ngOnInit(): void {
    window.addEventListener('resize', this.onResize);
  }

  ngOnDestroy(): void {
    window.removeEventListener('resize', this.onResize);
  }

  @HostListener('document:visibilitychange')
  onVisibilityChange(): void {
    console.log('visibility', document.visibilityState);
  }
}
```

```html
<p>幅: {{ size.width }} / 高さ: {{ size.height }}</p>
```

## ベストプラクティス
- 登録時に使うコールバックはクラスプロパティとして定義し、解除時に同じ参照を渡せるようにする
- Renderer2の`listen`を利用すると解除用関数が返るため、`ngOnDestroy`で実行すれば漏れない
- `HostListener`はテンプレートがシンプルな場合に便利だが、複雑なロジックは手動登録を検討する

## 注意点
- SSRやWeb Workerでは`window`や`document`が存在しないため、実行前にプラットフォームチェックが必要
- `addEventListener`で`passive`オプションを適切に設定し、スクロール性能を確保する
- `HostListener`は破棄時に自動解除されるが、外部リソースには対応しない点に注意

## 関連技術
- Renderer2 `.listen`
- `DestroyRef.onDestroy` で解除関数を登録
- RxJS `fromEvent` + `takeUntilDestroyed`
