# #140 「ViewChild でメソッド呼び出し」

## 概要
親コンポーネントが`@ViewChild`で子コンポーネントを取得し、子が公開するメソッドを呼び出すパターンを学びます。

## 学習目標
- 親から子コンポーネントのメソッドを呼び出す手順を理解する
- ライフサイクルに応じた呼び出しタイミングを把握する
- 密結合を避けるための公開API設計を意識する

## 技術ポイント
- **ViewChildで子取得**: `@ViewChild(ChildComponent) child?: ChildComponent;`
- **公開メソッド**: 子コンポーネントでpublicメソッドを用意
- **呼び出しタイミング**: `ngAfterViewInit`以降、またはイベント発生時

```typescript
@ViewChild(PlayerComponent)
player?: PlayerComponent;
```

```typescript
this.player?.play();
```

```html
<app-player></app-player>
<button (click)="player?.pause()">停止</button>
```

## 💻 詳細実装例（学習用）
```typescript
// player.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-player',
  standalone: true,
  template: `
    <p>再生状態: {{ playing ? '再生中' : '停止' }}</p>
  `,
})
export class PlayerComponent {
  playing = false;

  play(): void {
    this.playing = true;
  }

  pause(): void {
    this.playing = false;
  }
}
```

```typescript
// parent.component.ts
import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { PlayerComponent } from './player.component';

@Component({
  selector: 'app-player-container',
  standalone: true,
  imports: [PlayerComponent],
  templateUrl: './player-container.component.html',
})
export class PlayerContainerComponent implements AfterViewInit {
  @ViewChild(PlayerComponent)
  player?: PlayerComponent;

  ngAfterViewInit(): void {
    this.player?.play();
  }

  toggle(): void {
    if (!this.player) {
      return;
    }
    this.player.playing ? this.player.pause() : this.player.play();
  }
}
```

```html
<!-- player-container.component.html -->
<app-player></app-player>
<button type="button" (click)="toggle()">再生/停止</button>
```

## ベストプラクティス
- 子コンポーネントは親が利用するメソッドのみ公開し、他はprivateにして責務を限定する
- 親→子の直接呼び出しが多くなったらイベント通知や共有サービスへの移行を検討する
- テストでは親コンポーネントを生成し、ViewChild参照を通じてメソッドが呼ばれることを検証する

## 注意点
- 子コンポーネントが非表示または破棄されると参照がnullになるので、呼び出し前に確認する
- 双方向依存を避け、子が親へ依存しないよう設計する
- 非同期処理やエラー処理を伴うメソッドを呼ぶ場合は例外ハンドリングを行う

## 関連技術
- `@Output()`イベントを使った親子通信
- `@ViewChildren`で複数子コンポーネントを制御
- `ChangeDetectorRef`での手動検知（子メソッドが同期で状態を変える場合）
