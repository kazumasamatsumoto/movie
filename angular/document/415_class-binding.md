# #415 「class バインディング」

## 概要
`@HostBinding('class.class-name')`を使うとホスト要素にクラスを付与・削除でき、ディレクティブの内部状態をCSSスタイルへ反映できる。

## 学習目標
- クラスバインディングの書式を理解する
- 状態管理とスタイル適用の連動方法を学ぶ
- 複数クラスの管理パターンを把握する

## 技術ポイント
- booleanプロパティで付与/削除を制御
- getterで複雑な条件を評価
- HostListenerから状態を更新してクラス反映

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('class.is-active') active = false;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appToggleClass]',
  standalone: true
})
export class ToggleClassDirective {
  @HostBinding('class.is-active') active = false;

  @HostListener('click')
  onClick(): void {
    this.active = !this.active;
  }
}
```

## ベストプラクティス
- クラス名はBEMやプロジェクト規約に従い衝突を避ける
- 複数クラスを切り替える場合は個別HostBindingに分けて管理
- HostBindingとスタイルシートを連携し、表示ルールをCSS側へ集約

## 注意点
- クラスを多用するとスタイル競合が起きるため設計が必要
- 状態変化をトリガーするロジックは確実にテストする
- SSRでは初期状態のクラスが正しく表示されるか確認

## 関連技術
- HostListener
- CSS BEM
- Renderer2.addClass/removeClass
