# #385 「条件付きスタイル適用」

## 概要
条件付きスタイルは、状態に応じて`ngStyle`やクラスを使い分けて視覚的な変化やアクセシビリティ改善を実現するパターンである。

## 学習目標
- 条件付きスタイルを設計するコツを理解する
- 値計算をコンポーネントで行いテンプレートを簡潔にする方法を学ぶ
- スタイル変更とアクセシビリティ属性の連動を把握する

## 技術ポイント
- 状態に応じてスタイルオブジェクトを更新
- Falsy値でスタイルを削除し元の状態へ戻す
- `aria-live`や`role`の設定と合わせて幅広いユーザーに配慮

## 📺 画面表示用コード（動画用）
```html
<div [ngStyle]="{ background: progress > 80 ? '#22c55e' : '#e2e8f0' }">進捗</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-conditional-style-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div
      [ngStyle]="styleByScore()"
      role="status"
      aria-live="polite">
      スコア: {{ score }}%
    </div>
    <button type="button" (click)="increase()">加算</button>
  `
})
export class ConditionalStyleDemoComponent {
  protected score = 40;

  protected styleByScore(): Record<string, string> {
    return {
      background: this.score >= 80 ? '#22c55e' : '#e2e8f0',
      color: this.score >= 80 ? '#fff' : '#0f172a',
      padding: '0.75rem',
      borderRadius: '0.75rem'
    };
  }

  protected increase(): void {
    this.score = Math.min(100, this.score + 10);
  }
}
```

## ベストプラクティス
- 状態が閾値を超えたときなど条件を明示し、複雑な式はメソッドへ抽出
- 視覚的変化と同時にARIAなど音声ユーザーへの配慮を行う
- テストで境界値（79→80など）を確認し意図どおりスタイルが変化するか検証

## 注意点
- 数値比較をテンプレートで直接書くと複雑になるのでメソッドやcomputedで管理
- 色の変化だけに頼らずアイコンやテキストを併用してアクセシブルにする
- アニメーションが必要ならCSSクラスの切り替えを優先し、ngStyleは補助的に

## 関連技術
- Accessibility (ARIA)
- Angular Signals
- Renderer2 / ngClass
