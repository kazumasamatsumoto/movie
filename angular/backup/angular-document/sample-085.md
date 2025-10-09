# #085 「Lifecycle のよくあるエラー」

## 概要
Lifecycle Hooksに関係する代表的なエラーメッセージと原因・対処法を紹介し、症状から素早く問題を突き止めます。

## 学習目標
- `ExpressionChangedAfterItHasBeenChecked`などの定番エラーを理解する
- ViewChildのundefinedや`NG0100`などの解決策を把握する
- エラーの再発防止策をLifecycle設計に取り入れる

## 技術ポイント
- **ExpressionChangedAfterItHasBeenChecked**: フック内で同期的に値を変更したケース
- **ViewChild undefined**: `ngAfterViewInit`より前に参照している
- **NG0303**: 必要モジュール未登録でバインディングできない（Lifecycle内での利用に注意）


```typescript
setTimeout(() => this.value = true);
```

```typescript
@ViewChild('panel') panel?: ElementRef;
```

```typescript
if (!this.panel) { console.warn('ViewChild not ready'); }
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-lifecycle-errors',
  standalone: true,
  templateUrl: './lifecycle-errors.component.html',
})
export class LifecycleErrorsComponent implements OnInit, AfterViewInit {
  @ViewChild('input') input?: ElementRef<HTMLInputElement>;
  value = 'initial';

  ngOnInit(): void {
    // ExpressionChangedAfterItHasBeenChecked対策: setTimeoutで次フレームへ
    setTimeout(() => {
      this.value = 'initialized';
    }, 0);
  }

  ngAfterViewInit(): void {
    if (!this.input) {
      console.error('input ViewChildが取得できません');
    }
  }
}
```

```html
<input #input [value]="value" />
```

## ベストプラクティス
- 初期化フックで値を変更する必要がある場合は`setTimeout`や`ChangeDetectorRef.detectChanges`を使用する
- ViewChildをオプショナルにし、参照が取得できたかガードしてから利用する
- エラーメッセージとLifecycleログをセットで確認し、原因のタイミングを把握する

## 注意点
- `setTimeout`対策は最終手段。根本的には初期化タイミングを見直す
- `detectChanges`の多用はパフォーマンス悪化を招くため慎重に使う
- `ViewChild`で`static: true`を指定すると`ngOnInit`で参照できるが、`ngIf`など動的要素には向かない

## 関連技術
- ChangeDetectorRef
- Angular公式エラーメッセージガイド
- Signalsでの初期化とエラー回避
