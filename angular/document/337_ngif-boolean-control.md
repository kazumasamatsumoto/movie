# #337 「真偽値での表示制御」

## 概要
真偽値を使った`*ngIf`制御は最も基本的なパターンであり、状態フラグを定義してUIを切り替える。

## 学習目標
- booleanフラグによる表示制御を設計する
- Signal/Observableの値をbooleanに変換する方法を理解する
- falsy値の扱いで起こりがちなバグを防ぐ

## 技術ポイント
- `!!value`で明示的にboolean化
- `AsyncPipe`でObservableを解決し、truthy/falsy判定を行う
- `signal`や`computed`で状態をまとめると可読性が高い

## 📺 画面表示用コード（動画用）
```html
<button (click)="toggle()">Toggle</button>
<div *ngIf="isVisible">表示中です</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-boolean-control-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <label>
      <input type="checkbox" [checked]="visible()" (change)="toggle()" />
      説明を表示
    </label>
    <section *ngIf="visible()">真偽値で制御されたセクション</section>
  `
})
export class BooleanControlDemoComponent {
  private readonly flag = signal(true);
  protected visible = this.flag.asReadonly();
  protected toggle(): void {
    this.flag.update(value => !value);
  }
}
```

## ベストプラクティス
- booleanフラグの命名は`isLoading`, `hasError`のように状態が分かる形にする
- `AsyncPipe`使用時はnullを返さないようにデフォルト値を設定する
- Signalを活用して状態更新とテンプレート更新をシンプルに保つ

## 注意点
- `0`や`''`などのfalsy値を判定したい場合は明示的に比較を行う
- 真偽値以外の型を条件に渡すと意図しない表示になることがある
- 複数のフラグが絡む場合は状態オブジェクトにまとめる

## 関連技術
- Angular Signals
- AsyncPipe
- Reactive Forms (状態管理例で利用)
