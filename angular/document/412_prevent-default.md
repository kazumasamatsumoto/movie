# #412 「preventDefault() の使用」

## 概要
`preventDefault()`はイベントの既定動作を抑止するメソッドで、HostListener内で呼び出すことでリンク遷移やフォーム送信を制御できる。

## 学習目標
- `preventDefault()`の役割を理解する
- HostListener内での使用例を学ぶ
- `stopPropagation()`との違いを把握する

## 技術ポイント
- `event.preventDefault()`で既定動作を無効化
- `event.stopPropagation()`でバブリングを停止
- 入力制御ではユーザー体験に配慮して適切に使用

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('click', ['$event']) onClick(event: MouseEvent) { event.preventDefault(); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appPreventSubmit]',
  standalone: true
})
export class PreventSubmitDirective {
  @HostListener('submit', ['$event'])
  onSubmit(event: Event): void {
    event.preventDefault();
    console.log('submit prevented');
  }
}
```

## ベストプラクティス
- preventDefaultの理由をコメントやドキュメントで明示
- フォーカス移動やアクセシビリティへ影響しないか検証
- 代替アクション（独自送信処理など）を確実に提供

## 注意点
- リンクに使用する場合はキーボード操作の動作も確認
- フォーム送信を抑止するとバリデーションやエラーハンドリングも手動で行う必要がある
- ブラウザの既定動作に依存する機能（印刷ダイアログなど）を阻害しないよう配慮

## 関連技術
- Event.stopPropagation
- Angular Forms
- Accessibilityガイドライン
