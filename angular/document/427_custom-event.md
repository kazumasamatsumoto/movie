# #427 「カスタムイベントの発行」

## 概要
Directiveは内部状態や操作結果をカスタムイベントとして発行でき、利用側は`(appSomething)`で受け取ってアプリケーションロジックに組み込める。

## 学習目標
- カスタムイベントの設計方法を理解する
- イベント名・ペイロードの命名規則を明確にする
- 発火条件とライフサイクルの整理を学ぶ

## 技術ポイント
- `@Output() appDragMoved = new EventEmitter<Point>();`
- ペイロードはオブジェクトで渡し、拡張性を確保
- イベントドキュメントに発火タイミングを記載

## 📺 画面表示用コード（動画用）
```typescript
@Output() appDragMoved = new EventEmitter<{ x: number; y: number }>();
```

## 💻 詳細実装例（学習用）
```typescript
interface DragPosition {
  x: number;
  y: number;
}

@Directive({
  selector: '[appDragTracker]',
  standalone: true
})
export class DragTrackerDirective {
  @Output() appDragMoved = new EventEmitter<DragPosition>();

  @HostListener('document:mousemove', ['$event'])
  onMove(event: MouseEvent): void {
    if (event.buttons === 1) {
      this.appDragMoved.emit({ x: event.clientX, y: event.clientY });
    }
  }
}
```

## ベストプラクティス
- イベントペイロードは変更に強いオブジェクト形式で定義
- イベント名は`appAction`形式で意味を明確にする
- 発火タイミングをドキュメントに記載し、テストで保証

## 注意点
- documentレベルのリスナーを使う場合は解除を忘れない
- 出力イベントが多すぎると利用側の処理が複雑化するため必要最小限に
- イベント発火順序を意識し、依存する処理では整合性を保つ

## 関連技術
- HostListener（document/window宛て）
- RxJSサブジェクト
- Event命名ガイドライン
