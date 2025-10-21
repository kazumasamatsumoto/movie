# #414 「@HostBinding デコレータ」

## 概要
`@HostBinding`デコレータはディレクティブ内のプロパティをホスト要素の特定プロパティへバインドするための構文で、クラスやスタイルの切り替えを容易にする。

## 学習目標
- `@HostBinding`のシンタックスを理解する
- クラス・スタイル・属性のバインディング例を学ぶ
- 内部状態の更新でDOMが変化するフローを把握する

## 技術ポイント
- `@HostBinding('class.some')`
- `@HostBinding('style.backgroundColor')`
- `@HostBinding('attr.aria-expanded')`

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('attr.aria-expanded') get ariaExpanded(): 'true' | 'false' { return this.open ? 'true' : 'false'; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAriaToggle]',
  standalone: true
})
export class AriaToggleDirective {
  private open = false;

  @HostBinding('attr.aria-expanded')
  get ariaExpanded(): 'true' | 'false' {
    return this.open ? 'true' : 'false';
  }

  toggle(): void {
    this.open = !this.open;
  }
}
```

## ベストプラクティス
- ゲッターで計算値を返し、状態と表示を同期
- バインディング名は明示的に指定し、可読性を高める
- HostBindingとHostListenerを組み合わせてリアクティブな挙動を実装

## 注意点
- バインド先が存在しないプロパティを指定するとランタイムエラーになる
- getterを使う場合は副作用を避け、純粋に値を返す
- パフォーマンスのためにgetter内で重い計算をしない

## 関連技術
- HostListener
- Accessibility属性
- ChangeDetectionStrategy
