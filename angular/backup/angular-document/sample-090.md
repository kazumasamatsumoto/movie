# #090 「Lifecycle のアンチパターン」

## 概要
Lifecycle Hooksの誤った使い方で発生するアンチパターンを紹介し、避けるべき設計と正しい代替策を学びます。

## 学習目標
- constructorでロジックを実行するなどの代表的なアンチパターンを把握する
- `ngDoCheck`乱用やクリーンアップ漏れの危険性を理解する
- 代替手段や改善策を適用できるようにする

## 技術ポイント
- **constructor利用の誤り**: DI以外の処理を置くとテスト困難・順序不整合
- **ngDoCheck乱用**: 高頻度フックに重い処理を入れると性能劣化
- **クリーンアップ忘れ**: `ngOnDestroy`未実装でメモリリーク
- **双方向変更**: フック内で無条件にSignalを更新し無限ループ


```typescript
constructor() {
  // ❌ API呼び出しなどの重い処理
}
```

```typescript
ngDoCheck() {
  // ❌ 重い計算を毎回実行
}
```

```typescript
ngOnDestroy() {
  // ❌ 何もしない -> 資源が残る
}
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DoCheck, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-anti-pattern',
  standalone: true,
  templateUrl: './anti-pattern.component.html',
})
export class AntiPatternComponent implements OnInit, DoCheck, OnDestroy {
  private expensive = 0;
  private readonly data: number[] = Array.from({ length: 5000 }, (_, i) => i);

  constructor() {
    // ❌ アンチパターン: constructorでロジックを実行
    console.log('constructorでAPI呼び出し');
  }

  ngOnInit(): void {
    console.log('ngOnInit should initialize state only');
  }

  ngDoCheck(): void {
    // ❌ アンチパターン: 毎回重い処理
    this.expensive = this.data.reduce((sum, value) => sum + value, 0);
  }

  ngOnDestroy(): void {
    // ❌ アンチパターン: クリーンアップしない
  }
}
```

```html
<p>アンチパターンの例。constructorやngDoCheckに注意。</p>
```

## ベストプラクティス
- constructorをDI専用とし、ロジックは`ngOnInit`以降の適切なフックへ移す
- 重い処理はSignalsや`computed`でメモ化し、`ngDoCheck`を使わない設計を優先する
- サービスや`DestroyRef`でクリーンアップを必ず実装し、リークを防ぐ
- フック内で状態を更新する場合は条件を設けて無限ループを回避する

## 注意点
- アンチパターン例は理解のために示しているだけであり、実運用では避ける
- パフォーマンス問題が顕在化する前にProfilerで監視する
- リファクタリング時は既存のアンチパターンがないかチェックリスト化する

## 関連技術
- Signalsと`computed`での最適化
- ChangeDetectionStrategy.OnPush
- Angular Style Guideのアンチパターン項目
