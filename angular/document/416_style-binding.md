# #416 「style バインディング」

## 概要
`@HostBinding('style.<prop>')`でホスト要素のスタイルをディレクティブのプロパティと結びつけ、Renderer2を使わずに動的スタイルを適用できる。

## 学習目標
- スタイルバインディングの書式を理解する
- 数値に単位を付ける方法を学ぶ
- 状態変化に伴うスタイル更新パターンを把握する

## 技術ポイント
- `@HostBinding('style.opacity') opacity = '1';`
- 背景色など文字列プロパティはそのまま渡す
- 数値はテンプレートリテラルで単位を付与

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('style.backgroundColor') bg = '#f1f5f9';
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appFade]',
  standalone: true
})
export class FadeDirective {
  private level = 1;

  @HostBinding('style.opacity')
  get opacity(): string {
    return this.level.toFixed(1);
  }

  fadeOut(): void {
    this.level = Math.max(0, this.level - 0.1);
  }
}
```

## ベストプラクティス
- getterでスタイル文字列を組み立てると複数条件を扱いやすい
- 動的スタイルが複雑化する場合はCSSクラスに委譲
- アニメーションはCSSで定義し、ディレクティブはトリガーに集中

## 注意点
- `null`を返すとスタイルが削除されるため意図して使用
- 連続的な更新はパフォーマンスを考慮し`requestAnimationFrame`などで制御
- SSRでスタイルが適切に初期化されることを確認

## 関連技術
- HostBinding
- Renderer2.setStyle
- CSS設計
