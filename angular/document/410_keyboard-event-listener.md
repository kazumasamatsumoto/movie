# #410 「キーボードイベントの監視」

## 概要
キーボードイベントを監視するとショートカットやアクセシビリティ向上が実現でき、フォーカスされた要素に対する`keydown`/`keyup`処理をDirectiveで共通化できる。

## 学習目標
- `keydown`, `keyup`, `keypress`の違いを理解する
- HostListenerでキー情報を取得する方法を学ぶ
- キーボード操作を伴うアクセシビリティ改善手法を把握する

## 技術ポイント
- `@HostListener('keydown', ['$event'])`
- `event.key`, `event.code`, `event.ctrlKey`などで修飾キー確認
- ショートカット登録は`event.preventDefault()`で既定動作を抑止

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('keydown', ['$event.key'])
handleKey(key: string): void { if (key === 'Enter') this.trigger(); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appShortcut]',
  standalone: true
})
export class ShortcutDirective {
  @Output() shortcut = new EventEmitter<void>();

  @HostListener('keydown', ['$event'])
  onKeydown(event: KeyboardEvent): void {
    if (event.key === 'Enter' || (event.key === ' ' && event.target instanceof HTMLElement)) {
      event.preventDefault();
      this.shortcut.emit();
    }
  }
}
```

## ベストプラクティス
- キー判定は`event.key`（ロケール対応）か`event.code`（物理キー）を状況に応じて選択
- アクセシビリティ向上のためSpace/Enterを同時にハンドル
- ショートカット一覧をドキュメント化し、ユーザーへ明示する

## 注意点
- キーボードイベントはフォーカスされている要素にのみ届くため、フォーカス管理を行う
- 修飾キー判定を組み合わせる際はOS差異を考慮
- ブラウザの予約ショートカットを上書きしないよう配慮

## 関連技術
- EventEmitter
- Accessibility (ARIA role/button/checkbox)
- KeyboardEvent API
