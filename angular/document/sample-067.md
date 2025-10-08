# #067 「ngDoCheck - 変更検知のカスタマイズ」

## 概要
Angularのデフォルト変更検知に追加のロジックを組み込みたいときに利用する`ngDoCheck`フックの活用と注意点を学びます。

## 学習目標
- `ngDoCheck`の呼び出しタイミングと頻度を理解する
- `KeyValueDiffers`や`IterableDiffers`と組み合わせて差分検出する
- パフォーマンス影響を最小限に抑えた実装パターンを適用する

## 技術ポイント
- **ngDoCheck**: 変更検知サイクルごとに呼ばれるカスタム検知フック
- **Differs API**: 差分検出サービスでコストを抑える
- **条件分岐**: `if (!dirty) return;` で不要な処理を避ける

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
constructor(private readonly differs: KeyValueDiffers) {}
```

```typescript
ngDoCheck(): void {
  const diff = this.differ.diff(this.settings);
}
```

```typescript
if (diff) { /* 差分に応じて処理 */ }
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DoCheck, KeyValueDiffers } from '@angular/core';

type Settings = { theme: string; language: string; notifications: boolean };

@Component({
  selector: 'app-settings-watch',
  standalone: true,
  templateUrl: './settings-watch.component.html',
})
export class SettingsWatchComponent implements DoCheck {
  settings: Settings = { theme: 'light', language: 'ja', notifications: true };
  logs: string[] = [];

  private readonly differ = this.differs.find(this.settings).create<Settings>();

  constructor(private readonly differs: KeyValueDiffers) {}

  ngDoCheck(): void {
    const changes = this.differ.diff(this.settings);
    if (!changes) {
      return;
    }

    changes.forEachChangedItem((record) => {
      this.logs.push(
        `${record.key}: ${record.previousValue} → ${record.currentValue}`,
      );
    });
  }

  toggleTheme(): void {
    this.settings = {
      ...this.settings,
      theme: this.settings.theme === 'light' ? 'dark' : 'light',
    };
  }
}
```

```html
<button type="button" (click)="toggleTheme()">テーマ切替</button>
<ul>
  <li @for (log of logs; track log)>{{ log }}</li>
</ul>
```

## ベストプラクティス
- `ngDoCheck`は最後の手段として利用し、まずSignalsや`OnPush`で解決できないか検討する
- 差分検出にはDiffers APIを使い、手動で深い比較を行わない
- 重い処理はスロットリングや条件分岐で最小化する

## 注意点
- 毎回の検知で呼ばれるため、`console.log`などでも大量に出力されパフォーマンスが低下する
- `ngDoCheck`内で状態を同期的に変更すると無限ループになる可能性がある
- テスト時は変更検知を手動で走らせて挙動を確認する必要がある

## 関連技術
- `IterableDiffers`による配列差分検出
- Signalsでの変更追跡
- ChangeDetectionStrategy.OnPush
