# #423 「デフォルト値の設定」

## 概要
DirectiveのInputにはデフォルト値を設定しておき、利用側が値を渡さなくても安全に動作させることで導入ハードルを下げられる。

## 学習目標
- デフォルト値設定のパターンを理解する
- `ngOnChanges`等で未指定時にフォールバックを適用する方法を学ぶ
- 明示的にドキュメントへ記載する重要性を把握する

## 技術ポイント
- プロパティ初期化で基本値を設定
- Setterや`ngOnChanges`でnull/undefinedをチェック
- `??`演算子や`??=`を活用

## 📺 画面表示用コード（動画用）
```typescript
@Input() appDelay = 150;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDelayHover]',
  standalone: true
})
export class DelayHoverDirective implements OnChanges {
  @Input() delay = 150;

  ngOnChanges(): void {
    if (this.delay < 0) {
      this.delay = 0;
    }
  }
}
```

## ベストプラクティス
- ドキュメントにデフォルト値を明記し、利用者が期待する挙動を理解できるようにする
- プロパティ初期化とバリデーションで二重に安全策を取る
- `@Input({ transform: ... })`を利用して値変換も検討

## 注意点
- `undefined`と`null`は別扱いなので明確に区別
- デフォルト値が複雑なオブジェクトの場合は不変な定数を使う
- 設定が外部ストアと連動する場合は競合しないようにする

## 関連技術
- Angular Input Transform
- TypeScript nullish coalescing
- Directive APIドキュメント
