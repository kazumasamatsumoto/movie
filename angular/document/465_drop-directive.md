# #465 「Drop Directive - ドロップ」

## 概要
Dropディレクティブはドラッグされた要素を受け入れる領域を定義し、dragover/dragenter/dropイベントを処理してドロップデータを扱う。

## 学習目標
- HTML5 Drag & Drop APIの基本を理解する
- ドロップゾーンにイベントを設定する方法を学ぶ
- データ転送と許可判定の仕組みを把握する

## 技術ポイント
- `dragover`で`event.preventDefault()`しドロップ可能に
- `drop`イベントで`event.dataTransfer`からデータ取得
- HostBindingでドロップ中のスタイルを変更

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('dragover', ['$event']) onDragOver(event: DragEvent) { event.preventDefault(); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDrop]',
  standalone: true
})
export class DropDirective {
  @HostBinding('class.is-over') over = false;
  @Input() accept?: string[];
  @Output() dropped = new EventEmitter<string>();

  @HostListener('dragover', ['$event'])
  onDragOver(event: DragEvent): void {
    event.preventDefault();
  }

  @HostListener('dragenter', ['$event'])
  onDragEnter(event: DragEvent): void {
    event.preventDefault();
    this.over = true;
  }

  @HostListener('dragleave')
  onDragLeave(): void {
    this.over = false;
  }

  @HostListener('drop', ['$event'])
  onDrop(event: DragEvent): void {
    event.preventDefault();
    this.over = false;
    const data = event.dataTransfer?.getData('text/plain');
    if (!data) return;
    if (this.accept && !this.accept.includes(data)) return;
    this.dropped.emit(data);
  }
}
```

## ベストプラクティス
- `dragover`で`preventDefault`を呼び、ドロップを許可
- HostBindingでドロップゾーンのビジュアルを変えユーザーへフィードバック
- Inputでドロップ可否を判定し、柔軟な制御を提供

## 注意点
- DataTransferは文字列のみのため複雑なデータはJSON化する
- 画像ファイルなど`files`経由のドロップにも対応する場合は追加処理が必要
- ブラウザ間でイベント挙動が異なるため検証する

## 関連技術
- Drag & Drop API
- EventEmitter
- DragDirectiveとの連携
