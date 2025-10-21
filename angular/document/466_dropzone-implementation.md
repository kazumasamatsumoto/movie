# #466 「ドロップゾーンの実装」

## 概要
ドロップゾーンはドロップ可能な領域を視覚化し、ドラッグ中にスタイルを変更してユーザーにフィードバックを与え、dropイベントで受け取ったデータを処理する。

## 学習目標
- ドロップゾーンの視覚的表現とイベント処理を理解する
- HostBindingを使った状態反映を学ぶ
- dropイベントからデータを取得し利用側で処理する方法を把握する

## 技術ポイント
- `dragenter`/`dragleave`でクラス切り替え
- `drop`で`dataTransfer.getData`
- Outputイベントで受け取ったデータを外部へ渡す

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('class.is-over') over = false;
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dropzone',
  standalone: true,
  imports: [CommonModule, DropDirective],
  template: `
    <div class="dropzone" appDrop (dropped)="handleDrop($event)">
      <p>ここにドロップ</p>
    </div>
  `
})
export class DropZoneComponent {
  protected handleDrop(data: string): void {
    console.log('dropped', data);
  }
}
```

CSS例:
```css
.dropzone { border: 2px dashed #94a3b8; padding: 2rem; text-align: center; transition: background .2s; }
.dropzone.is-over { background: #bfdbfe; border-color: #3b82f6; }
```

## ベストプラクティス
- ドロップ可能状態をスタイルで示し、ユーザーが直感的に操作できるようにする
- 受け取るデータ形式をドキュメント化し、バリデーションを行う
- アクセシビリティのためキーボード操作との連携も検討

## 注意点
- `dragenter`イベントは子要素にも発火するため`contains`チェックで制御
- ドロップしたデータは信頼できないため検証が必要
- モバイルではDrag & Dropが制限されるため代替操作を用意

## 関連技術
- DropDirective
- HTML5 Drag & Drop
- CSSトランジション
