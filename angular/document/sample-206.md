# #206 「コンテンツ投影とライフサイクル」

## 概要
コンテンツ投影がAngularライフサイクルのどの段階で利用可能になるかを理解し、`ngAfterContentInit` / `ngAfterContentChecked` の役割を整理します。

## 学習目標
- `ContentChild`/`ContentChildren`が取得可能になるタイミングを理解する
- 投影コンテンツの変化を監視する方法を把握する
- ViewChildとのライフサイクルの違いを説明できるようになる

## 技術ポイント
- **`ngAfterContentInit`**: 初回のコンテンツ投影が完了した直後に呼ばれる
- **`ngAfterContentChecked`**: 投影コンテンツに変更があった場合に呼び出される
- **`ViewChild`との違い**: Viewは`ngAfterViewInit`で、Contentは`ngAfterContentInit`

## 📺 画面表示用コード（動画用）

```typescript
ngAfterContentInit() { console.log('content initialized'); }
```

```typescript
ngAfterContentChecked() { console.log('content checked'); }
```

```typescript
@ContentChild('header') header?: ElementRef;
```

## 💻 詳細実装例（学習用）
```typescript
// lifecycle-demo.component.ts
import {
  AfterContentChecked,
  AfterContentInit,
  Component,
  ContentChild,
  ElementRef,
} from '@angular/core';

@Component({
  selector: 'app-lifecycle-demo',
  standalone: true,
  templateUrl: './lifecycle-demo.component.html',
  styleUrls: ['./lifecycle-demo.component.scss'],
})
export class LifecycleDemoComponent implements AfterContentInit, AfterContentChecked {
  @ContentChild('header')
  header?: ElementRef<HTMLHeadingElement>;

  initialized = false;
  changeCount = 0;

  ngAfterContentInit(): void {
    this.initialized = !!this.header;
  }

  ngAfterContentChecked(): void {
    this.changeCount++;
  }
}
```

```html
<!-- lifecycle-demo.component.html -->
<div class="lifecycle">
  <p>初期化済み: {{ initialized }}</p>
  <p>チェック回数: {{ changeCount }}</p>
  <ng-content></ng-content>
</div>
```

## ベストプラクティス
- 投影コンテンツに依存する初期化処理は`ngAfterContentInit`で行う
- 変更が頻繁に起こる場合、`ngAfterContentChecked`で重い処理を行わず、`changes` Observableを活用する
- ViewとContentのライフサイクル差異を把握し、`ngAfterViewInit`と混同しない

## 注意点
- `ngAfterContentChecked`は頻繁に呼び出されるため、ログ出力や重い計算を避ける
- 投影コンテンツが`*ngIf`などで非同期に準備される場合、値がnullになる期間に備える
- `ContentChild`参照を外部へ公開する場合はnullチェックを徹底する

## 関連技術
- `ContentChild` / `ContentChildren`
- Viewライフサイクル（`ngAfterViewInit`, `ngAfterViewChecked`）
- QueryListの`changes` Observable


