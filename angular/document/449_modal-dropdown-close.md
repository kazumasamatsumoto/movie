# #449 「モーダル・ドロップダウンの閉じる処理」

## 概要
ClickOutsideディレクティブを利用するとモーダルやドロップダウンの外側クリックで閉じる処理を簡潔に実装できる。閉じるロジックは外部で受け取り、ディレクティブは検知に専念する。

## 学習目標
- モーダル/ドロップダウンの閉じる処理を外部クリックに反応させる方法を理解する
- ディレクティブでイベント検知しコンポーネントで状態を変更する流れを学ぶ
- フォーカスやエスケープキーとの組み合わせを把握する

## 技術ポイント
- Outputイベントで`close`や`outside`を通知
- モーダルコンポーネントで状態をcontrollerする
- フォーカス制御やEscキー対応と組み合わせる

## 📺 画面表示用コード（動画用）
```html
<div class="dropdown" appClickOutside (appClickOutside)="close()">...</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dropdown',
  standalone: true,
  imports: [CommonModule, ClickOutsideDirective],
  template: `
    <div class="dropdown" appClickOutside (appClickOutside)="close()">
      <ul>
        <li><button (click)="select('Profile')">Profile</button></li>
        <li><button (click)="select('Settings')">Settings</button></li>
      </ul>
    </div>
  `
})
export class DropdownComponent {
  protected close(): void {
    console.log('close dropdown');
  }

  protected select(value: string): void {
    console.log('selected', value);
    this.close();
  }
}
```

## ベストプラクティス
- 閉じる処理はコンポーネント側で状態により制御し、ディレクティブは検知だけに集中
- Escキーやフォーカスアウトなど他の閉じるトリガーも併用
- クリックで閉じる条件をInputで渡し、細かな制御を可能にする

## 注意点
- モーダル内部でイベントが伝播して閉じてしまう場合は`stopPropagation`を適切に使用
- iFrameやShadow DOMではイベントが取得できないことがある
- 多重にモーダルが重なる場合はz-indexとイベント順序を考慮

## 関連技術
- ClickOutsideDirective
- Keyboardショートカット(Esc)
- FocusTrap
