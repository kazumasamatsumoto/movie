# #417 「attribute バインディング」

## 概要
`@HostBinding('attr.<name>')`は属性値を直接管理でき、ARIA属性やdata属性などをディレクティブで制御するのに適している。

## 学習目標
- 属性バインディングの書式を理解する
- ARIA属性を動的に更新するパターンを学ぶ
- null/undefinedで属性削除が可能なことを把握する

## 技術ポイント
- `@HostBinding('attr.aria-expanded')`
- boolean属性は空文字またはnullで付与/削除
- data属性も`attr.data-state`で制御

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('attr.aria-busy') get ariaBusy(): 'true' | null { return this.loading ? 'true' : null; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAriaBusy]',
  standalone: true
})
export class AriaBusyDirective {
  @Input() loading = false;

  @HostBinding('attr.aria-busy')
  get ariaBusy(): 'true' | null {
    return this.loading ? 'true' : null;
  }
}
```

## ベストプラクティス
- アクセシビリティ属性をDirectiveで標準化し、マークアップを簡潔に保つ
- nullを返すと属性が削除される仕様を活用し、不要な属性を残さない
- data属性で状態を露出させ、CSSやテストから参照しやすくする

## 注意点
- 文字列で返す必要があるためbooleanを直接返すと`true/false`文字列になる
- 属性名は小文字に統一し、ブラウザ互換性を確保
- フォーム属性など必須属性を誤って削除しないようテストで確認

## 関連技術
- Accessibility (ARIA)
- HostBinding
- Testing Library selectors
