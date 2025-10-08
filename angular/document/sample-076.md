# #076 「Lifecycle Hooks の使い分け」

## 概要
多数のLifecycle Hooksから適切なものを選び、責務を分担してコンポーネントの副作用を整理する方法を解説します。

## 学習目標
- 代表的なフックの役割と使いどころを整理する
- 初期化・変更検知・ビュー操作・破棄をフックごとに使い分ける
- Hooksを必要最小限に抑えた設計指針を身につける

## 技術ポイント
- **初期化系**: `ngOnInit`, `ngAfterContentInit`, `ngAfterViewInit`
- **監視系**: `ngOnChanges`, `ngDoCheck`, `ngAfter*Checked`
- **終了系**: `ngOnDestroy`
- **特殊ケース**: SignalsやRxJSと組み合わせてフックの負担を減らす

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnInit() { this.setup(); }
```

```typescript
ngAfterViewInit() { this.initChart(); }
```

```typescript
ngOnDestroy() { this.cleanup(); }
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild, ElementRef } from '@angular/core';
import { interval, Subscription } from 'rxjs';

@Component({
  selector: 'app-hook-usage',
  standalone: true,
  templateUrl: './hook-usage.component.html',
})
export class HookUsageComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild('canvas') canvas?: ElementRef<HTMLCanvasElement>;
  private subscription?: Subscription;

  ngOnInit(): void {
    this.subscription = interval(1000).subscribe((value) =>
      console.log('Tick', value),
    );
  }

  ngAfterViewInit(): void {
    if (this.canvas) {
      const ctx = this.canvas.nativeElement.getContext('2d');
      ctx?.fillRect(10, 10, 80, 40);
    }
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }
}
```

```html
<canvas #canvas width="120" height="80"></canvas>
```

## ベストプラクティス
- フックを実装するときは「何の責務か」をコメントやメソッド名で明示する
- 変更検知タイミングごとに必要な処理を分類し、不要なフックは実装しない
- SignalsやRxJSを活用して、`ngDoCheck`など重いフックの利用を避ける

## 注意点
- フックを多用しすぎると可読性が低下するため、コンポーネントを分割することも検討
- `ngAfterViewInit`でDOM操作した結果を`ngAfterViewChecked`で再調整しないよう設計する
- `ngOnDestroy`を実装し忘れるとリソースリークの原因になる

## 関連技術
- ChangeDetectionStrategy
- Signalsと`effect`による副作用管理
- Angular Style Guide (Lifecycle Hooksセクション)
