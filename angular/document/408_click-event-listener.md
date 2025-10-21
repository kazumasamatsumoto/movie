# #408 「クリックイベントの監視」

## 概要
クリックイベントをHostListenerで監視し、ホスト要素のクリックに応じた処理や状態更新を行うのは最も基本的なディレクティブパターンである。

## 学習目標
- `click`イベントをHostListenerで処理する方法を理解する
- `$event`からDOM情報を取得する手順を学ぶ
- preventDefaultとの組み合わせによる挙動制御を把握する

## 技術ポイント
- `@HostListener('click', ['$event'])`
- `$event.preventDefault()`で既定動作を停止
- `Event.target`を利用してクリック元を判断

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('click') handleClick(): void { this.toggle = !this.toggle; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appToggleOnClick]',
  standalone: true
})
export class ToggleOnClickDirective {
  @HostBinding('class.is-active') active = false;

  @HostListener('click', ['$event'])
  onClick(event: MouseEvent): void {
    event.preventDefault();
    this.active = !this.active;
  }
}
```

@Component({
  selector: 'app-click-demo',
  standalone: true,
  imports: [CommonModule, ToggleOnClickDirective],
  template: `
    <button type="button" appToggleOnClick>クリックで切り替え</button>
  `
})
export class ClickDemoComponent {}

## ベストプラクティス
- クリックの副作用は軽量に留め、複雑なロジックはサービスへ委譲
- `preventDefault()`や`stopPropagation()`は必要時のみ使用する
- HostBindingで表示状態を同期しテンプレートの可読性を高める

## 注意点
- ボタンやリンク以外の要素にクリックを付ける際はアクセシビリティ対応を行う
- タッチイベントとの互換性を考慮し、モバイルでの挙動をテストする
- イベント重複（ダブルクリックなど）が問題にならないか確認

## 関連技術
- HostBinding
- EventEmitter
- Accessibility（role/buttonなど）
