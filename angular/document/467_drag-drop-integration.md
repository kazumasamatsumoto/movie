# #467 「ドラッグ&ドロップの連携」

## 概要
ドラッグとドロップを連携させるにはドラッグ側でデータを保持・送信し、ドロップ側で受け取って処理する構造を整え、必要なら共有サービスで状態管理する。

## 学習目標
- ドラッグとドロップのデータ受け渡しの流れを理解する
- EventEmitterやサービスで情報を共有する方法を学ぶ
- 複数ドロップゾーンとの連携を設計する

## 技術ポイント
- DragDirectiveでデータset、DropDirectiveでget
- サービスで現在ドラッグ中のデータを保持
- Outputイベントでドロップ結果を外部へ通知

## 📺 画面表示用コード（動画用）
```typescript
@Injectable({ providedIn: 'root' })
export class DragDataService { data?: unknown; }
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class DragContextService {
  data?: unknown;
}

@Directive({
  selector: '[appDragSource]',
  standalone: true
})
export class DragSourceDirective {
  @Input() dragData?: unknown;

  constructor(private readonly context: DragContextService) {}

  @HostListener('dragstart', ['$event'])
  onDragStart(event: DragEvent): void {
    event.dataTransfer?.setData('text/plain', JSON.stringify(this.dragData));
    this.context.data = this.dragData;
  }
}

@Directive({
  selector: '[appDropTarget]',
  standalone: true
})
export class DropTargetDirective {
  @Output() dropped = new EventEmitter<unknown>();

  constructor(private readonly context: DragContextService) {}

  @HostListener('drop', ['$event'])
  onDrop(event: DragEvent): void {
    event.preventDefault();
    const data = this.context.data ?? event.dataTransfer?.getData('text/plain');
    this.dropped.emit(data);
    this.context.data = undefined;
  }
}
```

## ベストプラクティス
- サービスでドラッグ中のデータを共有し異なるドロップターゲットでも利用可能に
- Drop時にOutputで通知し、利用側が必要な処理を実行
- セキュリティのためデータを検証し、不正入力に対応

## 注意点
- DataTransferは文字列のみ対応のため、オブジェクトはJSON化
- DragContextServiceを使用する場合は並列ドラッグを考慮（IDで識別）
- モバイルでHTML5 Drag & Dropが動作しないケースがある

## 関連技術
- DragContextService
- HTML5 Drag & Drop
- EventEmitter
