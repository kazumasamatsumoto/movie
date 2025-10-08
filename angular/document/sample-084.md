# #084 「Lifecycle のデバッグ方法」

## 概要
Lifecycle Hooksの呼び出しタイミングや順序を可視化し、問題箇所を素早く特定するデバッグテクニックを紹介します。

## 学習目標
- Angular DevToolsやブラウザツールを使ったデバッグ手法を理解する
- Lifecycleごとにログ出力や計測を行う
- 本番前にデバッグコードを除去する運用ルールを整備する

## 技術ポイント
- **Angular DevTools**: Componentsタブでフック呼び出し回数を確認
- **パフォーマンス計測**: `performance.mark()` / `performance.measure()`
- **条件付きログ**: `ngAfterViewChecked`など多頻度のフックでは条件分岐を入れる

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
performance.mark('after-view-init');
```

```typescript
console.log('ngOnInit', this);
```

```typescript
debugger;
```

## 💻 詳細実装例（学習用）
```typescript
import {
  AfterViewChecked,
  AfterViewInit,
  Component,
  OnDestroy,
  OnInit,
} from '@angular/core';

@Component({
  selector: 'app-lifecycle-debug',
  standalone: true,
  templateUrl: './lifecycle-debug.component.html',
})
export class LifecycleDebugComponent
  implements OnInit, AfterViewInit, AfterViewChecked, OnDestroy
{
  private viewCheckedCount = 0;

  ngOnInit(): void {
    console.log('OnInit');
    performance.mark('component-init');
  }

  ngAfterViewInit(): void {
    console.log('AfterViewInit');
    performance.mark('after-view-init');
    performance.measure('init→view', 'component-init', 'after-view-init');
  }

  ngAfterViewChecked(): void {
    this.viewCheckedCount++;
    if (this.viewCheckedCount <= 3) {
      console.log(`AfterViewChecked #${this.viewCheckedCount}`);
    }
  }

  ngOnDestroy(): void {
    console.table(performance.getEntriesByType('measure'));
  }
}
```

```html
<p>Lifecycleの計測結果はコンソールで確認できます。</p>
```

## ベストプラクティス
- ログ出力はマクロ(`debugLifecycle`)として共通化し、開発時のみ有効化する
- Angular DevToolsのProfilerタブで描画回数を確認し、不要なフック呼び出しを削減する
- `console.table`や`performance.measure`で見やすい形に整形する

## 注意点
- `debugger;`を置くと実行が停止するため、チームで共有する際は注意書きを添える
- 本番ビルドではデバッグコードを削除し、`ngOnDestroy`でログをまとめて出す
- 大量ログはブラウザを圧迫するので必要最小限にする

## 関連技術
- Angular DevTools Components/Profiler
- `ng.profiler` (旧DevTools)
- Chrome Performance Panel
