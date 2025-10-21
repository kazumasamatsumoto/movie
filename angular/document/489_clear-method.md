# #489 「clear() メソッド」

## 概要
`ViewContainerRef.clear()`はコンテナ内にあるEmbeddedViewをすべて破棄し、構造ディレクティブの条件変更時などに不要なビューをまとめて削除できる。

## 学習目標
- clearメソッドの用途と挙動を理解する
- クリア後の状態管理方法を学ぶ
- createEmbeddedViewと組み合わせたビューリセット手順を把握する

## 技術ポイント
- `viewContainer.clear()`
- `viewContainer.length === 0`で空判定
- ViewRefを保持している場合は参照も破棄

## 📺 画面表示用コード（動画用）
```typescript
this.viewContainer.clear();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appResettable]',
  standalone: true
})
export class ResettableDirective {
  constructor(private readonly viewContainer: ViewContainerRef) {}

  reset(): void {
    this.viewContainer.clear();
  }
}
```

## ベストプラクティス
- 条件が変わる前にclearで既存ビューを削除し、新しい状態を生成
- clear後は参照やフラグも初期化して整合性を保つ
- `clear`を呼ぶとViewRefは破棄されるので再利用が必要な場合はdetachを検討

## 注意点
- clearで全てのビューが削除されるため、部分削除は`remove(index)`を使用
- 多数のビューを生成している場合はclearのコストを把握
- clear後に保持している参照へアクセスしないようにする

## 関連技術
- ViewContainerRef.remove
- EmbeddedViewRef
- Structural Directive制御
