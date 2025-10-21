# #374 「ngClass - クラス制御」

## 概要
`ngClass`は要素に付与するCSSクラスを動的に制御するAttribute Directiveで、条件に応じてスタイルを切り替えられる。

## 学習目標
- ngClassの役割と適用例を理解する
- 複数の指定方法（文字列・配列・オブジェクト）を把握する
- 条件付きクラスの付与パターンを設計できるようになる

## 技術ポイント
- `[ngClass]="expression"`でクラス集合を評価
- 文字列/配列/オブジェクトの3形式に対応
- 既存class属性とマージされる

## 📺 画面表示用コード（動画用）
```html
<button [ngClass]="{ 'is-active': active, 'is-disabled': disabled }">アクション</button>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngclass-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button
      type="button"
      class="btn"
      [ngClass]="buttonClasses"
      (click)="toggle()">
      {{ active ? 'ON' : 'OFF' }}
    </button>
  `,
  styles: [`
    .btn { padding: 0.5rem 1rem; border-radius: 9999px; }
    .btn.is-active { background: #0ea5e9; color: #fff; }
    .btn.is-disabled { opacity: .5; pointer-events: none; }
  `]
})
export class NgClassDemoComponent {
  protected active = false;
  protected disabled = false;

  protected get buttonClasses(): Record<string, boolean> {
    return {
      'is-active': this.active,
      'is-disabled': this.disabled
    };
  }

  protected toggle(): void {
    this.active = !this.active;
  }
}
```

## ベストプラクティス
- クラス名は役割が明確になるよう命名する
- コンポーネント側でクラス集合を計算し、テンプレートはシンプルに保つ
- 条件が増える場合は`computed`/`signal`で派生状態を作る

## 注意点
- Tailwindなどユーティリティクラスを使う場合は競合に注意
- 文字列指定時のスペルミスが検知しづらいのでレビューで確認
- 変更検知で頻繁に評価されるため、重い計算を式に書かない

## 関連技術
- Renderer2.addClass
- HostBinding
- Angular Signals
